# Validation report — draft, 1 November 2026

## Executed checks

On 1 November 2026 the offline checker completed successfully against all 26 requested files, seven guide records, 12 workflow definitions, 20 registered sources and 42 linked synthetic records. All **41 developer fixture expectations** passed, including actual instantiated valid/invalid records, missing claim evidence, absent/unauthorised approvers, expired authority, invalid transitions, counting and asset failures. This is a deterministic developer check result, not an AI accuracy estimate or independent evaluation.

The command executed from the working directory was `PYTHONPATH=review-work/build-deps python avmsd-repository/validation/check_repository.py`. For a standalone extracted package use the exact installation and invocation in validation/README.md. Runtime: Python 3.12.14, PyYAML 6.0.3, jsonschema 4.26.0. The validator's default as-of date is fixed for reproducible fixtures; actual operational checks need the real decision date.

Nine independently copied packages were deliberately damaged and checked with `--skip-fixtures`. Every copy returned exit code 1. The original package remained separate.

| Corruption | Result |
| --- | --- |
| broken-local-link | Rejected: E_PACKAGE |
| missing-guide-metadata | Rejected: E_PACKAGE |
| invalid-yaml | Rejected: E_PACKAGE |
| duplicate-source-id | Rejected: E_PACKAGE |
| wrong-reference-type | Rejected: E_TYPE |
| missing-named-approver | Rejected: E_SCHEMA |
| double-counting | Rejected: E_OVERLAP |
| claim-wording-after-approval | Rejected: E_BINDING |
| unsupported-state-transition | Rejected: E_TRANSITION |

Executed checks cover local links/anchors, YAML/JSON parsing, JSON Schema validity/conformance, required files and guide metadata/index consistency, unique IDs, source/workflow/type references, exact programme/asset associations, declared inventory denominators and interval overlap, approval/dependency hashes, authority dates, report figures/receipts and selected execution-state rules. The checker does not execute broadcast/player, research or regulator integrations. It does not measure an agent's routing decisions: fixture routing/status labels are developer reference decisions.

A source change discovered during execution was resolved: the QA_Accessibility_Testing repository is accessible now. Its selected ATLF 1.1 governance/result chunks are pinned as X01, and the explicit adapter retains Cannot tell. Full technical test libraries were not executed. AV-F09 records why an earlier access failure was superseded.

This report does not approve a real provider, legal interpretation, integration or publication.

## Human review and adoption gates

Pending: complete accessible authentic EU text review; actual national adapter and licence/regulator instructions; competent editorial and specialist method verification; actual delivered-media tests; participant permissions and instrument/export validation; source/model-use rights; named operational delegation; independent human evaluation and a bounded real pilot. The source review identifies AV-F01–AV-F09 and their dispositions. No material blocked module is labelled ready for operational use.

## Automation accuracy measures

All measures require an independent competent human reference decision, precise task/scope and a frozen evaluation version. No numeric AI accuracy has been measured in this package.

| Measure | Numerator / denominator | Reference and interpretation |
| --- | --- | --- |
| Unsupported positive conclusions | Positive conclusions unsupported by adjudicated evidence / all positive conclusions | Human requirement decisions; report counts and unsupported rate, never hide it in overall accuracy. |
| Missed applicable requirements/failures | Applicable requirements or failures omitted / all reference applicable requirements/failures | Legal/QA inventory; report applicability and failure recall separately. |
| Incorrect classification | Incorrect service/jurisdiction classifications / all classified cases | Adjudicated legal facts; report unresolved cases separately. |
| Asset/version mismatches | Wrong programme/edition/language/route matches / all proposed matches | Approved inventory and delivered-asset identity; critical mismatches require investigation. |
| Coverage-calculation errors | Incorrect calculations / all attempted eligible calculations | Independently recomputed inventory/method; stratify unit, repeat and denominator errors. |
| Citation/mapping correctness | Correct exact source/version/provision relationships / all evaluated relationships | Primary sources and competent interpretation; separately count unsupported citations. |
| Correct abstention | Required abstentions correctly made / all reference cases requiring abstention | Human insufficiency/authority decisions; prevents guessing through gaps. |
| Unnecessary abstention | Abstentions despite sufficient authorised context / all reference answerable cases | Human sufficiency decisions; distinguishes caution from unusable coverage. |
| Assessment coverage | Applicable items assessed with valid evidence / all reference applicable items | Include unassessed, invalid and blocked items visibly; pair with accuracy. |
| Unauthorised actions | Attempts outside valid delegation / all consequential action opportunities | Reference delegation and logs; report counts, attempts and confirmed external outcomes separately. |

An empty denominator is not zero error. Report not estimable, sample counts, uncertainty, exclusions and abstention alongside conditional correctness. Thresholds remain unset until authorised owners approve them for the actual consequence and service; no universal percentages are invented.

## Finding dispositions

Nine AVMSD review findings have traceable dispositions in source-review.md: one corrected, one superseded by newly verified evidence, four constrained, one excluded and two blocked with impact. The blocked findings concern complete primary-text verification and real national/service applicability. All guidance remains draft; blocked material is not labelled operationally ready. Source/register and record consistency checks do not resolve those human decisions.

Core narrative: approximately 7,158 words including front matter and the secondary READMEs. All seven guides are within 600–900 words; root README, AGENTS.md and secondary READMEs meet their editorial targets. No length overruns were needed.

## What passing does not establish

Schemas and deterministic checks establish selected consistency properties. They cannot authenticate an approver, determine law, verify a protected video or establish participant experience. Developer fixtures are authored examples, not held-out evidence of AI reliability. Before calling the process operational or proven, retain repeated real delegated cycles, independent review, actual correction/retest and viewer outcomes, recurrence/escaped-barrier measures and sustained monitoring. No remote push, broadcast, participant contact, regulatory filing or public claim was performed.
