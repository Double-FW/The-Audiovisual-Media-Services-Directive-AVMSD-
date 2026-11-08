# AVMSD weekly updates to Hugging Face

This package is for **Double-FW/The-Audiovisual-Media-Services-Directive-AVMSD-**. You do not need to download or upload the source repository folder to ChatGPT. Its public GitHub URL is sufficient.

The automation uses your existing AVMSD dataset. Its name was not supplied when this package was prepared, so it is deliberately configured through one GitHub repository variable. No dataset name has been guessed, and no live publication has been attempted.

## 1 Upload the three visible folders to GitHub

1. Unzip `AVMSD_Weekly_Update_Setup.zip` on your computer.
2. Open `AVMSD_Weekly_Update_Setup`, then `UPLOAD_TO_GITHUB`.
3. Open https://github.com/Double-FW/The-Audiovisual-Media-Services-Directive-AVMSD- in your browser. Use this AVMSD repository, not Accessible-Chatbots.
4. Choose **Add file → Upload files**.
5. Drag the three folders **huggingface**, **scripts** and **tests** from `UPLOAD_TO_GITHUB` into the upload area. Do not drag the ZIP, the outer folder or the `UPLOAD_TO_GITHUB` folder itself.
6. Enter `Add AVMSD weekly dataset updates` as the commit message and save to **main**. If a pull request is required, create and merge it before continuing.

The scripts read committed documentation from the repository. They do not download or execute instructions from linked sources. Only the approved file paths in `huggingface/export-config.json` are exported. Future files need adding to that list after review.

## 2 Create the workflow directly in GitHub

The package avoids hidden-folder uploads because GitHub rejected `.github` with “This file is hidden” in the earlier setup.

1. In the AVMSD repository, choose **Add file → Create new file**.
2. In **Name your file**, enter exactly `.github/workflows/huggingface-sync.yml`.
3. Open the visible `WORKFLOW_TO_COPY.txt` file from this download. On a Mac, if opening it launches an unfamiliar editor, right-click and choose **Open With → TextEdit**. Its contents are plain text.
4. Copy the entire contents of that file into GitHub's large editor box. There are no Markdown code fences to remove. Do not add quotation marks, change indentation or paste your token into this file.
5. Choose **Commit changes**, enter `Add AVMSD update workflow`, and save/merge to **main**.
6. Open **Actions** and look for **Update AVMSD Hugging Face dataset**. Enable GitHub Actions for this repository if prompted.

## 3 Set the destination dataset name once

This is an ordinary **variable**, not a secret. It is a name such as `GarethFW/the-name-you-actually-created`, not the token and not a full URL.

1. Open the existing AVMSD dataset on Hugging Face and look at the address bar.
2. Copy only the owner and dataset-name part after `https://huggingface.co/datasets/`. For example, if the URL were `https://huggingface.co/datasets/GarethFW/avmsd`, the value would be `GarethFW/avmsd`. This is an example, not a claim about your actual dataset name.
3. In the AVMSD GitHub repository, choose **Settings → Secrets and variables → Actions → Variables**.
4. Click **New repository variable**.
5. Set **Name** to `HF_DATASET_ID` and **Value** to the actual owner/dataset name you copied.
6. Click **Add variable**.

Direct link: https://github.com/Double-FW/The-Audiovisual-Media-Services-Directive-AVMSD-/settings/variables/actions

The package accepts a destination owned by **GarethFW** and explicitly rejects `GarethFW/accessible-chatbots`. It stops rather than guessing if the variable is missing. A destination owned by a company organisation needs a reviewed `destination_owner` configuration change.

## 4 Give this repository access to the AVMSD dataset

The chatbot repository's `HF_TOKEN` secret does not automatically exist in the AVMSD repository. Create a separate token for this connection if possible.

1. Open https://huggingface.co/settings/tokens and select **Create new token** or **New token**.
2. Choose **Fine-grained** if a token type is shown, name it `GitHub AVMSD weekly sync`, and choose **Custom** under **Presets**.
3. In the separate **Repositories permissions** section, select only the actual AVMSD dataset.
4. Enable **Read contents of selected repos** and **Write contents/settings of selected repos**. Leave broad **User permissions** and **Org permissions** unchecked.
5. If Hugging Face automatically selects **View access requests for selected gated repos** together with write access and will not let you deselect it, leave that linked permission selected. Confirm the selected resource is still only the AVMSD dataset. This publisher does not use access-request management.
6. Create and copy the token. Do not paste it into ChatGPT, files, messages or screenshots.
7. Open https://github.com/Double-FW/The-Audiovisual-Media-Services-Directive-AVMSD-/settings/secrets/actions
8. Choose **New repository secret**. Enter `HF_TOKEN` in **Name**, paste the token into **Secret**, and choose **Add secret**.
9. Check that `HF_TOKEN` is listed under **Repository secrets**. Its value is intentionally hidden and cannot be revealed again in GitHub.

