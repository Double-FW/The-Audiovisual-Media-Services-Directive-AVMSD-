---
document_id: AV-MAP-01
version: 0.1.0
status: draft_for_review
authority_type: guidance_dependency_mapping
review_date: 2026-11-01
target_repository_version: 0.1.0
suggested_repository_path: control/double-fw-guidance-matrix.md
source_boundary: Double-FW repositories and retained Double-FW source snapshots only
---

# AVMSD requirements to Double-FW guidance matrix

This matrix connects the AVMSD repository's **13 registered requirement routes**, delivery requirements across all seven guides, and agent/validation controls to relevant Double-FW guidance. The target is the previously produced AVMSD Delivery and Evidence Repository version 0.1.0. This is a companion mapping for retrieval and implementation planning; it does not amend the requirement register or approve a provider.

Only Double-FW guidance is linked. Legal references are retained as identifiers from the existing repository; no additional legal interpretation or outside-source verification is claimed here. Double-FW process guidance supports the work but does not establish national duties, fulfilment of a statutory target or legal conformity.

## Reading the matrix

| Fit | Meaning |
| --- | --- |
| Direct practice | The reviewed guidance directly supports the named practical control. It does not establish implementation or complete legal coverage. |
| Partial | Specific parts are supported; a material specialist method, service fact, authority or implementation remains required. |
| Contextual | Useful adjacent design, ethical or governance guidance; not a method for assessing the legal requirement itself. |
| Gap | No suitable specialist guidance identified in the reviewed Double-FW set. This is not a claim that no such resource can exist elsewhere. |

Source access is a separate question. **† marks a retained snapshot whose repository/file returned 404 during this check.** Its content was available for comparison, but it is not a verified live retrieval dependency. No broken external link is presented as working. Sources without † were successfully retrieved at their pinned URLs on 1 November 2026. The source catalogue records precise identity and limitations.

## 1. Registered requirement routes

Requirement IDs below are unchanged from `control/requirement-register.yaml`. The register's unresolved applicability and specialist blocks remain in force.

