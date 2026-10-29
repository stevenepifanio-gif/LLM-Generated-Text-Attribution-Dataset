# GenAttr-CD: Multi-domain Generated-text Attribution — Metadata Release

**This folder is an upload-ready METADATA-ONLY package. It does not contain the original input texts or any generated rewrite texts.** It represents the exact 15,270 generated records used in the thesis. Text redistribution has not been cleared; see [LICENSE_NOTICE.md](LICENSE_NOTICE.md). Do not describe this package as an openly released full-text benchmark.

## Task and scale

The underlying task is attribution among five known text generators, not human-versus-AI detection. Each original input has one rewrite from each generator. There are 3,054 original input groups and 15,270 generated outputs.

| Domain | Original inputs | Generated outputs | Train inputs / outputs | Valid inputs / outputs | Test inputs / outputs |
|---|---:|---:|---:|---:|---:|
| Yelp | 2,000 | 10,000 | 1,400 /7,000 | 200 /1,000 | 400 /2,000 |
| Arxiv | 350 | 1,750 | 245 /1,225 | 35 /175 | 70 /350 |
| News | 704 | 3,520 | 492 /2,460 | 70 /350 | 142 /710 |

The five exact machine labels are Qwen2-7B-Instruct, gemma-2-9b-it, deepseek-llm-7b-chat, Meta-Llama-3-8B-Instruct and Mistral-7B-Instruct-v0.2. Each contributes 3,054 outputs. Integer labels 0–4 follow that order; see `metadata/source_models.json`.

## Original-input-level split

The existing frozen split is preserved without resampling. All five rewrites of the same input remain in the same split. Within each domain, original input IDs and exact input hashes are disjoint across train/valid/test. The historical split sorts exact input strings, uses random_state 42 to reserve 30%, then divides that remainder into validation/test with test_size 2/3. Published memberships, not a fresh split, are authoritative. These are project splits, not upstream dataset splits.

Formal source training uses Yelp-train only and model selection uses Yelp-valid only. Yelp-test is in-domain; Arxiv-test and News-test are cross-domain. Existing Arxiv/News train and valid partitions are archived but were not used for formal source training/selection. Original article/document IDs were not completely preserved, so exact-input separation is not a proof of document-level separation.

## Historical generation conditions

Three original instructions were sampled independently for each rewrite:

1. `Revise this with your best effort`
2. `Help me polish this`
3. `Concise this for me and keep all the information`

The exact template is `"{instruction}:\n\n{input_text}\n\nOutput:"` (real newline characters; no trailing newline after the colon). No chat template was applied. All five models used sampling, temperature 0.7, top_p 0.9, max_new_tokens 256, tokenizer truncation at 2048 input tokens, and seed 42. Historical inference used FP16. Only newly generated tokens were decoded. Identical original input does not imply identical sampled instruction across the five models.

There are 15,266 `offline_regeneration` records and four historical Gemma/Arxiv `offline_regeneration_repair` records (train 2, valid 1, test 1). These exceptions are retained. `prompt_split` is a historical generation field, not the final split. Complete historical generator weight/tokenizer revisions and weight hashes are unavailable; these settings are not a byte-identical regeneration guarantee. No new generation was performed for this release.


## Scope and limitations

The rewrites are not guaranteed faithful or factually correct. Model attribution may reflect content, length, prompt and task-compliance artifacts as well as style. No per-record manual rewrite-quality certification is claimed. The data do not establish open-world detection of arbitrary unseen generators. No checkpoint, training prediction, secret, machine configuration or private source text is included here. There is no automatic publication or remote repository associated with this preparation.

See [DATASET_CARD.md](DATASET_CARD.md), [LICENSE_NOTICE.md](LICENSE_NOTICE.md), [UPLOAD_GUIDE.md](UPLOAD_GUIDE.md) and [FILE_LIST.txt](FILE_LIST.txt).
