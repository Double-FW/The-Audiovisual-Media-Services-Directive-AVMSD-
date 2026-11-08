---
document_id: AV-MAP-01
version: 0.2.0
status: draft_for_review
authority_type: guidance_dependency_mapping
review_date: 2026-11-08
target_repository_version: 0.1.0
suggested_repository_path: control/double-fw-guidance-matrix.md
source_boundary: publicly available Double-FW repository files only
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

Only files in repositories confirmed as public on **8 November 2026** are mapped. Each retained pinned file was retrieved successfully on that date. Private sources and their retained snapshots, hashes and source-specific locators have been removed. Where public guidance supports only part of a control, the mapping is narrowed or marked Partial; where it supplies no suitable method, the row remains a Gap. Source identifiers retain their original numbers so existing references to retained sources remain stable; numbering gaps are intentional.

## 1. Registered requirement routes

Requirement IDs below are unchanged from `control/requirement-register.yaml`. The register's unresolved applicability and specialist blocks remain in force.

| Requirement ID | Repository route | Requirement / duty area | Double-FW guidance and locator | Fit | Use and boundary | Required output/evidence |
| --- | --- | --- | --- | --- | --- | --- |
| A7-1 | AV-G02; WF03/WF08 | Continuous, progressive accessibility through proportionate measures | [DF03](#df03): ATLF-10, ATLF-18; [DF16](#df16): delivery and measurement | Partial | Connect baselines, resources, owned actions and measured change using the public delivery and testing guidance. These methods do not determine national proportionality, quotas or legal sufficiency. | action_plan, coverage, improvement, conclusion |
| A7-2P | AV-G06; WF09 | Regular provider reporting | [DF11](#df11): section 7; [DF12](#df12): section 9; [DF16](#df16): delivery and measurement | Partial | Prepare evidence-led reports with named owners and approval. Provider reporting format, deadline, recipient and actual receipt remain service-specific. | report, approval, submission |
| A7-2M | AV-G06; WF09 | Member State reporting to the Commission | — | Gap | No reviewed Double-FW source establishes this public-authority reporting route. Do not substitute an internal executive report or transfer its timetable to a provider. | requirement with separate duty holder; unresolved dependency |
| A7-3 | AV-G02/AV-G06; WF03/WF09 | Accessibility action plans and communication | [DF16](#df16): delivery and measurement; [DF11](#df11): sections 5, 7; [DF18](#df18): review and renewal | Partial | Build owned, resourced and reviewable plans. These sources do not establish whether a national plan is mandatory or prove communication to the regulator. | action_plan, improvement, approval, submission |
| A7-4 | AV-G06; WF11 | Accessible national information and complaints contact point | [DF15](#df15): Assessment protocol and Manual keyboard checks | Partial | Support technical accessibility and keyboard checks on a contact journey. DF15 does not designate the actual national contact point or supply a complete complaints-service usability method; provider support is a separate route. | jurisdiction, delivery/quality, complaint |
| A7-5 | AV-G06; WF10 | Accessible emergency information | [DF01](#df01): sections 1, 3–4, 7–9; [DF02](#df02): section 10 | Partial | Plan multimodal messages, live preparation and tested delivery. National emergency authority, exact rapid-response procedure and legal treatment remain unresolved; no blanket delay rule is created. | emergency, evidence, issue |
| OTHER-MINORS | AV-G07; WF03 | Audience/minors protection and related data safeguards | [DF07](#df07): Data Collection Principles and AI Training and Accessibility Data; [DF02](#df02): section 11 | Contextual | Supports minimisation and age-sensitive caption design. Does not supply a complete harmful-content, age-assurance, safeguarding or children’s-data legal assessment. | requirement, specialist issue, protected evidence |
| OTHER-COMMERCIAL | AV-G07; WF03 | Commercial communications, sponsorship, placement and linear advertising rules | [DF14](#df14): The Brand Connection | Contextual | Supports an inclusive brand-experience lens. Does not provide a specialist marketing-accessibility method or assess advertising-time calculations, prohibited categories, sponsorship independence or placement permissions. | specialist requirement/assessment gap |
| OTHER-WORKS | AV-G07; WF03 | European works, prominence and relevant contribution routes | — | Gap | No reviewed specialist Double-FW method establishes work classification, catalogue share, prominence or financial-contribution calculations. Accessibility percentages are unrelated measures. | specialist requirement/assessment gap |
| OTHER-VSP | AV-G01/AV-G07; WF02/WF03 | Platform jurisdiction and protective/commercial measures | [DF12](#df12): section 10; [DF07](#df07): data-governance principles | Contextual | Supports dependency ownership and data controls. Does not establish VSP classification, jurisdiction, appropriate moderation measures, redress or a universal Article 7 duty for uploads. | classification, jurisdiction, specialist requirement gap |
| OTHER-INTEGRITY | AV-G07; WF03 | Provider information, prominence and programme integrity | [DF01](#df01): section 9; [DF02](#df02): section 13 | Partial | Supports access-feature metadata, caption-track labels, control and viewer choice. Does not settle provider disclosure, general-interest prominence or legal permission for overlays/modifications; specialist connected-TV and general interactive-media methods are not mapped here. | route, quality, specialist requirement gap |
| OTHER-REMEDIES | AV-G07; WF03 | Major events, short extracts and reply/remedies | — | Gap | No reviewed Double-FW specialist guidance supports these broadcast-law determinations. Accessible complaints practice cannot establish rights to extracts, events or statutory reply. | specialist requirement/assessment gap |
| OTHER-COOPERATION | AV-G07; WF03/WF12 | Regulatory cooperation, institutions and media-literacy duties | [DF11](#df11): section 8; [DF12](#df12): section 11 | Contextual | Supports internal review, governance reporting and escalation. Does not establish current regulator/Media Board powers, cooperation procedures or media-literacy reporting duties. | monitoring, source review, specialist requirement gap |

## 2. Delivery, assessment and viewer requirements

These are the practical requirements in the guides, including adopted-policy candidates and recommended practice. They are not all direct statutory instructions. Each row identifies the relevant guide section or workflow and the evidence it should produce.

| Repository locator | Requirement / control | Double-FW guidance and locator | Fit | Use and boundary | Required output/evidence |
| --- | --- | --- | --- | --- | --- |
| AV-G01: Build the jurisdiction adapter; WF01/WF02 | Record scope, authority, versions and unresolved interpretation | [DF11](#df11): sections 2–3; [DF12](#df12): D01–D02 in section 10 | Direct practice | Reuse source/applicability register discipline and legal-owner escalation. Service classification and actual national rules still require their own assessment. | jurisdiction, classification, source |
| AV-G02: Plan measurable improvement; WF03 | Turn commitments into funded delivery actions | [DF16](#df16): complete prompt; [DF11](#df11): sections 3, 5, 7 | Direct practice | Carry authority → outcome → activity → owner → evidence → review. Do not turn draft targets or unfunded promises into established provision. | action_plan, target, monitoring |
| AV-G02: Plan measurable improvement; WF08 | Feature-specific numerator, denominator and eligible population | [DF03](#df03): ATLF-11, ATLF-18; [DF11](#df11): Measures must explain what they mean | Partial | Use explicit coverage dimensions, denominator and measure definitions. Programme-duration, repeats, overlapping intervals and qualifying-feature algorithms remain AVMSD repository-specific controls. | target, coverage, evidence |
| AV-G02: Interpret five separate findings; WF08 | Separate provision, quality, viewer outcomes and progress | [DF03](#df03): ATLF-14; [DF11](#df11): section 7; [DF16](#df16): delivery and measurement; [DF18](#df18): review and renewal | Partial | Keep testing, delivered provision, reported experience and progress evidence distinct. These sources support reporting discipline but do not define the AVMSD five-finding model or its viewer-outcome taxonomy. Progress and QA statuses require explicit adapters to the AVMSD record vocabularies. | coverage, quality, viewer, improvement, conclusion |
| AV-G03: Define acceptance before creation or purchase; WF04 | Plan accessibility before production and purchase | [DF01](#df01): Scope and limits; section 7; [DF03](#df03): ATLF-10 Procurement activities | Direct practice | Define audience, feature, language, destination, budget, acceptance and supplier correction before commitment. | programme, feature, supplier, acceptance |
| AV-G03: Define acceptance before creation or purchase; WF04 | Check acquired assets, rights and alternate versions | [DF01](#df01): Scope and limits; sections 7, 9; [DF02](#df02): sections 3, 12 | Partial | Specify and verify deliverables, version identity and redelivery. These sources do not grant rights or replace title/territory/language-specific contract scrutiny. | rights, supplier, acceptance |
| AV-G03: Plan meaning through sound and picture; WF05 | Integrated information and audio-description editorial treatment | [DF01](#df01): sections 2–3, 5, 10 | Partial | Support early descriptive planning, important graphics in sound, intelligibility and genre-appropriate AD. This mapping does not establish a detailed radio/podcast commentary or specialist AD editorial method beyond the cited public production guide. | editorial, feature, quality |
| AV-G03/AV-G04; WF05/WF06 | Captions/SDH preserve dialogue, speakers and meaningful sound | [DF02](#df02): sections 1, 4, 7–8, 14; [DF01](#df01): section 1 | Direct practice | Apply editorial fidelity and distinct track roles. Translation subtitles and automatic speech recognition are not automatically assessed SDH. | feature, quality, evidence |
| AV-G03/AV-G04; WF05/WF06 | Readable, synchronised captions without obscuring information | [DF02](#df02): sections 5–6, 9, 14 | Direct practice | Review linguistic grouping, cue timing, reveal order, placement and rendering. Numeric source defaults need a justified language/platform profile; they are not EU-wide thresholds. | quality, route, evidence |
| AV-G03/AV-G04; WF05/WF06 | Target-language signing and spoken-subtitle coordination | [DF01](#df01): section 4; [DF02](#df02): section 1 Related services | Partial | Signing is a language service with framing and Deaf-user QA; feature types are distinct. Detailed spoken-subtitle production and collision methods are not established by these sources. | feature, editorial, specialist quality |
| AV-G04: Trace each delivery state; WF06 | Bind programme, cut, language, feature and transformation | [DF01](#df01): sections 7, 9; [DF02](#df02): sections 3, 12, 15 | Direct practice | Retain exact identifiers and references through authoring, conversion, packaging and playback. AVMSD schema field names and identity checks are local implementations. | programme, feature, route, evidence |
| AV-G04: Trace each delivery state; WF06 | Distinguish file presence from delivered usable access | [DF01](#df01): sections 8–9; [DF02](#df02): sections 12–14 | Direct practice | Validate syntax and actual rendition, synchronisation and feature selection. A master, upload receipt or valid file cannot establish viewer access alone. | delivery, quality, issue |
| AV-G04: Trace each delivery state; WF06 | Discover, select and retain features during real viewing | [DF02](#df02): section 13 | Partial | DF02 directly supports caption discovery, accurate labels, accessible controls, synchronisation and preference retention. Equivalent controls for other access services and advert/episode/device handoffs require separate specification and executed evaluation; a caption method does not establish complete player coverage. | route, delivery, viewer |
| AV-G04: Assess distinct features; WF06 | Cognitive clarity and flexible media control | [DF19](#df19): sections 4–10 | Direct practice | Use clear messages, recognisable choices, feedback and user control from the public cognitive-design guidance. Adapt these general principles to the actual player; they do not provide a specialist interactive-media acceptance method or mandate every output mode for every interface. | feature specification, route, viewer |
| AV-G04: Execute and preserve observations; WF06 | Combine partial automated, manual, keyboard and specialist methods | [DF03](#df03): ATLF-09, ATLF-11–12; [DF15](#df15): Assessment protocol; Manual keyboard checks | Direct practice | Use actual interaction and retain engine/profile versions. A clean scan cannot establish caption meaning, signing quality, AD adequacy, full playback or complete legal compliance. | quality, delivery, evidence |
| AV-G04: Outputs and next workflow; WF06 | Photosensitivity, live quality and destination-specific methods | [DF01](#df01): section 6 and Claims requiring current verification; [DF02](#df02): sections 10, 12 | Partial | Sources identify preparation, risk and the need for a current specialist method/profile. They do not provide every instrument, limit or validated integration. | quality with explicit blocked methods |
| AV-G05: Recruit beyond current successful viewers; WF07 | Include disabled people early and evaluate assembled delivery | [DF01](#df01): section 8; [DF03](#df03): ATLF-09; [DF07](#df07): Customers Versus Research Participants | Direct practice | Include relevant language/access approaches, disabled viewers and people excluded from the journey. Use actual assembled-delivery evaluation and defined human decision rights; research participation does not transfer compliance accountability to participants. | viewer plan, permissions, evidence |
| AV-G05: Select outcomes without rewriting their IDs; WF07 | Resolve a publicly documented viewer-outcome taxonomy | — | Gap | No retained public source in this review defines the outcome taxonomy previously cited for this control. Do not reconstruct its identifiers, definitions or status rules from a private copy. Treat dependent outcome selection as unresolved until a suitable public canonical source is reviewed; retain existing AVMSD records without silently renaming their fields or values. | viewer taxonomy dependency, affected record references and limitations |
| AV-G05: Define and validate measures; WF07 | Separate observed comprehension, reported experience and uncertainty | [DF11](#df11): section 7; [DF03](#df03): ATLF-09, ATLF-14 | Partial | Define the task, scope, denominator, collection method, study context, assistance and uncertainty. Keep observed results and reported experience distinct. The public guidance does not provide the removed outcome model or a complete validated comprehension instrument; analysis and export validation require local evidence. | viewer, evidence, instrument contract |
| AV-G05: Protect evidence and interpret carefully; WF07 | Minimise data and keep synthetic/participant evidence separate | [DF07](#df07): Data Collection Principles; Customers Versus Research Participants; AI Training and Accessibility Data | Partial | Respect purpose, consent, minimisation, access and training-use limits. The public data-ethics guide does not define a synthetic-evidence taxonomy: keep simulated outputs visibly separate from participant observations as an AVMSD implementation control. The guidance does not itself establish a lawful basis or commercial reuse permission. | evidence, viewer, delegation |
| AV-G05: Outcomes; WF07 | Explore dignity, confidence, enjoyment and brand experience | [DF07](#df07): Core Ethical Principles; [DF14](#df14): emotional brand framing | Contextual | Use dignity, autonomy and emotional brand experience as research lenses, with locally defined questions and measures. These sources do not define the removed outcome IDs or a validated enjoyment scale. Feeling Valued is not a fifth official POUR principle; brand claims or a WCAG pass do not prove viewer experience. | viewer, research questions, bounded interpretation |
| AV-G06: Prepare and approve reports; WF09 | Prepare reconstructable reports and exact-version approvals | [DF11](#df11): section 7; [DF12](#df12): section 9; [DF17](#df17): assurance prompt | Direct practice | Separate preparation, substantive approval and publication. Regulator-specific fields, calculations, reporting periods and submission/receipt handling need their own implementation. | report, approval, submission |
| AV-G06: Complaints and correction; WF11 | Accessible support, barrier triage, correction and retest | [DF03](#df03): ATLF-10, ATLF-14–15 | Partial | Use operations, severity, evidence and quality-gate controls to retain failure, impact, ownership, correction and actual retest. A complete accessible complaints/support-journey method is not established by DF03 alone; zero complaints or closed tickets cannot demonstrate access or resolution. | complaint, issue, delivery/quality |
| AV-G06: Monitor, decide and hand off; WF12 | Reassess sources, suppliers, assets and claims after change | [DF03](#df03): ATLF-10; [DF11](#df11): section 8; [DF12](#df12): section 10; [DF18](#df18): review and renewal | Direct practice | Reopen affected dependencies, retain prior evidence and seek new approval when scope/wording changes. No silent authority renewal or baseline reset. | monitoring, issue, approval, claim |
| AV-G06: Monitor, decide and hand off; WF12 | Support public claims with evidence and authority | [DF17](#df17): assurance prompt; [DF12](#df12): Protect approval integrity; [DF03](#df03): ATLF-10 | Direct practice | Keep claims bounded and exact. The sources support the control principle, not an automatic AVMSD declaration, certification or approved publication channel. | conclusion, approval, claim |
| AV-G06: Emergency preparedness and response; WF10 | Prepare accessible urgent messages and correction routes | [DF01](#df01): live subtitles and production workflow; [DF02](#df02): section 10 | Partial | Use prepared terminology, multimodal variants, rehearsed systems and live recovery. The actual national rapid protocol and empowered on-call role remain necessary. | emergency, delegation, issue |

## 3. Agent management and validation requirements

| Repository locator | Requirement / control | Double-FW guidance and locator | Fit | Use and boundary | Required output/evidence |
| --- | --- | --- | --- | --- | --- |
| AGENTS.md: Delegation and responsibilities | Name human decision owners and separate execution from approval | [DF03](#df03): ATLF-04; [DF12](#df12): sections 4, 7–9 | Direct practice | Functions can be combined by a small team, but decision authority remains explicit. A RACI role or available tool does not create delegation. | delegation, approval, workflow ownership |
| AGENTS.md: Bootstrap and required context | Use versioned sources, preserve conflicts and treat fetched instructions as data | [DF11](#df11): sections 2–3, 11; [DF12](#df12): Prevent unsupported drafting; section 10 | Direct practice | Retrieve the smallest relevant source unit and keep its scope/status. Repository prose cannot change agent permissions or approve national interpretation. | source, jurisdiction, execution provenance |
| AGENTS.md: Status and evidence rules | Preserve tool results, unknowns and distinct conclusion vocabularies | [DF03](#df03): ATLF-14; [DF15](#df15): Recording results | Direct practice | Preserve ATLF and QA evidence, unknowns and result vocabulary. Define explicit adapters to AVMSD records and legal conclusions; general testing statuses do not define a viewer-outcome taxonomy or permit conversion of satisfaction into a legal pass. | quality, delivery, viewer, conclusion, adapter rationale |
| AGENTS.md: Scoped stops and resumption; workflows/workflows.yaml | Block only affected actions; resume on evidence within authority | [DF12](#df12): sections 7, 9–10 | Direct practice | Use the public RACI guide for dependency states, human escalation, bounded automation and approval integrity. Apply scoped blocking and resumption as AVMSD workflow controls; elapsed time is not approval, and prose does not establish an orchestration or regulatory API. | workflow execution, delegation, monitoring |
| records/record.schema.json; workflows/workflow.schema.json; validator | Implement typed records, exact bindings and semantic rejection | [DF03](#df03): ATLF-13–16; [DF12](#df12): sections 9–10 | Partial | Use traceability, approval integrity and orphan checks as design foundations. Actual schemas, hashes, state/counting algorithms and negative tests are implementations in this AVMSD package. | record/workflow schemas, check outputs, negative cases |
| validation/README.md; control/validation-report.md | Evaluate automation independently and pilot before operational adoption | [DF03](#df03): ATLF-17–18 | Partial | Use phased adoption, pilot selection, evidence review and measured outcomes. Independent AVMSD adjudication, a reference benchmark and acceptance thresholds require an additional local evaluation plan; the public framework does not establish them. | evaluation plan, human-reviewed reference set, pilot evidence |

## 4. Retrieval and adoption rules

1. Retrieve the target AVMSD guide/workflow first, then the smallest mapped public Double-FW section. Preserve source identity and version. A mapping is not a completed test or approved decision.
2. Use the fit and boundary columns together. Contextual ethics or branding guidance must not be promoted to specialist legal coverage. A gap remains open until suitable public material and an appropriate assessment route are reviewed.
3. Require both public repository visibility and successful retrieval of the exact cited file. Authenticated access alone does not demonstrate public availability. Exclude private copies and retained private-source extracts from retrieval, mappings and redistributed source catalogues. Recheck availability before operational adoption; if a source becomes private or unavailable, remove it from active retrieval and reassess affected mappings.
4. Keep each public source's vocabulary and baseline visible. DF15 uses axe-core 4.12.1. Do not merge engine profiles, numeric defaults or pass counts across sources. Choose and validate the actual assessment configuration separately.
5. Keep the viewer-outcome taxonomy dependency explicit. This public-source matrix supplies no replacement for the removed canonical outcome dataset. Do not invent identifiers or silently rewrite existing AVMSD record values. Progress labels and ATLF/QA results require explicit adapters to AVMSD vocabularies; no adapter turns satisfaction into legal conformity.
6. Treat the brand reframing as Double-FW interpretation. Its additional emotional framing is not an extra official POUR principle, and technical proof must not become proof of all experience outcomes.
7. Use DF01 for the AD content it supports. Detailed commentary/editorial methods beyond that guide remain a gap in this reviewed public source set. No separate non-public package is a mapping dependency.
8. Review source/model-use permissions before ingestion or redistribution. Public readability does not select a licence for the AVMSD repository or authorise use of participant evidence. Outbound links in a public source are not automatically approved dependencies; check their availability and scope separately before adding them.

## 5. Source catalogue

Each link identifies an exact file at a pinned commit in a Double-FW repository confirmed as public on 8 November 2026. All 12 linked files were retrieved successfully. Locators name sections rather than unverified fragment links. The pins preserve the versions used for this matrix; they do not assert that these are the latest editions. External bibliographies and linked private resources inside the source documents are outside this matrix's source boundary.

### DF01

[Accessible TV Content Guidance for Production Teams](https://github.com/Double-FW/Accessible-Film-TV-and-Video-Content-Production-Management/blob/40cf5488e46906807ae8764ff0a191f35a85cea9/Accessible_TV_Content_Guidance_for_Production_Teams.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026. **Version:** 1.1-semantic.

**Relevant units:** Sections 1–10; Scope and limits; Claims requiring current verification.

### DF02

[Closed Caption Subtitle Guidelines](https://github.com/Double-FW/Closed-Caption-Subtitles/blob/7ad0f5f1d8a31969f832985b63345ce4988ff1e6/Closed_Caption_Subtitle_Guidelines.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026. **Version:** 1.0.

**Relevant units:** Sections 1, 3–15; distinct services, authoring, live production, formats, player operation and acceptance.

### DF03

[Accessibility Test-Led Delivery Framework](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Accessibility_Test_Led_Delivery_Framework.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026. **Version:** 1.1.

**Relevant units:** ATLF-04; ATLF-09–18, especially decision rights, procurement, traceability, results and adoption.

### DF07

[Ethical and Inclusive Use of Data Relating to Disabled People.md](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/3db809cb035e53bc1825f884f3979fdc73f793a2/Ethical%20and%20Inclusive%20Use%20of%20Data%20Relating%20to%20Disabled%20People.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026.

**Relevant units:** Core Ethical Principles; Data Collection Principles; Customers Versus Research Participants; AI Training and Accessibility Data.

### DF11

[Accessibility_and_Inclusion_Policy_Creation_Guide.md](https://github.com/Double-FW/Inclusion-and-Accessibility-Policy/blob/145b4b2d2ae0680ca0d4c481dbbd077a31beb761/Accessibility_and_Inclusion_Policy_Creation_Guide.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026.

**Relevant units:** Sections 2–3, 5, 7–8 and 11: scope, authority, delivery, measures, source control and review.

### DF12

[Accessibility_and_Inclusion_Policy_RACI_and_Steering_Group_Guide.md](https://github.com/Double-FW/Inclusion-and-Accessibility-Policy/blob/145b4b2d2ae0680ca0d4c481dbbd077a31beb761/Accessibility_and_Inclusion_Policy_RACI_and_Steering_Group_Guide.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026.

**Relevant units:** Sections 4, 7–11: decision rights, bounded automation, approval integrity, dependencies and escalation.

### DF14

[The WCAG POUR principles reframed through emotional outcomes for branding systems.md](https://github.com/Double-FW/POUR-for-Branding-Systems-and-CX/blob/0e041d8aee75ba5585dd5c78af56f82ad9d626a8/The%20WCAG%20POUR%20principles%20reframed%20through%20emotional%20outcomes%20for%20branding%20systems.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026.

**Relevant units:** Feeling framing and The Brand Connection; interpretive brand practice only.

### DF15

[Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md](https://github.com/Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA/blob/f2ec12286e15233527196bb223260dd2846e53af/Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026.

**Relevant units:** Assessment protocol; Manual keyboard checks; Recording results; versioned rule profiles.

### DF16

[prompts/05-delivery-and-measurement.md](https://github.com/Double-FW/Executive-and-Organisational-Commitments/blob/5e296922234a50a0c2fa4b6cc187a8745ca55d73/prompts/05-delivery-and-measurement.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026.

**Relevant units:** Complete short prompt: owned delivery records and distinct activity/output/outcome/impact measures.

### DF17

[prompts/06-assurance.md](https://github.com/Double-FW/Executive-and-Organisational-Commitments/blob/5e296922234a50a0c2fa4b6cc187a8745ca55d73/prompts/06-assurance.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026.

**Relevant units:** Complete short prompt: unsupported claims, evidence, permissions and human approval.

### DF18

[prompts/07-review-and-renewal.md](https://github.com/Double-FW/Executive-and-Organisational-Commitments/blob/5e296922234a50a0c2fa4b6cc187a8745ca55d73/prompts/07-review-and-renewal.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026.

**Relevant units:** Complete short prompt: progress, changed context, renewal and controlled claims.

### DF19

[Cognitive Design Principles.md](https://github.com/Double-FW/Cognitive-UX-Design/blob/a6d0f2751bdc67a19e7d3f9c9645a7a93303a6e4/Cognitive%20Design%20Principles.md)

**Access:** repository confirmed public and pinned file retrieved successfully on 8 November 2026.

**Relevant units:** Sections 4–10: communication, redundancies, patterns, recall, feedback and choice.

## 6. Review results and remaining dependencies

The matrix retains **45 mapping rows**: 13 registered requirement routes, 26 delivery/viewer controls and 6 agent/validation controls. Fit distribution: 19 partial, 4 gap, 5 contextual and 17 direct practice. These counts describe mapping support, not percentages of AVMSD legal coverage.

The source catalogue now contains **12 publicly available files across nine Double-FW repositories**. Seven sources from four private repositories have been removed, including six previously marked as retained snapshots and one previously presented as a retrievable workflow guide. Their catalogue entries, hashes, citations and source-specific locators are excluded. Remaining source IDs are unchanged to preserve reference stability.

Where the removed material supplied the only canonical outcome definitions, that control is now a Gap. Other affected rows use public guidance only to the extent that its content supports them; several are narrowed to Partial. No replacement taxonomy, identifier scheme or specialist method has been invented. Existing AVMSD records and workflows may still need separate maintenance where they depend on the removed material; this companion document does not modify those files.

The main unresolved dependencies remain national/service applicability and reporting instructions; specialist European-works, broadcast remedies, commercial-content and platform assessments; destination-specific technical methods; detailed AD commentary/editorial methods beyond DF01; and a publicly documented viewer-outcome taxonomy. General guidance must not conceal these gaps.

Checks performed for this revision: repository visibility checked for every retained source; all 12 pinned file links retrieved successfully; affected mappings reconsidered against public guidance; private-source catalogue entries and references removed; all mapping references resolved to the retained catalogue; 45 mapping rows and fit totals checked; all outbound links restricted to `github.com/Double-FW/`. The requirement, guide and workflow identifiers are retained from the supplied matrix; this revision does not repeat the original reconciliation against the complete AVMSD repository, reassess national law, audit every Double-FW repository or independently approve the mapping.
