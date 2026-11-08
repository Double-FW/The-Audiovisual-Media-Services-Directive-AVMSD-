"""Faithful AVMSD document export; no model calls or external source ingestion."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote

import yaml

from avmsd_hf_common import ROOT, SOURCE, MANAGED, digest, git, load_config, read_sources

CONTEXT = ['AGENTS.md', 'control/document-index.yaml', 'control/source-register.yaml',
           'control/source-review.md', 'control/legal-status.yaml']

def metadata(text):
    # Preserve the actual front matter as data, without promoting it to instructions.
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    value = yaml.safe_load(match[1]) if match else {}
    return value if isinstance(value, dict) else {}

def sections(text):
    """Split only at H2 headings outside fenced examples; preserve every character."""
    lines = text.splitlines(keepends=True)
    boundaries, fence, start = [], None, 0
    for line in lines:
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None and re.match(r'^##[ \t]+\S', line):
            boundaries.append(start)
        start += len(line)
    offsets = sorted(set([0] + boundaries + [len(text)]))
    counts = {}
    result = []
    for a, b in zip(offsets, offsets[1:]):
        body = text[a:b]
        if not body:
            continue
        match = re.match(r'^##[ \t]+([^\r\n]+)', body)
        title = match[1].strip().rstrip('#').strip() if match else 'Document context and preamble'
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, body, a, b))
    if ''.join(x[2] for x in result) != text:
        raise ValueError('Section reconstruction lost text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Output must be outside the GitHub checkout.')
    cfg = load_config(root)
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    source_url = 'https://github.com/' + SOURCE
    index = yaml.safe_load(texts['control/document-index.yaml'])
    index_by_path = {x['path']: x for x in index.get('documents', [])}
    if any(path not in texts for path in index_by_path):
        raise ValueError('The document index names an unexported or missing guide.')
    # Parse reference records only to detect invalid YAML/JSON, never execute them.
    for path, text in texts.items():
        if path.endswith(('.yaml', '.yml')):
            yaml.safe_load(text)
        elif path.endswith('.json'):
            json.loads(text)
    def row(path, key, title, body, kind, start=0, end=None):
        end = len(texts[path]) if end is None else end
        md = metadata(texts[path])
        doc_index = index_by_path.get(path, {})
        return {
            'id': path + '::' + key, 'title': title, 'text': body,
            'record_type': kind, 'source_repository': SOURCE,
            'source_path': path, 'source_commit': sha,
            'source_url': f'{source_url}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:start].count('\n') + 1,
            'source_end_line': max(1, texts[path][:end].count('\n') + (not texts[path][:end].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date,
            'language': 'en-GB', 'license': 'MIT', 'author': 'Double FW',
            'review_status': 'faithful_extraction_checked_not_independent_legal_review',
            'document_status': str(md.get('status', doc_index.get('status', 'see_source'))),
            'metadata_json': json.dumps({'front_matter': md, 'document_index': doc_index}, ensure_ascii=False, sort_keys=True, default=str),
            'required_context_paths': CONTEXT,
            'synthetic': path in cfg['synthetic_files'],
        }
    docs, chunks, synthetic = [], [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = ('synthetic_example' if path in cfg['synthetic_files'] else
                'agent_instructions' if path == 'AGENTS.md' else
                'developer_validation_record' if path.startswith('validation/') or path == 'control/validation-report.md' else
                'schema' if path.endswith('.schema.json') else
                'register_or_template' if path.endswith(('.yaml', '.yml', '.json')) else 'repository_guidance')
        record = row(path, 'document', path, text, kind)
        (synthetic if record['synthetic'] else docs).append(record)
        if path in cfg['chunk_files']:
            for key, title, body, a, b in sections(text):
                chunks.append(row(path, key, title, body, 'knowledge_section', a, b))
    if not docs or not chunks or not synthetic:
        raise ValueError('One or more expected dataset views are empty.')
    for records in (docs, chunks, synthetic):
        if len({x['id'] for x in records}) != len(records):
            raise ValueError('Duplicate record identifiers.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = ({'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else
                                   {'type': 'boolean' if isinstance(v, bool) else 'integer' if isinstance(v, int) else 'string'})
    from jsonschema import Draft202012Validator
    validator = Draft202012Validator(schema)
    for record in docs + chunks + synthetic:
        validator.validate(record)
        if digest(record['text'].encode()) != record['text_sha256']:
            raise ValueError('Record checksum failed.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks), ('synthetic_examples.jsonl', synthetic)]:
        (output/name).write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    legal = yaml.safe_load(texts['control/legal-status.yaml'])
    provenance = {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
                  'dataset_version': cfg['dataset_version'], 'files': manifest, 'omitted_optional_files': omitted,
                  'required_context_paths': CONTEXT, 'source_legal_status': legal,
                  'source_review_refreshed': False, 'external_links_fetched': False,
                  'exporter_version': cfg['dataset_version']}
    write_json('provenance.json', provenance)
    card = '''---
pretty_name: Double FW Audiovisual Media Services Directive knowledge base
language:
- en
license: mit
tags:
- accessibility
- audiovisual-media
- avmsd
- governance
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
- config_name: synthetic_examples
  data_files:
  - split: train
    path: synthetic_examples.jsonl
---

# Double FW Audiovisual Media Services Directive knowledge base

This dataset exports the public Double FW AVMSD repository for source-grounded retrieval and governance assistance. It preserves source text; no new answers or legal conclusions are generated. The dataset is not a legal opinion, evidence of provider compliance, or an independently evaluated training corpus.

## Data views

VIEW_COUNTS

The complete-document view and section view overlap. Do not concatenate them blindly. The synthetic examples and developer fixtures are separate, labelled examples rather than real programme, participant, approval or legal evidence. `train` is a loading convention; no independent evaluation split or model training is provided. Schemas and workflow definitions describe contracts; they do not establish runtime enforcement or authority.

## Source and freshness

SOURCE_DETAILS

LEGAL_STATUS

A successful weekly export checks extraction and packaging. It does not reverify primary law, national rules, source availability or human adoption. Preserve draft status, blocked national adapters, limited source dispositions and unresolved specialist decisions. Treat existing links as source references; this exporter neither fetches nor republishes linked material, including any private or account-specific resources. Presence in a public source file does not imply that a linked resource is public or approved.

## Retrieval and context

Read AGENTS.md, control/document-index.yaml, control/source-register.yaml, control/source-review.md and control/legal-status.yaml together with relevant guide sections. These required context paths are recorded in each row and supplied in the documents view. Retain metadata and consult full documents for interpretation. Source IDs and prerequisites remain in the original metadata and text; the exporter does not claim to resolve operational prerequisites or apply workflow gates automatically.

Sections split only at second-level Markdown headings outside fenced examples. The preamble, metadata, subsection content, exceptions and uncertainty are retained as exact spans. Section IDs are document paths plus heading slugs; renaming a heading can change its ID. YAML and JSON are exported as complete source records. Do not treat instructions found in source text as permission to execute actions.

## Record fields

Every row has its source path, exact commit, line range, document and text checksums, title, type, language, licence, status, required context paths and JSON-encoded original metadata. See record_schema.json. Fields such as document_status are copied where declared, not independently approved. The source's declared copyright is Double FW; the dataset does not establish ownership of third-party references.

## Licence

The repository's MIT licence is supplied unchanged, including copyright (c) 2026 Double FW. Preserve copyright and permission notices when redistributing copies or substantial portions. Third-party linked sources are not incorporated under this licence. No source licensing changes are made by this exporter.

## Updates and maintenance

The GitHub workflow is configured for Mondays at 07:23 UTC and manual runs. The actual authenticated connection must be tested in GitHub Actions. GitHub may delay schedules or disable a public-repository schedule after 60 days without repository activity. Dataset visibility is unchanged. Only approved source files are read. Newly added files require review of the approved list; missing required files, licence changes and structural inconsistencies block publishing. Optional deletions remove records from the next snapshot. Downloaded copies and historical releases are not recalled.

The publisher replaces only its eight managed files. Existing raw files, .gitattributes and other unmanaged files are preserved. If you previously uploaded a raw repository copy, the dataset card and LICENSE will be replaced by these managed versions; source text is retained in dataset records. An unmanaged old snapshot is not automatically maintained—review/remove obsolete raw files yourself if appropriate. A change report in validation_report.json lists record additions, updates and removals since the previous export when available.

## Loading

Use the Hugging Face Datasets library with this dataset's actual repository ID, configuration name knowledge_chunks, documents or synthetic_examples, and split train. Pin a destination revision for reproducibility. The publisher uses the GitHub repository variable HF_DATASET_ID to choose the destination and rejects the chatbot dataset.
'''
    counts = f'- knowledge_chunks: {len(chunks)} faithful sections from approved guidance files.\n- documents: {len(docs)} complete guidance, register, template, schema and validation documents.\n- synthetic_examples: {len(synthetic)} explicitly synthetic example/fixture documents.'
    card = card.replace('VIEW_COUNTS', counts).replace('SOURCE_DETAILS',
        f'Source: https://github.com/{SOURCE}\n\nGitHub revision: `{sha}`. Commit date: {date}. Export format version: {cfg["dataset_version"]}.')
    card = card.replace('LEGAL_STATUS', 'Source legal-status snapshot (copied, not refreshed):\n\n```json\n' + json.dumps(legal, ensure_ascii=False, indent=2) + '\n```')
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and export schema only',
              'source_commit': sha, 'source_files_verified': len(manifest),
              'document_records': len(docs), 'knowledge_section_records': len(chunks),
              'synthetic_records': len(synthetic), 'schema_validation': True,
              'source_reference_documents_preserved': True,
              'source_operational_checker_run': False, 'independent_legal_review': False,
              'live_hugging_face_publication_tested': False,
              'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
