"""AVMSD export integration tests; remote publication uses a controlled fake."""
import importlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import avmsd_hf_common as common
import export_huggingface as exporter
import publish_huggingface as publisher

class ExportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.repo = self.base/'source'
        self.repo.mkdir()
        cfg = common.load_config(ROOT)
        for path in cfg['files'] + ['LICENSE']:
            result = subprocess.run(['git', '-C', str(ROOT), 'show', 'HEAD:' + path], capture_output=True)
            if result.returncode:
                if path in cfg['required_files']:
                    self.fail('Required committed source is missing: ' + path)
                continue
            p = self.repo/path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(result.stdout)
        shutil.copytree(ROOT/'huggingface', self.repo/'huggingface')
        self.git('init', '-q')
        self.git('config', 'user.name', 'Export test fixture')
        self.git('config', 'user.email', 'test@example.invalid')
        self.commit()
        self.output = self.base/'export'

    def git(self, *args):
        return common.git(self.repo, *args)

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'Fixture')

    def build(self):
        return exporter.build(self.repo, self.output)

    def rows(self, name):
        return [json.loads(x) for x in (self.output/name).read_text().splitlines()]

    def test_exact_documents_and_nested_sources(self):
        self.build()
        docs = self.rows('documents.jsonl')
        self.assertTrue(any(x['source_path'].startswith('workflows/') for x in docs))
        self.assertTrue(any(x['source_path'].startswith('records/') for x in docs))
        for row in docs + self.rows('synthetic_examples.jsonl'):
            self.assertEqual(row['text'].encode(), self.git('show', 'HEAD:' + row['source_path']))
        for path in common.load_config(self.repo)['chunk_files']:
            text = ''.join(x['text'] for x in self.rows('knowledge_chunks.jsonl') if x['source_path'] == path)
            self.assertEqual(text.encode(), self.git('show', 'HEAD:' + path))

    def test_synthetic_records_are_separate_and_legal_status_preserved(self):
        self.build()
        self.assertEqual(len(self.rows('synthetic_examples.jsonl')), 2)
        self.assertTrue(all(x['synthetic'] for x in self.rows('synthetic_examples.jsonl')))
        self.assertFalse(any(x['synthetic'] for x in self.rows('documents.jsonl')))
        for row in self.rows('knowledge_chunks.jsonl'):
            self.assertIn('control/legal-status.yaml', row['required_context_paths'])
        p = json.loads((self.output/'provenance.json').read_text())
        self.assertEqual(p['source_legal_status']['national_adapter']['status'], 'blocked')
        self.assertFalse(p['source_review_refreshed'])

    def test_fences_and_frontmatter_reconstruct_exactly(self):
        text = '---\nstatus: draft\n---\n# Title\nintro\n## One\n```md\n## Not a boundary\n```\nA\n## Two\nB\n'
        sections = exporter.sections(text)
        self.assertEqual(len(sections), 3)
        self.assertEqual(''.join(x[2] for x in sections), text)
        self.assertIn('Not a boundary', sections[1][2])

    def test_repeatable_output(self):
        self.build()
        before = {p.name: p.read_bytes() for p in self.output.iterdir()}
        self.build()
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.output.iterdir()})

    def test_unapproved_and_untracked_files_stay_out(self):
        p = self.repo/'guides/not-approved.md'
        p.write_text('Do not export this')
        self.commit()
        (self.repo/'private-notes.md').write_text('Untracked')
        self.build()
        combined = (self.output/'documents.jsonl').read_text()
        self.assertNotIn('not-approved.md', combined)
        self.assertNotIn('Untracked', combined)

    def test_deleted_optional_source_is_removed(self):
        (self.repo/'control/validation-report.md').unlink(missing_ok=True)
        self.commit()
        self.build()
        self.assertFalse(any(x['source_path'] == 'control/validation-report.md' for x in self.rows('documents.jsonl')))

    def test_missing_required_or_changed_license_blocks(self):
        (self.repo/'AGENTS.md').unlink()
        self.commit()
        with self.assertRaises(ValueError): self.build()
        self.git('reset', '--hard', 'HEAD~1')
        (self.repo/'LICENSE').write_text('Changed terms')
        self.commit()
        with self.assertRaises(ValueError): self.build()

    def test_output_inside_checkout_is_rejected(self):
        with self.assertRaises(ValueError): exporter.build(self.repo, self.repo/'generated')

    def test_missing_wrong_and_chatbot_destinations_are_rejected(self):
        for value in ('', 'GarethFW/accessible-chatbots', 'SomeoneElse/avmsd', 'https://huggingface.co/datasets/GarethFW/avmsd', 'GarethFW/your-dataset-name'):
            with self.assertRaises(ValueError): common.destination(value)
        self.assertEqual(common.destination('GarethFW/avmsd-test'), 'GarethFW/avmsd-test')

    def test_private_source_is_rejected(self):
        response = Mock()
        response.read.return_value = json.dumps({'full_name': common.SOURCE, 'private': True, 'visibility': 'private'}).encode()
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        with patch.object(common.urllib.request, 'urlopen', return_value=response):
            with self.assertRaises(ValueError): common.public_source()

    def test_publisher_noop_atomic_commit_and_record_deletions(self):
        self.build()
        api = Mock(); api.repo_info.return_value.sha = 'destination-revision'
        def same(**kw): return str(self.output/kw['filename'])
        result = publisher.publish(self.output, 'fixture-not-real-token', 'GarethFW/avmsd-test', api=api, download=same, check_public=lambda: None)
        self.assertIn('No changes', result)
        api.create_commit.assert_not_called()
        old = self.base/'old'; shutil.copytree(self.output, old)
        p = old/'documents.jsonl'
        rows = self.rows('documents.jsonl')
        rows.append({**rows[0], 'id': 'removed-record'})
        p.write_text(''.join(json.dumps(x) + '\n' for x in rows))
        def previous(**kw): return str(old/kw['filename'])
        publisher.publish(self.output, 'fixture-not-real-token', 'GarethFW/avmsd-test', api=api, download=previous, check_public=lambda: None)
        args = api.create_commit.call_args.kwargs
        self.assertEqual(args['parent_commit'], 'destination-revision')
        self.assertEqual(args['repo_id'], 'GarethFW/avmsd-test')
        self.assertNotIn('.gitattributes', {x.path_in_repo for x in args['operations']})
        report_op = next(x for x in args['operations'] if x.path_in_repo == 'validation_report.json')
        change_report = json.loads(report_op.path_or_fileobj)
        self.assertIn('removed-record', change_report['record_changes']['documents.jsonl']['removed'])
        api.update_repo_settings.assert_not_called()
        api.create_repo.assert_not_called()

    def test_missing_token_foreign_provenance_and_tampered_export_block(self):
        self.build()
        with self.assertRaises(ValueError):
            publisher.publish(self.output, '', 'GarethFW/avmsd-test', check_public=lambda: None)
        api = Mock(); api.repo_info.return_value.sha = 'head'
        p = self.base/'foreign.json'; p.write_text(json.dumps({'source_repository': 'Another/Source'}))
        def wrong(**kw): return str(p if kw['filename'] == 'provenance.json' else self.output/kw['filename'])
        with self.assertRaises(ValueError):
            publisher.publish(self.output, 'fake', 'GarethFW/avmsd-test', api=api, download=wrong, check_public=lambda: None)
        (self.output/'README.md').write_text('Unvalidated change')
        with self.assertRaises(ValueError):
            publisher.publish(self.output, 'fake', 'GarethFW/avmsd-test', api=api, download=wrong, check_public=lambda: None)

if __name__ == '__main__':
    unittest.main()
