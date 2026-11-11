---
document_id: AV-RUN-01
version: 1.0.0
status: draft_for_review
authority_type: operational_guidance
review_date: '2026-11-11'
repository_baseline: 10f679772fbfa550d4f0b8056726de1ca68ab759
workflow_reference: workflows/workflows.yaml
legal_reading_version: '2010/13/EU consolidated 2025-02-08'
---

# AVMSD operational runbook

A practical guide to managing audiovisual accessibility through policy, commissioning, production, distribution, viewer research, reporting and correction.

**Start with the viewer:** can someone find the programme, choose the access service they need, understand the important meaning, control the experience and get help when something fails? Follow that experience through the actual delivery chain. Owning an access file is only one part of delivering access.

This single-document runbook explains how to operate the repository's existing **WF01–WF12** workflows. It supplements the seven guides, record contracts and public Double-FW guidance matrix. It does not replace them or change their identifiers. Its main delivery workstream is Article 7 accessibility; other applicable AVMSD duties require the specialist routes below. Completing this workstream alone cannot establish whole-AVMSD compliance.

**Adoption state:** draft for competent organisational review. No real service, jurisdiction adapter, report, participant study or compliance claim is approved by this document. The repository contains synthetic examples and validation tools, not an implemented broadcast, regulator or research integration.

## Contents

