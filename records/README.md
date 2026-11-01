# Record creation and handling

Use [templates.yaml](templates.yaml) as typed field contracts and [record.schema.json](record.schema.json) as the executable contract. Create one stable ID per identity, increment record_version for material changes, and retain prior versions in controlled history. Reference exact versions for decisions and asset combinations; do not recycle IDs for unrelated editions.

Every record has scope, provenance, owner, dates, relationships and limitations. Distinct record types preserve separate decisions. Schema validation checks structure; the repository checker also checks typed links, evidence, approvals, versions, counting and selected transitions. It cannot authenticate approvers, verify legal interpretation or examine private playback evidence.

Keep restricted participant, contract and operational evidence in an authorised evidence system. Public records may contain minimised locators and access restrictions, never secrets or identifying research data. Record retention, reuse and model-use permissions. Synthetic records must remain labelled; their fictional approvals cannot authorise real actions.

From the repository root run:

```bash
python3 -m pip install PyYAML==6.0.3 jsonschema==4.26.0
python3 validation/check_repository.py
```

Pass an additional record bundle using `--records path/to/bundle.yaml`. Failure exits nonzero. See [validation limits](../validation/README.md).
