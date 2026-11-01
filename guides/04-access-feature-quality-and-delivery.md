---
document_id: AV-G04
version: 0.1.0
status: draft
authority_type: repository_guidance
review_date: '2026-11-01'
source_ids:
- D01
- D02
- D03
- D04
- D05
- X01
prerequisites:
- programme
- feature
- rights
output_record_types:
- route
- delivery
- quality
- evidence
- issue
---

# Access-feature quality and delivery

## Purpose and trigger
Verify that the correct access feature reaches viewers and works throughout the assessed journey. Trigger this guide for new assets, conversions, player/device changes, adverts, distribution migrations, complaints and retests. The accountable delivery owner coordinates QA, access-service specialists and product teams. Inputs are exact programme and track identities, rights, national/contractual quality conditions, format profiles, route/configuration matrix and versioned test methods.

## Assess distinct features
SDH/captions convey dialogue, speakers and meaningful non-speech audio. Review factual meaning, completeness, synchronisation, readable presentation and interaction with the picture. Translation subtitles can omit essential audio information; do not relabel them complete SDH without assessment. Sign languages are distinct natural languages; subtitles do not automatically provide equivalent access. Check target sign language, translation quality, visibility, framing, timing and obstruction with competent reviewers and intended language users.

AD communicates relevant visual information not adequately in sound. Assess cue accuracy, narrative knowledge, intelligibility, mix, protected dialogue/sound and timing, including humour and revelation. Spoken subtitles communicate displayed translation through speech; coordinate their timing with AD and dialogue. AD does not replace sound for someone who cannot hear. Identify which feature and audience each test concerns rather than using an undifferentiated accessible label.

D02 supplies caption editorial practice, not an EU statutory timing profile. Retrieve current service, language and platform specifications before adopting its recommendations. Syntax validation supports file conformance; it cannot judge whether a name is wrong, a sound omitted or a joke spoiled. Tools may assist cue inspection and error triage, but specialist review remains necessary for contextual quality.

## Trace each delivery state
Preserve independent states for the production master, supplied assets, packaged/transcoded output, transmitted route, player-presented track and viewer experience. Link each transformation to the exact input/output versions. Programme ID alone is insufficient: edition, episode, language, runtime, region, period and live/on-demand status matter. A track for a different cut is not a valid substitute even when it loads successfully.

Use the route matrix to identify actual app/build, device/firmware, region, network/delivery mode, media/track profiles and settings. Test availability labels, search/filtering, selection, activation and correct language. Check full sequences containing meaningful content as well as starts and endings. Exercise pause, seek, resumption, speed where supported, adverts, episode changes, casting and device handoff where claimed. Record what was actually tested and why the sample addresses the relevant risks; disclose untested routes.

## Execute and preserve observations
Before execution, verify reference assets, clock/frame-rate/timing assumptions, instrumentation and expected results. An invalid setup returns invalid assumptions; a tool error returns tool error. Neither is a pass or non-applicability. Preserve the tool's original status and vocabulary/version, then an explicit normalisation rationale. The record schema defines the normalised values; adapters cannot silently erase causes.

Store observations with timestamps/locators, method version, evaluator competence, environment, expected versus actual behaviour and protected evidence references. Record meaningful caption errors individually even where aggregate accuracy looks high. A clean interface scan cannot establish editorial accuracy or reliable track persistence. Use manual playback, assistive technologies and specialist methods where the questions require them.

## Interpret boundaries and correct failures
Separate AVMSD programme/service conclusions from EAA access-service and WAD website/app conclusions. The same keyboard or track-selection observation may support several assessments, but each needs its own applicability, exact legal/technical reference and limits. No automated result establishes universal AVMSD conformity.

When the master has AD and the player does not, retain master availability as present and delivery as failed. Diagnose packaging, metadata, distribution or control behaviour. Assign the correction owner, amend the exact affected configuration, retest the actual output and assess related routes for regression. Ticket closure is not evidence of restored access.

## Outputs and next workflow
Output route and delivery records, quality executions, evidence and linked issues/corrections. The delivery owner stops the affected readiness or provision claim for wrong assets, unresolved material defects, invalid tests or missing methods. Specialist photosensitivity, signing, live quality or format conformance requires a verified competent method; this repository does not implement those tools. Route correction to WF11, viewer evaluation to WF07 and qualifying provision evidence to WF08. Changes reopen affected checks through WF12, preserving earlier failures and their limitations.