1. [Use this runbook](#1-use-this-runbook)
2. [Understand the duties and boundaries](#2-understand-the-duties-and-boundaries)
3. [Assign owners and establish policy](#3-assign-owners-and-establish-policy)
4. [Build the service and evidence records](#4-build-the-service-and-evidence-records)
5. [Run the twelve workflows](#5-run-the-twelve-workflows)
6. [Plan access features and editorial meaning](#6-plan-access-features-and-editorial-meaning)
7. [Test the complete viewing journey](#7-test-the-complete-viewing-journey)
8. [Research viewer outcomes responsibly](#8-research-viewer-outcomes-responsibly)
9. [Measure provision and progress](#9-measure-provision-and-progress)
10. [Manage reports and public claims](#10-manage-reports-and-public-claims)
11. [Handle emergencies and complaints](#11-handle-emergencies-and-complaints)
12. [Control automation and agent work](#12-control-automation-and-agent-work)
13. [Adopt, validate and maintain the runbook](#13-adopt-validate-and-maintain-the-runbook)
14. [Find supporting guidance and sources](#14-find-supporting-guidance-and-sources)

## 1. Use this runbook

Use the numbered workflows for each service, programme, supplier or reporting cycle. One person may hold several roles, but record who actually has the decision authority. Disabled contributors and viewers provide expertise; they do not inherit the provider's accountability.

### First working session

1. Read [AGENTS.md](AGENTS.md), the [document index](control/document-index.yaml), [source register](control/source-register.yaml), [source review](control/source-review.md) and [legal status](control/legal-status.yaml).
2. Name the service owner and legal decision owner. Record what work is authorised, by whom, on which systems and until when.
3. Identify the legal entity, service/activity, territories, editorial control, relevant dates, programme editions and delivery routes. List missing facts rather than guessing them.
4. Run WF01 and WF02 to establish sources, classification and national requirements. Inventory and planning can continue while a specific legal question remains unresolved.
5. Use WF03 to turn duties and voluntary commitments into a funded plan. Carry those requirements into commissioning, production, delivery checks and reporting.
6. Create records from the [field contracts](records/templates.yaml) and validate against the [schema](records/record.schema.json). Keep private evidence in an authorised evidence system.
7. Review failures, uncertainty and severe viewer barriers before approving a release, report or claim.

### Choose the right starting point

| Situation | Start here | Continue with |
| --- | --- | --- |
| New service, platform, territory or ownership structure | WF01–WF02 | WF03 and specialist legal routes |
| New commission or programme purchase | WF04 | WF05–WF07 |
| Recut, translated edition or new access asset | WF05 | WF06 and affected research/counting |
| Player, app, packaging or device change | WF06 | WF11–WF12 |
| Viewer study | WF07 | WF11 and decisions informed by findings |
| Reporting period closes | WF08 | WF09 |
| Public emergency information | Existing emergency protocol; WF10 | Urgent access correction and incident review |
| Complaint or discovered barrier | WF11 | WF06 retest; WF12 affected conclusions |
| New law, source conflict or expired approval | WF01/WF12 | Affected workflows only |

The [workflow registry](workflows/workflows.yaml) is the canonical dependency and step-ID reference. Dependencies apply to the affected final operation. They must not prevent discovery research, complaint intake, incident preparation or urgent action already authorised by an emergency protocol.

## 2. Understand the duties and boundaries

### Article 7 in operational terms

Use amended Directive 2010/13/EU, together with the applicable national law, regulator instructions and licence conditions. The primary text checked for this runbook is the [8 February 2025 consolidation](https://eur-lex.europa.eu/eli/dir/2010/13/2025-02-08/eng), especially Article 7. Consolidations assist reading; authentic acts and applicable national provisions control legal interpretation.

| Existing requirement route | EU framework | Operational response |
| --- | --- | --- |
| A7-1: Article 7(1) | Member States ensure continuing, progressive accessibility through proportionate measures without undue delay | Establish the provider's national duties; baseline provision and barriers; implement and measure improvement |
| A7-2P: Article 7(2), first sentence | Regular provider reporting to national regulators | Obtain the actual provider timetable, recipient, format and counting rules |
| A7-2M: Article 7(2), second sentence | Member State reporting to the Commission, beginning 19 December 2022 and every three years afterwards | Keep this public-authority duty separate from provider reporting |
| A7-3: Article 7(3) | States encourage accessibility action plans; any such plan is communicated to the national authority | Prepare owned, resourced actions and establish applicable communication requirements |
| A7-4: Article 7(4) | A single accessible national online information and complaints contact point | Identify that point separately from the provider's support and complaints routes |
| A7-5: Article 7(5) | Accessible emergency information made public through audiovisual services | Prepare and exercise an authorised rapid-response process; correct missing access urgently |

Article 7 does not set a universal EU caption, signing or audio-description percentage, a single accuracy/latency threshold or a single provider reporting date. Label targets by their actual authority: national law, regulator, licence, contract or organisational policy. An internal target cannot weaken a legal duty.

### Classify the activity before deciding obligations

Cover linear television, on-demand editorial catalogues and relevant video-sharing-platform activities through their respective definitions and rules. Include mixed businesses and separately identifiable editorial sections. A professional channel on a platform may need its own assessment.

Check editorial responsibility, selection and organisation, public audience, economic character and principal purpose or separate-section/essential-function tests as appropriate. Free access does not automatically mean non-economic activity. A video on a website, an audio-only podcast or a private communication needs a reasoned scope assessment; its format or label alone does not settle every legal question.

Jurisdiction follows the applicable establishment and other statutory tests, including Articles 2–4 or Article 28a as relevant. An EU viewer, a registered address or a UK head office alone is insufficient. Do not assume every targeted country supplies the same obligations; distinguish country-of-origin duties from specific targeting-based contribution rules.

### Websites, apps, televisions and other delivery surfaces

Inventory every route the provider supplies or relies on: broadcast reception, catch-up, streaming websites, mobile apps, connected-TV apps, set-top boxes, electronic programme guides, embedded players and casting/handoff. Track downloads and offline playback where offered. Their exact legal treatment depends on service and function.

| Assessment | Main question | Evidence boundary |
| --- | --- | --- |
| AVMSD Article 7 and national implementation | Is the audiovisual service becoming accessible under its applicable duties? | Access-feature provision, quality, national targets, emergency information and reporting |
| EAA: Directive (EU) 2019/882, Articles 2(2)(b), 3(6), Annex I Section IV(b) | Can consumers identify, select and view covered audiovisual services and use their access features? | Programme guides, accessible access journeys, transmission, synchronisation and user control; assess covered terminal equipment separately |
| Web Accessibility Directive: Directive (EU) 2016/2102 | Is the website/app of a qualifying public-sector body covered? | Its own scope, exclusions, technical baseline, statement and feedback duties; Article 1(3)(a) excludes specified public-service-broadcaster websites/apps |
| Other applicable law and commitments | Do privacy, equality, consumer, procurement, contract or employment requirements apply? | Separate requirement records, duty holders, methods and evidence |

The EAA expressly addresses covered access services; it is not a reason to replace AVMSD programme obligations with a website scan. Equally, an accessible programme does not prove the player is usable. One observation can support several assessments when linked to each distinct requirement and its limitations. Select and verify the applicable WCAG/EN 301 549 version and legal or contractual basis. Neither standard automatically establishes Article 7 compliance.

Do not transfer EAA microenterprise provisions, CE-marking routes, WAD live-media exclusions or a standard website statement template into AVMSD decisions.

### Route wider AVMSD duties

Use [Guide 07](guides/07-other-avmsd-duties-and-legal-interfaces.md) and the [requirement register](control/requirement-register.yaml). Maintain explicit specialist gaps until assessed.

| Existing route | Relevant areas | Accountable specialist |
| --- | --- | --- |
| OTHER-MINORS | Articles 6/6a: prohibited content, protection of minors and relevant data safeguards | Editorial, safeguarding and privacy |
| OTHER-COMMERCIAL | Articles 9–11 and applicable linear rules: commercial communications, sponsorship, product placement and advertising | Commercial/broadcast counsel |
| OTHER-WORKS | Articles 13–17 as applicable: European works, prominence, independent works and contributions | Catalogue/broadcast compliance |
| OTHER-VSP | Articles 28a–28b: platform jurisdiction and protective/commercial measures | Platform trust and safety/legal |
| OTHER-INTEGRITY | Articles 5, 7a–7b: provider information, prominence and integrity | Product/editorial/legal |
| OTHER-REMEDIES | Articles 14–15 and 28: events, extracts and reply/remedies | Broadcast legal |
| OTHER-COOPERATION | Regulatory cooperation, institutional changes and literacy routes | Legal/policy |

European-works shares concern cultural programming; they are not accessibility or disability-casting quotas. Authentic disability representation is a valuable editorial commitment, assessed separately from access-feature delivery. National or other legal requirements may add obligations. Check current institutional arrangements, including EMFA changes, through WF01 rather than relying on historic regulator descriptions.

## 3. Assign owners and establish policy

### Name accountable people

| Function | Owns | Key evidence |
| --- | --- | --- |
| Executive sponsor/service owner | Resources, service priorities, adoption and correction | Approved policy, action plan and unresolved-risk decisions |
| Legal decision/source owners | Classification, jurisdiction, source currency and national interpretation | Source records, adapter, requirements and scope decisions |
| Commissioner/procurement | Brief, budget, supplier terms and acceptance | Programme/feature specifications, contracts and acceptance records |
| Editorial/access lead | Meaning, feature treatment and competent review | Visual audit, scripts, exact asset versions and editorial decisions |
| Engineering/distribution/product | Packaging, metadata, accessible controls and route reliability | Transformation trace, builds, delivery tests and corrections |
| QA lead and specialists | Valid methods, competent execution and disclosed coverage | Expected/observed results, environments and evidence |
| Research/privacy owners | Participation, instruments, lawful data use and interpretation | Approved research plan, protected findings and restrictions |
| Reporting/publication owners | Reconstructable reports, exact approval and controlled claims | Approved artifacts, handoffs, receipts and claim review |
| Support/emergency leads | Accessible response, urgent correction and escalation | Complaint/incident records and retest evidence |

Consult disabled experts throughout decisions. Provide accessible working arrangements, sufficient time and compensation appropriate to the engagement. Do not treat one person's approval as proof of access for all viewers.

### Adopt an implementable policy

The policy should define:

- Services, legal entities, territories, programmes, languages, routes and suppliers covered.
- How legal requirements, interpretation, contractual commitments and recommended practice are distinguished.
- Feature-specific targets, quality profiles and the authority behind each threshold.
- Commissioning and acquisition acceptance, correction terms, rights checks and change control.
- Accessible UX design-system and branding-system responsibilities for websites, apps, guides, support and communications.
- Editorial judgement, disabled participation, research safeguards and permitted AI use.
- Evidence, retention, reporting, incident handling, escalation and review responsibilities.

Connect each policy commitment to an owner, funded activity, output, intended viewer outcome and review evidence. A policy publication or training attendance figure is activity evidence; it does not show that access improved.

Design-system foundations such as typography, colour, labels, content order, status messages and focus need documented guidance and applicable manual/automated checks. Patterns and components need design requirements, technical techniques, reference implementations and task-based acceptance scripts. Link these to QA and the actual player versions. Accessible branding should help everyone identify the service, build trust, understand expectations and recognise its values without concealing access controls or making essential instructions ambiguous. These are delivery recommendations; identify their adopted authority separately from Article 7.

## 4. Build the service and evidence records

Use [records/README.md](records/README.md), [templates.yaml](records/templates.yaml) and the executable schema. This runbook supplies operating instructions, not an alternative record format.

| Record group | Existing record types | What the operator establishes |
| --- | --- | --- |
| Sources and scope | source, jurisdiction, classification | Exact law/version, service facts, regulator, national method and rationale |
| Duties and plan | requirement, target, action_plan | Actor, authority, applicability, baseline, resources, actions and review |
| Content and supply | programme, feature, editorial, rights, supplier, acceptance | Exact edition, language, duration, feature role, lawful uses and acceptance |
| Delivery and evaluation | route, delivery, quality, viewer, evidence | Configuration, method, observations, outcome limits and protected locators |
| Progress and correction | coverage, improvement, issue, complaint, emergency, monitoring | Counting, comparison, consequences, correction version and retest |
| Decisions and communication | delegation, approval, conclusion, report, submission, claim | Authority, exact artifacts, scoped conclusions and confirmed execution |

Every record needs its stable ID, schema/record version, lifecycle status, synthetic flag, service/period/region scope, provenance, owner, created/updated dates, relationships, limitations and matching data fields. Increment versions for material changes; preserve earlier evidence. Do not insert invented values simply to satisfy a required field. Record an incomplete dependency outside a purportedly complete operational bundle until it can be resolved.

The national adapter is the jurisdiction record plus linked sources, requirements and interpretation evidence. It should identify exact national provisions, applicable dates, service classification, duty holders, regulator/licence, reporting instructions, feature targets, populations, repeat/exclusion rules and review triggers. No real adapter is supplied by the fictional example.

### Keep result meanings separate

| Finding | Exact record vocabulary |
| --- | --- |
| Applicability | `applicable`, `not_applicable`, `unresolved` |
| Asset availability | `present`, `absent`, `unknown` |
| Delivery/quality execution | `pass`, `fail`, `cannot_tell`, `not_tested`, `blocked`, `invalid_assumptions`, `tool_error`, `not_applicable` |
| Viewer finding | `supported`, `partly supported`, `not supported`, `insufficient evidence`, `not evaluated`, `not relevant with rationale` |
| Requirement conclusion | `met`, `not_met`, `cannot_conclude`, `not_applicable` |
| Progress | `improved`, `unchanged`, `worsened`, `cannot_compare` |
| Issue resolution | `open`, `corrected_pending_retest`, `verified_resolved`, `blocked` |

Lifecycle status and workflow execution state are additional, separate fields. Preserve the original tool result, vocabulary/version and normalisation rationale. A tool error is not a pass. Non-applicability requires a scope rationale. A corrected ticket remains pending until retest demonstrates the relevant access has been restored.

Keep participant identities, contracts, credentials and sensitive operational material outside this public repository. Public records may use approved, minimised locators. Define access, retention, disposal and model-use restrictions; a hash identifies bytes but does not prove their accuracy, rights or approval.

## 5. Run the twelve workflows

Each subsection expands the existing three canonical step IDs. Keep the registry's dependencies, output types and authority rules when executing. Complete a step only when evidence and required decisions exist. For a block, record the affected action, owner, reason, missing evidence and exact resume condition. Continue independent work.

### WF01 — Source verification

**Trigger:** intake, changed law/guidance, new reporting period or source conflict. **Owner:** source owner. **Input:** source identities and task. **Dependency:** none.

1. **WF01-S1:** verify currency and read the selected source units. Record URL, issuing body, version, exact provision/section, access date and retrieval limits. Start with primary law for duties.
2. **WF01-S2:** compare conflicting wording with controlling authority. Separate amended law, national implementation, official interpretation and Double-FW practice. Route unresolved interpretation to the legal owner.
3. **WF01-S3:** record the adopted use and its limits; identify unavailable or restricted sources and affected decisions. Do not treat navigation-only retrieval as complete review.

**Output/exit:** versioned source evidence and explicit adoption limits. An unresolved source blocks its affected legal conclusion, not unrelated inventory work. Read [Guide 01](guides/01-service-scope-and-jurisdiction.md).

### WF02 — Service and jurisdiction intake

**Trigger:** new or changed service, editorial model, entity or territory. **Owner:** legal decision owner. **Input:** entity, economic/public-service facts, editorial control and establishment facts. **Dependency:** WF01.

1. **WF02-S1:** classify each editorial and platform activity separately; record alternative interpretations and unresolved facts.
2. **WF02-S2:** establish jurisdiction using the applicable provisions. Retrieve national law, regulator/licence instructions and reporting methods; build the real adapter.
3. **WF02-S3:** obtain the named human's exact scope decision, bound to service, dates and facts. Record unresolved applicability instead of inferring an exemption.

**Output/exit:** classification and jurisdiction records with accountable approval where supported. Use [Guide 01](guides/01-service-scope-and-jurisdiction.md) and [Guide 07](guides/07-other-avmsd-duties-and-legal-interfaces.md).

### WF03 — Legal target and action planning

**Trigger:** approved scope, planning cycle or changed obligations. **Owner:** legal and service owners. **Input:** current requirements, national adapter, inventory and resources. **Dependency:** WF02.

1. **WF03-S1:** map each applicable duty to an actor, source, evidence and owner. Open specialist gaps for wider AVMSD and adjacent laws.
2. **WF03-S2:** establish feature-specific baseline and target methods: population, unit, exclusions, repeats, period and qualifying delivered evidence. Label policy ambitions distinctly.
3. **WF03-S3:** approve funded actions and national interpretations. Assign deliverables, correction owners, due dates and review triggers.

**Output/exit:** requirement, target and action-plan records. Unsupported legal targets or an unverified adapter remain blocked. Use [Guide 02](guides/02-accessibility-duties-and-progress.md).

### WF04 — Commissioning and acquisition

**Trigger:** commission, purchase, supplier change or renewal. **Owner:** commissioner/procurement owner. **Input:** requirements, audience needs, reference programme and proposed rights. **Dependency:** WF03.

1. **WF04-S1:** inspect actual assets and rights before commitment. Match episode, edition, language, duration, territory, platform and period; ask for missing access assets.
2. **WF04-S2:** contract deliverables, destination profiles, metadata, review access, acceptance criteria, correction deadlines, redelivery and reuse rights. Budget for independent QA and participation.
3. **WF04-S3:** review supplier evidence and record acceptance conditions. A declaration or delivery receipt alone cannot establish quality or permission to distribute.

**Output/exit:** programme, feature, rights, supplier and acceptance records. Record conditional/rejected/blocked acceptance honestly; supplier acceptance does not establish downstream readiness. Use [Guide 03](guides/03-commissioning-production-and-acquisition.md).

### WF05 — Production and editorial review

**Trigger:** new production, recut, language version or changed treatment. **Owner:** editorial/access lead. **Input:** requirements, reference picture/sound, scripts and rights. **Dependency:** WF04.

1. **WF05-S1:** audit meaning conveyed visually and through sound. Plan captions/SDH, signing, description and spoken subtitles separately, including relevant integrated explanation.
2. **WF05-S2:** produce and independently review the exact assets. Verify names, timing, sound, reveals, language, mix and fit with the final cut. Recheck after edits.
3. **WF05-S3:** approve the editorial route against applicable obligations. A no-separate-AD decision requires a version-specific visual audit and listening review; it cannot override a legal quota.

**Output/exit:** versioned features, editorial decisions and quality evidence. Use [Guide 03](guides/03-commissioning-production-and-acquisition.md) and Section 6.

### WF06 — Packaging and delivery verification

**Trigger:** new or changed asset, package, route, app/player or device configuration. **Owner:** delivery owner. **Input:** exact approved programme/features, rights and route specifications. **Dependency:** WF05.

1. **WF06-S1:** trace master, supplied, packaged, transmitted, player-presented and viewer-experienced states. Preserve identifiers and conversion history.
2. **WF06-S2:** verify the test setup, then run playback, selection and persistence tests on the relevant route matrix. Record expected versus actual behaviour and evidence.
3. **WF06-S3:** retain failures, untested routes and invalid results. Identify which observations qualify as delivered provision under the adopted counting method.

**Output/exit:** route, delivery, quality and evidence records; route defects to WF11. Unsupported provision/readiness claims stop. Use [Guide 04](guides/04-access-feature-quality-and-delivery.md) and Section 7.

### WF07 — Viewer research

**Trigger:** discovery, format decisions, formative work or delivered evaluation. **Owner:** research/privacy owners. **Input:** permitted research question, accessible instruments and versioned material. **Dependency:** WF03 for dependent decisions; discovery may start independently.

1. **WF07-S1:** recruit beyond current successful viewers. Trial accessible tasks, questions and exports. Confirm lawful data handling, participation arrangements and safety.
2. **WF07-S2:** run permitted tasks on the specified programme/route. Record assistance, abandonment, comprehension, control and reported experience distinctly.
3. **WF07-S3:** analyse differences, missing viewers, severe minority barriers and uncertainty. Keep observed performance separate from satisfaction and from legal conclusions.

**Output/exit:** protected viewer/evidence records and correction recommendations. Preserve the unresolved public-taxonomy dependency described in Section 8. Use [Guide 05](guides/05-viewer-outcomes-and-research.md).

### WF08 — Provision and progress calculation

**Trigger:** period end, inventory correction or changed evidence. **Owner:** reporting owner. **Input:** counting rules, eligible inventory and qualifying delivery evidence. **Dependency:** WF06.

1. **WF08-S1:** validate populations, units, durations and intervals. Reconcile acquisitions, exclusions, repeats, failures and missing assets.
2. **WF08-S2:** calculate provision separately for each feature and stage. Reconcile baseline/current catalogue and method changes before comparison.
3. **WF08-S3:** review absolute and percentage change, limitations and contradictory evidence. Use `cannot_compare` where comparison is unsupported.

**Output/exit:** coverage and improvement records with reproducible evidence. No unsupported aggregate accessibility score. Use [Guide 02](guides/02-accessibility-duties-and-progress.md) and Section 9.

### WF09 — Regulator reporting and plan communication

**Trigger:** actual national provider deadline or plan communication. **Owner:** authorised reporting owner. **Input:** national instructions, reviewed evidence and current authority. **Dependency:** WF08 for dependent figures/conclusions.

1. **WF09-S1:** reconstruct each figure and scope each conclusion. Include unresolved failures, limits, action-plan progress and required national fields.
2. **WF09-S2:** obtain approval for the exact report/plan artifact, figures, wording, period, recipient and scope. Bind versions/digests and supporting dependencies.
3. **WF09-S3:** hand off or submit through an actually supported, authorised channel. Verify receipt and preserve the submitted artifact and transaction reference.

**Output/exit:** conclusion, report, approval and submission records. Preparation is not submission; communication of a plan should follow the applicable national route rather than wait unnecessarily for a later reporting cycle. Use [Guide 06](guides/06-reporting-emergencies-and-corrective-action.md).

### WF10 — Emergency exercise and response

**Trigger:** controlled exercise or real incident. **Owner:** emergency lead. **Input:** national instructions and approved rapid protocol. **Dependency:** WF03 for planning; existing incident authority governs urgent action.

1. **WF10-S1:** identify the current message/version, essential instruction, accessible variants, responsible operators and update routes.
2. **WF10-S2:** exercise or respond within existing authority. Test delivery of the actual instruction, location, timing and updates through relevant modalities.
3. **WF10-S3:** retain missing/contradictory variants, escalate and correct urgently. Record activation/transmission times and review causes afterwards.

**Output/exit:** emergency, issue and evidence records. Exercises remain labelled and controlled; they do not establish real incident performance. Use Section 11 and [Guide 06](guides/06-reporting-emergencies-and-corrective-action.md).

### WF11 — Complaint correction and retest

**Trigger:** complaint, escaped barrier or regression. **Owner:** service owner. **Input:** observed barrier and affected asset/route, with uncertainty preserved. **Dependency:** WF06 for related delivery evidence; complaint intake and triage need not wait.

1. **WF11-S1:** triage consequences, reach and urgency. Assign correction and support owners; identify affected programmes, routes, calculations and claims.
2. **WF11-S2:** apply the versioned fix within authority. Preserve the original failure and the causal evidence; coordinate supplier redelivery where needed.
3. **WF11-S3:** retest actual delivery and relevant neighbouring routes. Verify the original barrier where feasible, communicate the supported result accessibly and reopen remaining issues.

**Output/exit:** complaint, issue, delivery and quality records. Mark `verified_resolved` only with sufficient retest evidence. Use [Guide 04](guides/04-access-feature-quality-and-delivery.md) and [Guide 06](guides/06-reporting-emergencies-and-corrective-action.md).

### WF12 — Monitoring reassessment and claim review

**Trigger:** changed law, programme, rights, supplier, configuration, evidence or authority expiry. **Owner:** service/legal/publication owners. **Input:** affected records and valid authority. **Dependency:** WF09 for review of its reporting/claim outputs; other change triage continues independently.

1. **WF12-S1:** identify affected requirements, assets, evidence, reports and claims. Determine the smallest justified reassessment scope.
2. **WF12-S2:** reopen conclusions and agree scoped wording based on current evidence. Preserve contradictions and prior failures.
3. **WF12-S3:** approve the exact handoff or amend/withdraw unsupported claims through an authorised publication process. Confirm what actually changed.

**Output/exit:** monitoring, conclusion, approval and claim records. Reapproval is required when bindings change. Use [Guide 06](guides/06-reporting-emergencies-and-corrective-action.md) and [Guide 07](guides/07-other-avmsd-duties-and-legal-interfaces.md).

## 6. Plan access features and editorial meaning

The following are production and assessment recommendations. Adopt exact language/destination quality profiles with competent specialists; do not present illustrative defaults as EU legal thresholds.

| Feature | Plan and assess | Avoid assuming |
| --- | --- | --- |
| Captions/SDH | Dialogue, speaker identification, meaningful non-speech sound, accurate meaning, readable grouping, timing and placement | Translation subtitles or an unchecked speech-recognition transcript provide complete SDH |
| Audio description | Important visual meaning, action, relevant graphics, orientation, genre, emotion, humour and reveal timing; intelligible mix preserving important sound | Every genre needs the same treatment, or a transcript automatically substitutes for synchronised description |
| Sign language | Correct target sign language, competent translation/presentation, legible framing, lighting, size and delivery; Deaf-user review | Signing is universal across languages or interchangeable with captions |
| Spoken subtitles | Essential translated on-screen speech/text made audible with coordinated description and sound | AD necessarily covers all translated dialogue, or overlapping tracks remain understandable |
| Integrated explanation | Essential names, places, graphics, demonstrations and instructions conveyed naturally in the main soundtrack | Calling a production audio-led removes the need to audit the final picture or meet an applicable quota |

For factual work, prioritise practical instructions, evidence and accurate explanation. For drama and entertainment, also protect character information, suspense, visual humour, tone and emotional meaning. Describe supported observations; do not invent motives or identities. Radio-style orientation and clear introductions can reduce avoidable visual dependence before separate access assets are produced.

Supply access teams with the final reference cut, verified names/pronunciations, scripts/running orders, graphics text and suitable audio stems. Caption the actual final soundtrack. Each recut, crop, language version, graphic alteration or remix requires an impact assessment. Independent specialist review should evaluate meaning as well as file validity.

AI-generated captions, descriptions or translations need competent human review against the actual programme. Log the tool/model version and corrections where used. Do not send restricted production or participant material to a model without authority and appropriate rights/data controls.

## 7. Test the complete viewing journey

### Define the route matrix

For each claimed route, bind programme/episode/edition, feature and language, region, delivery profile, player/app build, device/firmware, operating system, network context and relevant assistive technology/settings. Identify risk-based samples and untested combinations. Tests on a browser do not establish equivalent behaviour on connected television or mobile apps.

### Execute the checks

| Layer | Checks and methods | Preserve |
| --- | --- | --- |
| Source and package | Correct cut, rights, track roles/languages, timing origin, frame rate, syntax/profile and metadata | Exact files, versions, profile, tool version and validation result |
| Editorial quality | Dialogue/sound fidelity, description adequacy, signing quality, translated meaning and reveal order | Specialist judgement, individual meaningful errors and timed locators |
| Transmission | Tracks/metadata survive conversion, transcoding, broadcast/distribution and regional variants | Transformation trace and actual output evidence |
| Discover and select | Programme-guide information, labels, access-feature search/discovery, accessible track controls and clear feedback | Keyboard, screen-reader, remote-control and other relevant interaction observations |
| Watch and control | Start/end, synchronisation, intelligibility, pause, seek, resume, speed where supported and preference retention | Expected/observed behaviour and failures |
| Boundaries and recovery | Adverts, episode changes, live-to-catch-up, downloads, casting and device handoff where offered | What persists, what fails, recovery and untested routes |
| Support | Accessible help/contact, understandable responses and correction verification | Actual contact journey and evidence restrictions |

Use automated syntax/metadata checks for suitable questions, manual playback and assistive-technology checks for interaction, and competent specialists for editorial quality, signing, live-service quality and photosensitivity methods. An axe scan of player controls cannot establish meaningful captions, adequate description or safe flashing imagery. Do not expose participants to suspected unsafe material as a substitute for specialist assessment.

For each execution, record method/version, valid assumptions, environment, evaluator competence, expected result, actual observation, timestamp/locator and protected evidence. Preserve `invalid_assumptions`, `tool_error`, `blocked` and `not_tested` results distinctly.

If AD is present in the master but absent from the viewer's player, record source availability as `present` and the relevant delivery execution as `fail`. Assign the packaging, metadata, transmission or interaction fault and retest the actual route after correction. Do not count source presence as established usable access.

## 8. Research viewer outcomes responsibly

Ask whether people can find, understand, control and enjoy the delivered experience, recover from problems and obtain support. Include people excluded before playback: registration, payment, discovery and support barriers can hide them from a study of existing successful viewers.

Use voluntary, overlapping access-needs lenses and relevant languages rather than assumed diagnoses. Include relevant blind/partially sighted viewers, Deaf/hard-of-hearing viewers, sign-language users, cognitive and combined needs as justified by the research question. No universal participant count or task-time threshold is established here.

### Resolve the outcome-taxonomy dependency

[Guide 05](guides/05-viewer-outcomes-and-research.md) and the schema retain `IDSO-01`–`IDSO-20` references. The newer [public guidance matrix](AVMSD_Double_FW_Guidance_Matrix.md), under viewer-outcome selection, marks the public canonical taxonomy source as unresolved. Preserve existing identifiers and values; **do not reconstruct their definitions from private snapshots or invent a replacement mapping**.

The research owner must resolve and review an appropriate public canonical source before treating those ID mappings as operationally established. Until then, draft explicit research questions and measures with this limitation visible. Do not call an incomplete viewer bundle schema-valid or invent IDs to fill it. This dependency does not prevent accessible research planning or lawful independent investigation of a reported barrier.

### Define each measure before collection

Record the decision it informs, definition, task/context, programme/route version, unit/scale, denominator, instrument/version, observation method, assistance rules, missing-data treatment, uncertainty and interpretation limits. Trial the instrument and export codes before use.

Separate:

- **Observed comprehension:** what information or narrative meaning the person could obtain accurately.
- **Interaction performance:** discovery, selection, control, recovery, completion, effort and assistance.
- **Reported experience:** satisfaction, confidence, dignity, equivalence and relevant enjoyment.
- **Study coverage:** who participated, who could not enter, who abandoned and whose needs remain unexamined.

A positive rating cannot establish comprehension or legal conformity. Retain severe minority failures, negative accounts and contradictory evidence alongside averages. Comparisons require compatible tasks, versions, populations and methods; disclose uncertainty and avoid unsupported causal or population claims.

Make invitations, consent, sessions and payment arrangements accessible. Allow pauses and withdrawal under the agreed arrangements. Minimise personal data; have the privacy owner verify the lawful basis and any special-category conditions. Do not publish identifiable small cells or upload participant material for unrestricted model training. Research participation consent is not general permission for reuse. Keep synthetic exercises separate from lived experience and measured satisfaction. Relevant children's protection data must not be repurposed commercially; obtain specialist review of Articles 6a/28b where applicable.

## 9. Measure provision and progress

Maintain the five separate findings used by [Guide 02](guides/02-accessibility-duties-and-progress.md):

| Finding | Question | Supporting record |
| --- | --- | --- |
| Applicability | Which requirement applies to this actor/service/period? | classification, jurisdiction, requirement |
| Provision | What feature was available at which stage and counted by which method? | feature, coverage |
| Quality/delivery | Was the correct feature usable and meaningful on the tested route? | delivery, quality |
| Viewer outcome | What did the actual evaluation establish, for whom and with what limits? | viewer, evidence |
| Progress | What changed against a reconciled baseline? | improvement |

### Calculation procedure

1. Freeze the reporting period and eligible inventory, including exact editions, duration, language, region and service mode.
2. Apply the actual national counting rules where required. State units, repeats, acquisitions, exclusions and treatment of partial provision. Maintain any internal usable-provision measure separately if its method differs from regulatory reporting.
3. Calculate each access feature separately. Identify whether the measure concerns intended, produced, supplied or usable provision; retain missing/failed evidence.
4. Validate denominator membership, units and intervals; reject overlaps, double counting and a numerator greater than its denominator. A zero eligible denominator needs an explicit treatment rather than a fabricated percentage.
5. Link usable-provision figures to qualifying route evidence. Sampled tests do not automatically prove every untested title or route; disclose the inference and its basis.
6. Reconcile catalogue growth, removals, edits, rights, repeat rules and method changes before comparing periods.
7. Report absolute figures and percentage change with limitations; assign `improved`, `unchanged`, `worsened` or `cannot_compare` as supported.

**Synthetic arithmetic illustration:** 600 qualifying minutes out of 1,000 is 60%. A later 700 out of 1,400 is 50%. Accessible minutes increased by 100 while the share fell by 10 percentage points. Explain both changes and population differences. These numbers are not a legal target or real provider evidence.

Never add SDH, AD and signing percentages: features serve different needs and can overlap on the same programme. Keep legal targets, quality failures and viewer outcomes visible even when volume rises. Budget spent, assets commissioned and tickets closed are not equivalent to delivered improvement.

## 10. Manage reports and public claims

### Prepare the evidence pack

Include service/entity/jurisdiction, reporting period, source/method versions, applicable national requirements, eligible inventory, feature-specific calculations, delivery/quality findings, viewer-study limits, significant barriers, correction status and action-plan progress. Identify specialist modules outside the report's assurance scope.

The reporting owner should be able to trace every material figure to the inventory and underlying evidence. Include explanations for acquisitions, repeats, missing features, failed delivery, changed methods and catalogue growth. Use the actual national template and provider deadline, not the Member State's Commission reporting cycle.

### Approve and communicate

1. Validate records and reconcile figures; obtain competent legal, editorial, technical and research review relevant to the claims.
2. Bind approval to the exact artifact/version/digest, dependency versions, wording, figures, period, scope, recipient, named authorised human, authority basis, date and validity.
3. Hand off or submit through an authorised supported channel. Record operation, transaction reference and actual receipt. A handoff record must remain a handoff.
4. If the outcome of transmission is uncertain, check status before retrying; use idempotency where supported or operator reconciliation.
5. Re-review changed figures, wording, periods or dependencies. Keep previous versions and corrections.

Use accessible report formats and clear caveats near affected claims. Do not convert a WAD accessibility statement, an EAA service-information document, a VPAT/ACR or a website audit into an AVMSD regulator report without establishing its actual suitability.

### Control public wording

A claim should name the feature, programmes/population, language, routes, period and evidence boundary. For example, a scoped statement that captions were verified on named builds is more defensible than saying the entire service is accessible. Retain material failures and untested routes. Public claims need approved conclusions and wording, current authority, a destination, expiry/review trigger and withdrawal owner. Preparation, publication handoff and confirmed publication are separate events.

## 11. Handle emergencies and complaints

### Emergency preparation and incident response

Prepare the approved rapid protocol before an incident. Define on-call roles, national instructions, essential information, access variants, sign/language needs, distribution routes, fallback arrangements and version synchronisation. Exercise the chain under controlled conditions and measure whether the instruction actually reaches people.

During an incident:

1. Use the existing authorised command structure and rapid-response protocol.
2. Verify the current instruction, location, time and update version across available variants.
3. Publish/transmit within that authority and correct missing or conflicting access urgently; preserve timestamps and unresolved barriers.
4. Escalate specialist decisions to the emergency lead and relevant owners.
5. Review the incident, causes and preventive actions after immediate response.

Article 7(5) is the duty route. [Directive (EU) 2018/1808, recital 24](https://eur-lex.europa.eu/eli/dir/2018/1808/oj/eng) recognises exceptional cases where accessibility difficulties should not prevent emergency information being made public. It is context, not a general exemption or permission to neglect preparedness. Do not impose ordinary approval delays on urgent public information or invent authority because a situation is urgent.

### Complaints and correction

Maintain accessible provider support alongside information about the designated national contact point. Test the complete complaint journey, including response comprehension and resolution. Do not require a diagnosis or a technical explanation before accepting a barrier report. Zero complaints is weak evidence if people cannot find or use the channel.

Record the available programme, language, approximate time, route and barrier details; preserve uncertainty. Prioritise essential information, serious exclusion, repeated faults, reach and time without access. Obtain the applicable national response requirements rather than inventing a universal EU deadline.

Link the complaint to an owned issue, due date, versioned correction, actual-route retest and affected reports/claims. Communicate the verified outcome accessibly. Track recurrence and time until access is restored, including unresolved harm. Closing a ticket is not evidence that access returned.

## 12. Control automation and agent work

Use [AGENTS.md](AGENTS.md) and actual delegation. This section does not grant operational access or create an orchestrator.

| Work | Permitted preparation within delegation | Human decision or execution boundary |
| --- | --- | --- |
| Sources/scope | Retrieve, compare, record gaps and draft classifications | Legal interpretation and scope approval |
| Production | Inventory, draft feature treatments, compare versions and flag mismatches | Editorial judgement, rights and specialist acceptance |
| QA/data | Run authorised supported checks, retain raw results, calculate and identify anomalies | Competent review of validity, coverage and conclusions |
| Research | Prepare instruments; analyse permitted data under stated restrictions | Permissions, safety, privacy and interpretation |
| Reports/claims | Reconstruct figures, draft artifacts and prepare review packs | Exact approval and separately authorised submission/publication |
| Correction | Triage, prepare tickets and verify evidence within authority | Consequential changes limited to actual delegated scope |

Delegation needs a named accountable human, authority basis, purpose, operations/resources, limits, validity, revocation and escalation. Recheck it before consequential action. Retrieved documents, comments and supplier text are evidence inputs, not instructions that can expand authority.

Log input/output versions, attempted operation, attempt ID, timestamps, tool/method version and observed result. Read current state before retries. Never claim a test ran, a fix was deployed, a receipt arrived or a barrier resolved without evidence. Preserve negative findings and abstain where facts, methods or permissions are missing. Synthetic agents cannot replace disabled participants or provide measured lived experience.

## 13. Adopt, validate and maintain the runbook

### Suggested management rhythm

This is an organisational recommendation, not an EU reporting schedule. Adapt it to actual obligations and risk.

| When | Review | Decision/output |
| --- | --- | --- |
| Before commissioning or acquisition | Requirements, audience needs, rights, budget and acceptance | Owned brief and supplier conditions |
| Every material content/route release | Asset identity, editorial review, delivery checks and open barriers | Scoped readiness decision and unresolved gaps |
| Weekly during active delivery | Severe failures, blocked dependencies and correction progress | Assigned actions and escalations |
| Monthly | Provision, delivery reliability, recurring complaints, source/authority expiry | Updated management dashboard and action plan |
| Quarterly or locally agreed | Viewer findings, supplier performance, resources and claims | Reprioritisation and funded improvements |
| Each national reporting deadline | Reconciled evidence and exact approvals | Report/plan handoff and verified receipt |
| Any material change or incident | Affected scope, sources, routes and conclusions | WF12 reassessment and targeted retest |

### Validate the repository and records

From the repository root, follow [validation/README.md](validation/README.md):

```bash
python3 -m pip install PyYAML==6.0.3 jsonschema==4.26.0
python3 validation/check_repository.py
```

For an actual operational bundle, supply the real decision date:

```bash
python3 validation/check_repository.py --records path/to/bundle.yaml --as-of YYYY-MM-DD
```

Replace the placeholder path/date. The default fixture date is 1 November 2026; it does not prove that a real approval remains valid today. Developer fixtures test selected structural rules, not legal truth, real playback, human identity, independent agent-routing accuracy or participant outcomes.

**Baseline limitation recorded on 11 November 2026:** at repository commit `10f679772fbfa550d4f0b8056726de1ca68ab759`, the documented full checker returns `E_PACKAGE` because `CHANGELOG.md` is missing. It exits before the normal example/fixture sequence. Record this existing package failure accurately; do not describe the full check as passed. A separately executed fixture result must be labelled as such. This runbook does not change that unrelated file requirement.

### Adoption checklist

- Name actual owners and adopt the policy, authority and evidence arrangements.
- Resolve service classification, national sources, jurisdiction and specialist legal modules relevant to the proposed conclusions.
- Resolve the public canonical outcome-taxonomy dependency before relying on IDSO mappings.
- Verify current destination profiles, specialist methods, rights and operational data permissions.
- Resolve package validation blockers and validate the intended operational bundle.
- Build a separate expert-adjudicated, held-out evaluation set; include unseen routes, ambiguity, severe minority barriers and unauthorised-action cases.
- Run a bounded real pilot with competent independent review. Do not call the process proven from synthetic fixtures or one successful cycle.
- Test actual integrations before using them. Record correction effectiveness, escaped barriers and sustained viewer outcomes.

The existing Hugging Face export configuration uses an explicit file list. Adding this document to GitHub alone does not include it in that export or in the seven-guide document index. The new runbook remains a companion entry point. Any later index/export adoption should preserve its draft status, source limits and appropriate chunk context.

## 14. Find supporting guidance and sources

### Repository navigation

| Resource | Use |
| --- | --- |
| [Seven-guide index](guides/README.md) | Task-specific legal, production, delivery and research guidance |
| [Plain English breakdown and evidence guide](AVMSD_Plain_English_Breakdown_and_Evidence_Guide.md) | Background explanation; verify legal details against primary/national sources |
| [Public Double-FW guidance matrix](AVMSD_Double_FW_Guidance_Matrix.md) | Exact public-source pins, relevant sections, fit and specialist gaps |
| [Requirement register](control/requirement-register.yaml) | Existing A7 and OTHER route identifiers |
| [Workflow registry](workflows/workflows.yaml) | Canonical WF01–WF12 steps, dependencies and output types |
| [Records](records/README.md) | Field contracts, schema and evidence handling |
| [Validation report](control/validation-report.md) | Historical executed checks and unresolved adoption gates; compare with current execution |

### Double-FW practice to retrieve for delivery

The following are public repositories already linked by the public guidance matrix. Its pinned files and section locators define the reviewed scope. Consult that matrix before using them; this runbook does not claim a fresh full audit of every repository or its linked bibliography.

| Delivery need | Public Double-FW resource | Apply it to |
| --- | --- | --- |
| Production planning and access-feature distinctions | [Accessible film, TV and video production](https://github.com/Double-FW/Accessible-Film-TV-and-Video-Content-Production-Management) | Briefs, picture/sound planning, suppliers, feature quality and delivery |
| Caption authoring and player behaviour | [Closed-caption subtitle guidance](https://github.com/Double-FW/Closed-Caption-Subtitles) | Meaning, timing, sound/speaker information, tracks, controls and acceptance |
| Evidence and test planning | [Accessibility QA](https://github.com/Double-FW/QA_Accessibility_Testing) | Requirements-to-tests traceability, coverage, result meanings and completion |
| Web player and support interaction | [Phased accessibility QA approach](https://github.com/Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA) | Applicable axe-core checks and manual keyboard/focus work |
| Policy and decision rights | [Inclusion and accessibility policy](https://github.com/Double-FW/Inclusion-and-Accessibility-Policy) | Scope, owners, steering, measures, escalation and bounded automation |
| Owned delivery, assurance and renewal | [Executive and organisational commitments](https://github.com/Double-FW/Executive-and-Organisational-Commitments) | Funded actions, distinct activity/output/outcome measures and controlled claims |
| Ethical research and data | [Data ethics and disability](https://github.com/Double-FW/Data_Ethics_and_Disability) | Purpose limits, minimisation, participation, model-use restrictions and surveillance risks |
| Clear choices and interaction | [Cognitive UX design](https://github.com/Double-FW/Cognitive-UX-Design) | Understandable labels, feedback, recall support and manageable control |
| Accessible brand experience | [POUR for branding systems and CX](https://github.com/Double-FW/POUR-for-Branding-Systems-and-CX) | Recognisability, trust, expectations and inclusive communication |

These resources support practice. They do not establish national quotas, classify European works, grant production rights or provide every specialist signing, description, photosensitivity, safeguarding or broadcast-law method. Preserve the matrix's Partial and Gap findings.

### Primary legal reading

- [Directive 2010/13/EU, consolidated 8 February 2025](https://eur-lex.europa.eu/eli/dir/2010/13/2025-02-08/eng): definitions, jurisdiction, Article 7 and wider duty routes.
- [Directive (EU) 2018/1808](https://eur-lex.europa.eu/eli/dir/2018/1808/oj/eng): Article 1(11) replaces Article 7; recitals 22–24 explain accessibility context and recital 26 discusses integrity and user controls.
- [European Accessibility Act, Directive (EU) 2019/882](https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng): Articles 2(2)(b), 3(6), Annex I Section IV(b), and other applicable scope/obligation provisions.
- [Web Accessibility Directive, Directive (EU) 2016/2102](https://eur-lex.europa.eu/eli/dir/2016/2102/oj/eng): scope and Article 1(3)(a) broadcaster exclusion; assess applicable national requirements separately.

Primary Article 7 text and the named EAA/WAD interface provisions were retrieved for this runbook on 11 November 2026. This focused check does not certify all linked material, update the repository's historic source-review records, establish national obligations or prove that no subsequent change exists. Recheck the relevant current provisions through WF01 before an operational legal decision.

This runbook is original operational guidance for Double FW. See the repository's [MIT licence](LICENSE) for its applicable terms. External legislation, guidance, programmes, contracts and research evidence retain their own rights and restrictions; a repository licence does not grant rights to those materials.
