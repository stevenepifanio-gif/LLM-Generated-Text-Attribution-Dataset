# Dataset card

Release scope: metadata only, reviewed 2026-10-29. Language of the underlying inputs/outputs: English. The nine JSONL files represent 15,270 generated examples and 3,054 input groups. The represented texts are withheld, not missing accidentally and not replaced by empty strings.

Schema: `sample_id` uniquely joins domain/model/source line index; `original_input_id` joins all five outputs of an input; `domain` and `split` retain formal membership; `source_model` and `label` are the attribution targets; `prompt_id` indexes the exact shared instruction pool. `generation_type`, `prompt_split` and optional `repair_raw_index` retain historical generation provenance. `source_line_index`, `pool_index` and `formal_manifest_row` refer to project snapshots, not publisher IDs. `input_sha256` and `output_sha256` fingerprint exact stored UTF-8 strings without further normalization. Character counts use Python len, not tokenizer lengths. `text_release_status` always states that rights clearance is pending.

All grouped splits and hashes were checked against frozen source manifests. Counts, class completeness, group separation, repair exceptions and exact duplicate checks are in `metadata/verification_report.json`. No changes to the original experiment data were made. The package contains no source text examples, article titles, author fields, review-user fields or personal contact fields.

Yelp derives from Yelp review data; Arxiv stores derived abstracts from ccdv/arxiv-summarization; News has documented Reuters50-50 lineage via Ghostbuster/RAIDAR. News lineage is established more clearly than in older draft documentation, but its redistribution rights remain unresolved. See the upstream provenance and license review.

Use labels as targets only, not as features fed to an attribution model. Same-input rewrites and shared test inputs are dependent observations. Research splits are not official upstream splits, and absent article IDs prevent a document-level nonleakage guarantee. Metadata/hash release does not resolve all copyright, model-use, privacy or downstream-use questions. No claim of comprehensive manual semantic quality review is made.