| Requirement ID | Repository route | Requirement / duty area | Double-FW guidance and locator | Fit | Use and boundary | Required output/evidence |
| --- | --- | --- | --- | --- | --- | --- |
| A7-1 | AV-G02; WF03/WF08 | Continuous, progressive accessibility through proportionate measures | [DF03](#df03): ATLF-10, ATLF-18; [DF09](#df09): sections 5, 14, 16; [DF16](#df16): delivery and measurement | Partial | Connect baselines, resources, actions and measured change. These methods do not determine national proportionality, quotas or legal sufficiency. | action_plan, coverage, improvement, conclusion |
| A7-2P | AV-G06; WF09 | Regular provider reporting | [DF11](#df11): section 7; [DF12](#df12): section 9; [DF16](#df16): delivery and measurement | Partial | Prepare evidence-led reports with named owners and approval. Provider reporting format, deadline, recipient and actual receipt remain service-specific. | report, approval, submission |
| A7-2M | AV-G06; WF09 | Member State reporting to the Commission | — | Gap | No reviewed Double-FW source establishes this public-authority reporting route. Do not substitute an internal executive report or transfer its timetable to a provider. | requirement with separate duty holder; unresolved dependency |
| A7-3 | AV-G02/AV-G06; WF03/WF09 | Accessibility action plans and communication | [DF16](#df16): delivery and measurement; [DF11](#df11): sections 5, 7; [DF18](#df18): review and renewal | Partial | Build owned, resourced and reviewable plans. These sources do not establish whether a national plan is mandatory or prove communication to the regulator. | action_plan, improvement, approval, submission |
| A7-4 | AV-G06; WF11 | Accessible national information and complaints contact point | [DF06†](#df06): IDSO-08; [DF15](#df15): Assessment protocol and Manual keyboard checks | Partial | Support usability and accessibility checks on a contact journey. Neither source identifies/designates the actual national contact point; provider support is a separate route. | jurisdiction, delivery/quality, complaint |
| A7-5 | AV-G06; WF10 | Accessible emergency information | [DF13†](#df13): Crisis and Emergency Communications; [DF01](#df01): sections 1, 3–4, 7–9; [DF02](#df02): section 10 | Partial | Plan multimodal messages, live preparation and tested delivery. National emergency authority, exact rapid-response procedure and legal treatment remain unresolved; no blanket delay rule is created. | emergency, evidence, issue |
| OTHER-MINORS | AV-G07; WF03 | Audience/minors protection and related data safeguards | [DF07](#df07): Data Collection Principles and AI Training and Accessibility Data; [DF02](#df02): section 11 | Contextual | Supports minimisation and age-sensitive caption design. Does not supply a complete harmful-content, age-assurance, safeguarding or children’s-data legal assessment. | requirement, specialist issue, protected evidence |
| OTHER-COMMERCIAL | AV-G07; WF03 | Commercial communications, sponsorship, placement and linear advertising rules | [DF13†](#df13): Accessible Marketing and Social Media; [DF14](#df14): The Brand Connection | Contextual | Supports accessible, respectful marketing and brand experience. Does not assess advertising-time calculations, prohibited categories, sponsorship independence or placement permissions. | specialist requirement/assessment gap |
| OTHER-WORKS | AV-G07; WF03 | European works, prominence and relevant contribution routes | — | Gap | No reviewed specialist Double-FW method establishes work classification, catalogue share, prominence or financial-contribution calculations. Accessibility percentages are unrelated measures. | specialist requirement/assessment gap |
| OTHER-VSP | AV-G01/AV-G07; WF02/WF03 | Platform jurisdiction and protective/commercial measures | [DF12](#df12): section 10; [DF07](#df07): data-governance principles | Contextual | Supports dependency ownership and data controls. Does not establish VSP classification, jurisdiction, appropriate moderation measures, redress or a universal Article 7 duty for uploads. | classification, jurisdiction, specialist requirement gap |
| OTHER-INTEGRITY | AV-G07; WF03 | Provider information, prominence and programme integrity | [DF04†](#df04): access-service discovery; [DF05†](#df05): themes 5, 10–11; [DF01](#df01): section 9 | Partial | Supports access-feature labels, control, feedback and viewer choice. Does not settle provider disclosure, general-interest prominence or legal permission for overlays/modifications. | route, quality, specialist requirement gap |
| OTHER-REMEDIES | AV-G07; WF03 | Major events, short extracts and reply/remedies | — | Gap | No reviewed Double-FW specialist guidance supports these broadcast-law determinations. Accessible complaints practice cannot establish rights to extracts, events or statutory reply. | specialist requirement/assessment gap |
| OTHER-COOPERATION | AV-G07; WF03/WF12 | Regulatory cooperation, institutions and media-literacy duties | [DF11](#df11): section 8; [DF12](#df12): section 11 | Contextual | Supports internal review, governance reporting and escalation. Does not establish current regulator/Media Board powers, cooperation procedures or media-literacy reporting duties. | monitoring, source review, specialist requirement gap |

## 2. Delivery, assessment and viewer requirements

These are the practical requirements in the guides, including adopted-policy candidates and recommended practice. They are not all direct statutory instructions. Each row identifies the relevant guide section or workflow and the evidence it should produce.

| Repository locator | Requirement / control | Double-FW guidance and locator | Fit | Use and boundary | Required output/evidence |
| --- | --- | --- | --- | --- | --- |
| AV-G01: Build the jurisdiction adapter; WF01/WF02 | Record scope, authority, versions and unresolved interpretation | [DF11](#df11): sections 2–3; [DF12](#df12): D01–D02 in section 10 | Direct practice | Reuse source/applicability register discipline and legal-owner escalation. Service classification and actual national rules still require their own assessment. | jurisdiction, classification, source |
| AV-G02: Plan measurable improvement; WF03 | Turn commitments into funded delivery actions | [DF16](#df16): complete prompt; [DF11](#df11): sections 3, 5, 7; [DF08†](#df08): Roles they own and lifecycle controls | Direct practice | Carry authority → outcome → activity → owner → evidence → review. Do not turn draft targets or unfunded promises into established provision. | action_plan, target, monitoring |
| AV-G02: Plan measurable improvement; WF08 | Feature-specific numerator, denominator and eligible population | [DF03](#df03): ATLF-11, ATLF-18; [DF11](#df11): Measures must explain what they mean | Partial | Use explicit coverage dimensions, denominator and measure definitions. Programme-duration, repeats, overlapping intervals and qualifying-feature algorithms remain AVMSD repository-specific controls. | target, coverage, evidence |
| AV-G02: Interpret five separate findings; WF08 | Separate provision, quality, viewer outcomes and progress | [DF06†](#df06): Core proposition and Relationship to legal-requirement conclusions; [DF16](#df16)–[DF18](#df18): activity/output/outcome/impact distinctions | Direct practice | Keep evidence streams distinct; satisfaction cannot cancel a failure. Commitment-review statuses require an explicit adapter to the AVMSD progress vocabulary. | coverage, quality, viewer, improvement, conclusion |
| AV-G03: Define acceptance before creation or purchase; WF04 | Plan accessibility before production and purchase | [DF01](#df01): Scope and limits; section 7; [DF03](#df03): ATLF-10 Procurement activities | Direct practice | Define audience, feature, language, destination, budget, acceptance and supplier correction before commitment. | programme, feature, supplier, acceptance |
| AV-G03: Define acceptance before creation or purchase; WF04 | Check acquired assets, rights and alternate versions | [DF01](#df01): Scope and limits; sections 7, 9; [DF02](#df02): sections 3, 12 | Partial | Specify and verify deliverables, version identity and redelivery. These sources do not grant rights or replace title/territory/language-specific contract scrutiny. | rights, supplier, acceptance |
| AV-G03: Plan meaning through sound and picture; WF05 | Integrated information and audio-description editorial treatment | [DF01](#df01): sections 2–3, 5, 10 | Partial | Support early descriptive planning, important graphics in sound, intelligibility and genre-appropriate AD. Detailed radio/podcast commentary methods in the separate local AD package have no verified GitHub location here. | editorial, feature, quality |
| AV-G03/AV-G04; WF05/WF06 | Captions/SDH preserve dialogue, speakers and meaningful sound | [DF02](#df02): sections 1, 4, 7–8, 14; [DF01](#df01): section 1 | Direct practice | Apply editorial fidelity and distinct track roles. Translation subtitles and automatic speech recognition are not automatically assessed SDH. | feature, quality, evidence |
| AV-G03/AV-G04; WF05/WF06 | Readable, synchronised captions without obscuring information | [DF02](#df02): sections 5–6, 9, 14 | Direct practice | Review linguistic grouping, cue timing, reveal order, placement and rendering. Numeric source defaults need a justified language/platform profile; they are not EU-wide thresholds. | quality, route, evidence |
| AV-G03/AV-G04; WF05/WF06 | Target-language signing and spoken-subtitle coordination | [DF01](#df01): section 4; [DF02](#df02): section 1 Related services | Partial | Signing is a language service with framing and Deaf-user QA; feature types are distinct. Detailed spoken-subtitle production and collision methods are not established by these sources. | feature, editorial, specialist quality |
| AV-G04: Trace each delivery state; WF06 | Bind programme, cut, language, feature and transformation | [DF01](#df01): sections 7, 9; [DF02](#df02): sections 3, 12, 15 | Direct practice | Retain exact identifiers and references through authoring, conversion, packaging and playback. AVMSD schema field names and identity checks are local implementations. | programme, feature, route, evidence |
| AV-G04: Trace each delivery state; WF06 | Distinguish file presence from delivered usable access | [DF01](#df01): sections 8–9; [DF02](#df02): sections 12–14 | Direct practice | Validate syntax and actual rendition, synchronisation and feature selection. A master, upload receipt or valid file cannot establish viewer access alone. | delivery, quality, issue |
| AV-G04: Trace each delivery state; WF06 | Discover, select and retain features during real viewing | [DF02](#df02): section 13; [DF04†](#df04): access services and spoken interfaces; [DF05†](#df05): themes 4–6, 10–11 | Direct practice | Check labels, controls, state and persistence through seeking/resumption and claimed routes. Advert/episode/device handoff coverage must be specified and executed, not assumed. | route, delivery, viewer |
| AV-G04: Assess distinct features; WF06 | Cognitive clarity and flexible media control | [DF19](#df19): sections 4–10; [DF05†](#df05): themes 2, 6–8 | Direct practice | Use clear messages, recognisable choices, feedback and contextual personalisation. Adapt recommendations to the actual player; do not mandate every output mode for every interface. | feature specification, route, viewer |
| AV-G04: Execute and preserve observations; WF06 | Combine partial automated, manual, keyboard and specialist methods | [DF03](#df03): ATLF-09, ATLF-11–12; [DF15](#df15): Assessment protocol; Manual keyboard checks | Direct practice | Use actual interaction and retain engine/profile versions. A clean scan cannot establish caption meaning, signing quality, AD adequacy, full playback or complete legal compliance. | quality, delivery, evidence |
| AV-G04: Outputs and next workflow; WF06 | Photosensitivity, live quality and destination-specific methods | [DF01](#df01): section 6 and Claims requiring current verification; [DF02](#df02): sections 10, 12 | Partial | Sources identify preparation, risk and the need for a current specialist method/profile. They do not provide every instrument, limit or validated integration. | quality with explicit blocked methods |
| AV-G05: Recruit beyond current successful viewers; WF07 | Include disabled people early and evaluate assembled delivery | [DF01](#df01): section 8; [DF09](#df09): section 7; [DF06†](#df06): Roles and decision rights | Direct practice | Include relevant language/access approaches and people excluded from the journey; participants supply evidence without inheriting compliance accountability. | viewer plan, permissions, evidence |
| AV-G05: Select outcomes without rewriting their IDs; WF07 | Preserve IDSO outcome identities and scope | [DF06†](#df06): IDSO-01–20; Interpreting outcome findings; Stop conditions | Direct practice | Use relevant canonical outcomes and original meanings. Snapshot-only retrieval must be resolved for a live agent dependency; a supported outcome is not a legal pass. | viewer with IDSO IDs and limitations |
| AV-G05: Define and validate measures; WF07 | Separate observed comprehension, reported experience and uncertainty | [DF06†](#df06): Evidence model and Evidence sufficiency; [DF09](#df09): sections 8, 11; [DF11](#df11): section 7 | Direct practice | Define task, denominator, scale, instrument, context, missingness and subgroup findings. Provider/export validation and the actual analysis design need local evidence. | viewer, evidence, instrument contract |
| AV-G05: Protect evidence and interpret carefully; WF07 | Minimise data and keep synthetic/participant evidence separate | [DF07](#df07): collection, research participants and AI training sections; [DF06†](#df06): Synthetic personas and simulated evidence | Direct practice | Respect purpose, access, retention and training-use limits. Data-ethics guidance does not itself establish a lawful basis or permission for commercial reuse. | evidence, viewer, delegation |
| AV-G05: Outcomes; WF07 | Explore dignity, confidence, enjoyment and brand experience | [DF06†](#df06): IDSO-12–18, IDSO-20; [DF14](#df14): emotional brand framing | Contextual | Use the brand interpretation as a research lens. Feeling Valued is not a fifth official POUR principle; brand claims or a WCAG pass do not prove viewer experience. | viewer, research questions, bounded interpretation |
| AV-G06: Prepare and approve reports; WF09 | Prepare reconstructable reports and exact-version approvals | [DF11](#df11): section 7; [DF12](#df12): section 9; [DF17](#df17): assurance prompt | Direct practice | Separate preparation, substantive approval and publication. Regulator-specific fields, calculations, reporting periods and submission/receipt handling need their own implementation. | report, approval, submission |
| AV-G06: Complaints and correction; WF11 | Accessible support, barrier triage, correction and retest | [DF06†](#df06): IDSO-08, IDSO-11; [DF03](#df03): ATLF-10, ATLF-14–15; [DF09](#df09): section 6 | Direct practice | Retain failure, impact, ownership, applied correction and actual retest. Zero complaints or closed tickets cannot demonstrate access or resolution. | complaint, issue, delivery/quality |
| AV-G06: Monitor, decide and hand off; WF12 | Reassess sources, suppliers, assets and claims after change | [DF03](#df03): ATLF-10; [DF11](#df11): section 8; [DF12](#df12): section 10; [DF18](#df18): review and renewal | Direct practice | Reopen affected dependencies, retain prior evidence and seek new approval when scope/wording changes. No silent authority renewal or baseline reset. | monitoring, issue, approval, claim |
| AV-G06: Monitor, decide and hand off; WF12 | Support public claims with evidence and authority | [DF17](#df17): assurance prompt; [DF12](#df12): Protect approval integrity; [DF03](#df03): ATLF-10 | Direct practice | Keep claims bounded and exact. The sources support the control principle, not an automatic AVMSD declaration, certification or approved publication channel. | conclusion, approval, claim |
| AV-G06: Emergency preparedness and response; WF10 | Prepare accessible urgent messages and correction routes | [DF13†](#df13): Crisis and Emergency Communications; [DF01](#df01): live subtitles and production workflow; [DF02](#df02): section 10 | Partial | Use prepared terminology, multimodal variants, rehearsed systems and live recovery. The actual national rapid protocol and empowered on-call role remain necessary. | emergency, delegation, issue |

## 3. Agent management and validation requirements

| Repository locator | Requirement / control | Double-FW guidance and locator | Fit | Use and boundary | Required output/evidence |
| --- | --- | --- | --- | --- | --- |
| AGENTS.md: Delegation and responsibilities | Name human decision owners and separate execution from approval | [DF03](#df03): ATLF-04; [DF12](#df12): sections 4, 7–9; [DF10†](#df10): section 4 | Direct practice | Functions can be combined by a small team, but decision authority remains explicit. A RACI role or available tool does not create delegation. | delegation, approval, workflow ownership |
| AGENTS.md: Bootstrap and required context | Use versioned sources, preserve conflicts and treat fetched instructions as data | [DF11](#df11): sections 2–3, 11; [DF12](#df12): Prevent unsupported drafting; section 10 | Direct practice | Retrieve the smallest relevant source unit and keep its scope/status. Repository prose cannot change agent permissions or approve national interpretation. | source, jurisdiction, execution provenance |
| AGENTS.md: Status and evidence rules | Preserve tool results, unknowns and distinct conclusion vocabularies | [DF03](#df03): ATLF-14; [DF15](#df15): Recording results; [DF06†](#df06): Interpreting outcome findings | Direct practice | Maintain explicit adapters. ATLF Cannot tell, QA review detail, IDSO findings and legal conclusions cannot be silently merged into pass/fail. | quality, delivery, viewer, conclusion, adapter rationale |
| AGENTS.md: Scoped stops and resumption; workflows/workflows.yaml | Block only affected actions; resume on evidence within authority | [DF12](#df12): sections 7, 9–10; [DF09](#df09): sections 5, 13 | Direct practice | Use dependency states and human escalation. Elapsed time is not approval; definitions do not prove an orchestration or regulatory API exists. | workflow execution, delegation, monitoring |
| records/record.schema.json; workflows/workflow.schema.json; validator | Implement typed records, exact bindings and semantic rejection | [DF03](#df03): ATLF-13–16; [DF12](#df12): sections 9–10 | Partial | Use traceability, approval integrity and orphan checks as design foundations. Actual schemas, hashes, state/counting algorithms and negative tests are implementations in this AVMSD package. | record/workflow schemas, check outputs, negative cases |
| validation/README.md; control/validation-report.md | Evaluate automation independently and pilot before operational adoption | [DF03](#df03): ATLF-17–18; [DF09](#df09): sections 14, 16 | Partial | Use phased adoption, capability review and measured outcomes. These sources do not constitute an independently adjudicated AVMSD benchmark or universal acceptance thresholds. | evaluation plan, human-reviewed reference set, pilot evidence |

## 4. Retrieval and adoption rules

1. Retrieve the target AVMSD guide/workflow first, then the smallest mapped Double-FW section. Preserve both source identity and version. A mapping is not a completed test or approved decision.
2. Use the relationship and boundary columns together. A contextual ethics or branding source must not be promoted to specialist legal coverage. A gap remains open until suitable material and an appropriate assessment route are reviewed.
3. Resolve † dependencies before using them for live automated retrieval. Ask the source owner for an accessible canonical repository/version or an authorised versioned copy. Retained snapshots can support review but do not prove current public availability or reuse permission.
4. Keep each source's vocabulary and baseline visible. The pinned QA plan uses axe-core 4.12.1; the embedded source discusses a different baseline. Do not merge engine profiles, numeric defaults or pass counts. Choose and validate the actual assessment configuration separately.
5. Preserve the IDSO outcome IDs. The commitment-renewal prompt's progress labels and ATLF/QA results require explicit adapters to the AVMSD record vocabularies. No automated adapter turns satisfaction into legal conformity.
6. Treat the brand reframing as Double-FW interpretation. Its additional emotional framing is not an extra official POUR principle, and statements about technical proof must not become proof of all experience outcomes.
7. The separate audio-description package has no verified Double-FW GitHub location from this check. Its non-GitHub link is excluded under this matrix's source boundary. Use DF01 for its supported AD content and retain a gap for the package's more detailed commentary/editorial methods.
8. Review source/model-use permissions before ingestion or redistribution. A publicly readable file or a successful link check does not select a licence for the AVMSD repository or authorise use of participant evidence.

## 5. Source catalogue

The links below point to exact files at pinned Double-FW Git snapshots. Locators are named sections, rather than unverified fragment links. For unavailable sources, the expected repository/path is recorded without a live external link. Hashes identify locally retained retrieved text, not a claim about original download byte identity. External bibliographies inside these documents were not followed or incorporated into this matrix.

### DF01

[Accessible TV Content Guidance for Production Teams](https://github.com/Double-FW/Accessible-Film-TV-and-Video-Content-Production-Management/blob/40cf5488e46906807ae8764ff0a191f35a85cea9/Accessible_TV_Content_Guidance_for_Production_Teams.md)

**Access:** pinned file retrieved successfully. **Version:** 1.1-semantic; blob 6ecf75ece7b4d055b12f008656c583243e8a0b79.

**Relevant units:** Sections 1–10; Scope and limits; Claims requiring current verification.

**Retained text SHA256:** `5f1abfbe5155656eb32d08b22d55da943f887e869216bc8b71453be5e4e98923`.

### DF02

[Closed Caption Subtitle Guidelines](https://github.com/Double-FW/Closed-Caption-Subtitles/blob/7ad0f5f1d8a31969f832985b63345ce4988ff1e6/Closed_Caption_Subtitle_Guidelines.md)

**Access:** pinned file retrieved successfully. **Version:** 1.0; blob 554e362590334ab0e42c0ccb3e168358fe2eaff2.

**Relevant units:** Sections 1, 3–15; distinct services, authoring, live production, formats, player operation and acceptance.

**Retained text SHA256:** `feb770e8a95c4c724adfa156b7ddf672a938e11c0f35a7967a4c7f3bb67aafba`.

### DF03

[Accessibility Test-Led Delivery Framework](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Accessibility_Test_Led_Delivery_Framework.md)

**Access:** pinned file retrieved successfully. **Version:** 1.1; blob d3743f13b0f594f0279547bd0073ed6969587846.

**Relevant units:** ATLF-04; ATLF-09–18, especially decision rights, procurement, traceability, results and adoption.

**Retained text SHA256:** `4c57d74ea374099cfe22d032e8c8f5cfcd7db40bcc1b5dc4b8bba2c97bd76694`.

### DF04

**Connected_TV.md — snapshot only (†).**

**Access:** pinned file and repository lookup returned 404. Expected source identity: `Double-FW/Inclusive_and_Effective_Design/blob/14c4416398108df4ff3693277bd354f41de0481c/Connected_TV.md`. This result does not establish whether the repository was removed, renamed, made private or is inaccessible to this connection. **Version:** Git blob 6403e025fb6f3eacfee7d17be23f49a9dcc28534.

**Relevant units:** Whole short guide: access services, consistency, spoken output and disabled-user testing.

**Retained text SHA256:** `32b69846ac074e88ac087c63f44bc6ac6362d2eefc605b07b965d5ad8f7a377b`.

### DF05

**Accessible_Interactive_Media_Control.md — snapshot only (†).**

**Access:** pinned file and repository lookup returned 404. Expected source identity: `Double-FW/Inclusive_and_Effective_Design/blob/14c4416398108df4ff3693277bd354f41de0481c/Accessible_Interactive_Media_Control.md`. This result does not establish whether the repository was removed, renamed, made private or is inaccessible to this connection. **Version:** Git blob 35718b4dc6493646384a3fa30fc619433d224ae9.

**Relevant units:** Themes 1–12: participation, variable needs, controls, feedback, agency and maintainability.

**Retained text SHA256:** `b95a43b72d4f4e850d744f6f9935d7f3909e86518359c25e5ca876d5331220b7`.

### DF06

**Inclusive_Digital_Service_Outcome_Dataset.md — snapshot only (†).**

**Access:** pinned file and repository lookup returned 404. Expected source identity: `Double-FW/Inclusive_and_Effective_Design/blob/14c4416398108df4ff3693277bd354f41de0481c/Inclusive_Digital_Service_Outcome_Dataset.md`. This result does not establish whether the repository was removed, renamed, made private or is inaccessible to this connection. **Version:** Git blob 99515c2231ebf60ee6cde33b4a7b627c7be3e7fe.

**Relevant units:** IDSO-01–20; evidence model, statuses, contradictions, synthetic evidence and decision rights.

**Retained text SHA256:** `d2fe9fbd5a2991a415ab06b4658aecaf50f11403c083b138b57509a61c5a8a7b`.

### DF07

[Ethical and Inclusive Use of Data Relating to Disabled People.md](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/3db809cb035e53bc1825f884f3979fdc73f793a2/Ethical%20and%20Inclusive%20Use%20of%20Data%20Relating%20to%20Disabled%20People.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob 352bf43a2d34fe620be8c2852fe6d1f128df0be7.

**Relevant units:** Data Collection Principles; Customers Versus Research Participants; AI Training and Accessibility Data.

**Retained text SHA256:** `eab553f94c1a3fe5b8ca051c70e297670fe6d7e0aecf92ce464c5d232ebf3059`.

### DF08

**Managing_Embedded_Accessibility_and_Inclusive_Design.md — snapshot only (†).**

**Access:** pinned file and repository lookup returned 404. Expected source identity: `Double-FW/Managing-Embedded-Accessibility-and-Inclusive-Design/blob/0abaf4a737bfd4c780c3de46bac3c0ad991f6a2e/Managing_Embedded_Accessibility_and_Inclusive_Design.md`. This result does not establish whether the repository was removed, renamed, made private or is inaccessible to this connection. **Version:** Git blob f8cfcc4982ce85c9a90caaccb0c7223bc2bff665.

**Relevant units:** Embedded ownership, lifecycle controls and AI governance. Supporting snapshot; no row relies on it alone.

**Retained text SHA256:** `17819f4e67a0ad10343b722d4a2a5e3855630fd885967dbd5b0f3d86ce649ff5`.

### DF09

[Autonomous_Accessibility_Workflow_Management_Guide.md](https://github.com/Double-FW/Shift-Left_Accessibility_AI_Management/blob/27e299f281e4bb9adc78ef07760e12002e28c72a/Autonomous_Accessibility_Workflow_Management_Guide.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob b6c9aeff6e5fb2f3b0f6a6e8d5c3f9a5d371c7e2.

**Relevant units:** Sections 3–11, 13–14, 16: authority, continuous workflow, evidence, research, ethics and adoption.

**Retained text SHA256:** `0181dae6ccfc5bd06e3c55e8f56da5eaae08f0020bf0c87b880df394422faab3`.

### DF10

**Accessibility RACI.md — snapshot only (†).**

**Access:** pinned file and repository lookup returned 404. Expected source identity: `Double-FW/Organisation_Governance_and_Strategy/blob/391f4f6da28f5a3afd83bebdc7ee0edd29c64bc9/Accessibility%20RACI.md`. This result does not establish whether the repository was removed, renamed, made private or is inaccessible to this connection. **Version:** Git blob fe09c0c9d05a1f20e298bd3190d8a5e48d2990a6.

**Relevant units:** Section 4: RACI framework, P6 decision-specific RACI and escalation.

**Retained text SHA256:** `56510aa6c5ad0e1a789928073645caad216c7f6913f3e5c36c3bc369dcda06c3`.

### DF11

[Accessibility_and_Inclusion_Policy_Creation_Guide.md](https://github.com/Double-FW/Inclusion-and-Accessibility-Policy/blob/145b4b2d2ae0680ca0d4c481dbbd077a31beb761/Accessibility_and_Inclusion_Policy_Creation_Guide.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob f9e3ccb18d27dd0131d6d435db280d4c9012194f.

**Relevant units:** Sections 2–3, 5, 7–8 and 11: scope, authority, delivery, measures, source control and review.

**Retained text SHA256:** `3a2fc2a3b62af517dd36d84423e73094b1017d0d16e0cb2b084a6353a264a8a9`.

### DF12

[Accessibility_and_Inclusion_Policy_RACI_and_Steering_Group_Guide.md](https://github.com/Double-FW/Inclusion-and-Accessibility-Policy/blob/145b4b2d2ae0680ca0d4c481dbbd077a31beb761/Accessibility_and_Inclusion_Policy_RACI_and_Steering_Group_Guide.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob b762c54cae25dbebe514d8bcb9324eb1079ba93f.

**Relevant units:** Sections 4, 7–11: decision rights, bounded automation, approval integrity, dependencies and escalation.

**Retained text SHA256:** `7931665122fc9de3d02bd2c34fe606c7782d4ecb53739a3120ddca91bcf783a3`.

### DF13

**Corporate_Communications.md — snapshot only (†).**

**Access:** pinned file and repository lookup returned 404. Expected source identity: `Double-FW/Organisation_Governance_and_Strategy/blob/391f4f6da28f5a3afd83bebdc7ee0edd29c64bc9/Corporate_Communications.md`. This result does not establish whether the repository was removed, renamed, made private or is inaccessible to this connection. **Version:** Git blob 77ded22b4baf368612e4457377a01b9ae5e3a333.

**Relevant units:** Marketing, Corporate Reporting Accessibility, Crisis and Emergency Communications, and Governance.

**Retained text SHA256:** `d325ba42ac92f6a5a64c8f795d9b7f77e402c61f2641e1d40a1418ce2b25279e`.

### DF14

[The WCAG POUR principles reframed through emotional outcomes for branding systems.md](https://github.com/Double-FW/POUR-for-Branding-Systems-and-CX/blob/0e041d8aee75ba5585dd5c78af56f82ad9d626a8/The%20WCAG%20POUR%20principles%20reframed%20through%20emotional%20outcomes%20for%20branding%20systems.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob 79181b0748799d134ef1aed79f2ff97c828d6a39.

**Relevant units:** Feeling framing and The Brand Connection; interpretive brand practice only.

**Retained text SHA256:** `83424425e6b495d860009183772d3770a653337d07888681c7293b8797026d6f`.

### DF15

[Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md](https://github.com/Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA/blob/f2ec12286e15233527196bb223260dd2846e53af/Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob 1b14816fb63afb07de37f7a073f040eb65a11574.

**Relevant units:** Assessment protocol; Manual keyboard checks; Recording results; versioned rule profiles.

**Retained text SHA256:** `59b1afd34467a10ca4744cdbd28d5ab70fb2c4892285e42e84c309bb00146b66`.

### DF16

[prompts/05-delivery-and-measurement.md](https://github.com/Double-FW/Executive-and-Organisational-Commitments/blob/5e296922234a50a0c2fa4b6cc187a8745ca55d73/prompts/05-delivery-and-measurement.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob 313e8389852e60a8231590a2f83061f4293c2895.

**Relevant units:** Complete short prompt: owned delivery records and distinct activity/output/outcome/impact measures.

**Retained text SHA256:** `35da66c08824d2750a03622561949cadef05f6b1f8a1c717805e9d06ea60d617`.

### DF17

[prompts/06-assurance.md](https://github.com/Double-FW/Executive-and-Organisational-Commitments/blob/5e296922234a50a0c2fa4b6cc187a8745ca55d73/prompts/06-assurance.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob 25fdb6444728a5ace870076b2389ba07c74bcd41.

**Relevant units:** Complete short prompt: unsupported claims, evidence, permissions and human approval.

**Retained text SHA256:** `34946d6edc94a6e5727778c08d9138c66b8fcc342fbc4dac1f053bcd6fef1a8c`.

### DF18

[prompts/07-review-and-renewal.md](https://github.com/Double-FW/Executive-and-Organisational-Commitments/blob/5e296922234a50a0c2fa4b6cc187a8745ca55d73/prompts/07-review-and-renewal.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob ab4fec8db436e8abf41f58b622b23eaf6e3e6c6f.

**Relevant units:** Complete short prompt: progress, changed context, renewal and controlled claims.

**Retained text SHA256:** `450481cec8ea1a1a8ea356c952b69a7e9cdfc3ec0a4c9794e9823f653ae1039a`.

### DF19

[Cognitive Design Principles.md](https://github.com/Double-FW/Cognitive-UX-Design/blob/a6d0f2751bdc67a19e7d3f9c9645a7a93303a6e4/Cognitive%20Design%20Principles.md)

**Access:** pinned file retrieved successfully. **Version:** Git blob f7fc0c941eee8d28741b009db9d8082e07f092e1.

**Relevant units:** Sections 4–10: communication, redundancies, patterns, recall, feedback and choice.

**Retained text SHA256:** `d9926528af5188136d4ef925a1ceb9d8038833a03ccc8c11d012daca71ec31f3`.

## 6. Review results and remaining dependencies

The matrix contains **45 mapping rows**: 13 registered requirement routes, 26 delivery/viewer controls and 6 agent/validation controls. Fit distribution: 14 partial, 3 gap, 5 contextual, 23 direct practice. These counts describe mappings, not percentages of AVMSD legal coverage.

Nineteen Double-FW documents were considered: 13 pinned files retrieved successfully and six retained snapshots with current access gaps. The accessible Cognitive-UX-Design copy was selected for DF19 rather than retaining the unavailable shared-design link. DF08 supplies supporting ownership/lifecycle context; current DF03/DF09/DF11/DF12 guidance provides accessible governance routes without relying solely on that unavailable file.

The main unresolved dependencies are national/service applicability and reporting instructions; specialist European-works, broadcast remedies, commercial-content and platform assessments; destination-specific technical methods; a verified GitHub location for the detailed AD package; and access/authority confirmation for the six snapshot sources. General guidance should not be added merely to conceal these gaps.

Checks performed: target requirement IDs and guide/workflow IDs reconciled against the local repository; all source references resolved to this catalogue; all 13 active pinned file links fetched successfully; all six access failures recorded; all outbound links restricted to `github.com/Double-FW/`; no third-party links or bibliographies included. Named source units were reviewed for the stated mapping purposes. This is not an exhaustive review of every Double-FW repository or every linked file, and the mapping has not received independent human approval.