## 5 Run the first update manually

1. Open https://github.com/Double-FW/The-Audiovisual-Media-Services-Directive-AVMSD-/actions/workflows/huggingface-sync.yml
2. Select **Run workflow**, leave the branch as **main**, then click the green **Run workflow** button.
3. Refresh if needed, open the new run, then open its **publish** job.
4. Confirm the tests, export and **Publish AVMSD dataset** steps all finish successfully. The final message should say that files were updated or the dataset was already up to date.
5. Check the Hugging Face dataset's **Files and versions** history and main dataset card. Share the run URL if you need help interpreting a failure. Never share the token.

Monday updates are configured for **07:23 UTC**: 07:23 UK winter time or 08:23 UK summer time. GitHub can delay runs and may disable a public-repository schedule after 60 days without repository activity. Check the Actions page periodically and configure GitHub notifications for failures. No separate missed-run monitoring service is included.

## What the export contains

- **knowledge_chunks**: complete second-level Markdown sections from the nine approved AVMSD guidance files, with their preambles and original metadata retained. It does not expect chatbot C00–C23 identifiers.
- **documents**: complete approved guidance, legal-status and source records, schemas, templates, workflow definitions and developer validation records. Draft status and uncertainty remain visible.
- **synthetic_examples**: the labelled fictional programme/service example and developer validation fixtures. These are separate from the guidance and are not real legal, viewer, approval or service evidence.

The generated dataset card and every record identify the original source. Required legal and governance context paths are retained. YAML and JSON supporting files remain complete records. Existing private or account-specific links in public documents are retained as references but never followed or ingested. No legal-source freshness review, conformance assessment, model training or independent content approval is performed by the update.

Eight destination files are managed: `README.md`, `LICENSE`, `documents.jsonl`, `knowledge_chunks.jsonl`, `synthetic_examples.jsonl`, `provenance.json`, `record_schema.json`, `validation_report.json`. The dataset card and licence at those exact paths will be replaced by the generated versions; other raw files you previously uploaded and `.gitattributes` are preserved. The explicit dataset configuration loads the generated JSONL files only. Existing unmanaged raw snapshots are not kept in sync: review and remove obsolete copies separately if appropriate.

The current source MIT licence is preserved. Changing licensing later requires coordinated source terms, metadata and checksum review. A weekly export does not refresh the source's legal review date or remove draft/blocked statuses.

## Changes and safeguards

Changed text is rebuilt into the latest complete snapshot. Removed optional source documents disappear from the snapshot; newly added files require approval. Missing required guides or context documents, changed licence text, invalid YAML/JSON, inconsistent document-index paths, wrong repository/destination and export tampering stop publishing. All eight managed file changes are committed together against the destination revision that was read; concurrent edits cause a failure rather than a blind overwrite. No-change runs skip committing.

`validation_report.json` records added, changed and removed record IDs compared with the previous export when available. Old dataset revisions, copied material, downloads and model knowledge are not recalled when a source file is removed.

## Troubleshooting and pausing

- **Missing HF_DATASET_ID**: use the Variables tab, not Secrets; enter the owner/dataset name without the full URL.
- **Missing or denied HF_TOKEN**: check the AVMSD repository's Secrets tab and the token's permissions for the AVMSD destination, not the chatbot dataset.
- **Wrong source or destination provenance**: check the dataset name. The publisher refuses a destination already marked as coming from an unrelated source.
- **Skipped job**: choose main in the original AVMSD repository; the workflow deliberately does not publish from forks or other branches.
- **Run workflow button missing**: verify the exact workflow path and that the file has been saved/merged into main; enable Actions if required.
- **Specific data preview error**: copy the exact error for investigation. A temporary busy/processing message may resolve later.
- **Stop scheduled updates**: Actions → Update AVMSD Hugging Face dataset → workflow menu → Disable workflow. To revoke access as well, delete the GitHub secret and revoke the token in Hugging Face settings.

## Local verification for technical review

From the AVMSD repository root:

```sh
python -m pip install -r huggingface/requirements.txt
python -m unittest discover -s tests -p 'test_avmsd_huggingface.py' -v
python scripts/export_huggingface.py --output /tmp/avmsd-dataset
```

The tests use a fake remote destination. They do not publish or require your token. The first real GitHub run is still required to test authentication and live publication. The source's own `validation/check_repository.py` is not executed by this exporter; export tests do not replace its operational checks or independent legal review.
