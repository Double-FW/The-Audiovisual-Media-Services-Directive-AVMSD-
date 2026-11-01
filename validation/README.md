# Run and interpret validation

From the repository root, with Python 3.10 or later:

```bash
python3 -m pip install PyYAML==6.0.3 jsonschema==4.26.0
python3 validation/check_repository.py
```

The default fixture date is **2026-11-01** for reproducibility. For operational record bundles use `--records path/to/bundle.yaml --as-of YYYY-MM-DD` with the actual decision date. Expired fixture approvals will then fail deliberately; use separate maintained operational records. `--root path/to/package` checks a copy; `--skip-fixtures` skips only developer recipes, not the example or package checks.

The checker validates local links/anchors, metadata, YAML/JSON syntax, schemas, IDs, references, selected typed asset relationships, counting, status transitions, evidence and exact approval bindings. It exits nonzero on detected failures. [cases.yaml](cases.yaml) defines executable mutations of the complete synthetic bundle. Mutations instantiate actual invalid records in memory; expected rejection codes are checked. Routing/status labels are developer reference decisions, not evaluated AI routing behaviour. Use independent review to assess routing accuracy.

Before adoption, competent legal, broadcast/access-service, distribution, research/privacy and automation reviewers must build a separate held-out evaluation set. Include actual national obligations, expert-adjudicated edge cases, unseen programme/routes, severe minority barriers and authorised-action decisions. Resolve disagreements, document competence/conflicts, freeze versions and keep answers outside training retrieval. Evaluate proposed agents blind, including abstention, coverage and unauthorised actions. Set acceptance thresholds locally through named human approval and investigate failures before a bounded pilot.

No participant study, independent benchmark, specialist playback suite or real integration was run here. See the [validation report](../control/validation-report.md) for executed checks, measures and unresolved adoption gates.
