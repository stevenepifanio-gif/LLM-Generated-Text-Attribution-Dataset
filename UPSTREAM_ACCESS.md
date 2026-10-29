# Upstream access and reconstruction limitations

The public metadata is enough to verify counts and split membership, not enough to recover text or regenerate the historical outputs exactly.

## Authorized local manifests

If you already lawfully hold the nine exact frozen `*_records.json` files, run `scripts/rebuild_private.py` as documented in README. All hashes must match `metadata/formal_manifest_hashes.json`. Output must be a new private folder outside both this release and the source tree. Do not drag that reconstructed folder into GitHub. Reconstruction is not redistribution clearance.

## Upstream access routes

- Yelp: consult the [dataset agreement](https://s3-media0.fl.yelpcdn.com/assets/srv0/engineering_pages/f64cb2d3efcc/assets/vendor/Dataset_User_Agreement.pdf) and the [Yelp review-full card](https://huggingface.co/datasets/Yelp/yelp_review_full). The historical downloader selected the first 2,000 nonempty train texts and collapsed whitespace. The original revision and row identifiers were not retained. Do not assume a present download recreates the same order; check the published exact-input hashes locally.
- Arxiv: [ccdv/arxiv-summarization](https://huggingface.co/datasets/ccdv/arxiv-summarization) supplied the first 350 nonempty train abstracts after whitespace collapsing. Current document/section configurations and row order need not match the unarchived historical revision/configuration. Recover paper/version IDs, examine the applicable [arXiv license](https://info.arxiv.org/help/license/index.html), and establish whether the exact abstract corresponds to separately licensed metadata before distributing anything. No automatic scraping or bulk download is supplied.
- News: [RAIDAR](https://github.com/cvlab-columbia/RaidarLLMDetect) provides the documented lineage; the recorded upstream file is `News/Human.json`. Its historical SHA-256 is in `metadata/upstream_provenance.json`. Frozen evidence reports 730 rows and 704 first-occurrence unique inputs after whitespace normalization, with exact order matching. Confirm applicable permissions before obtaining or using copies. The [UCI entry](https://archive.ics.uci.edu/dataset/217/reuter+50+50) and [NIST agreements](https://trec.nist.gov/data/reuters/reuters.html) require reconciliation for public redistribution; this package does not automatically download or redistribute the news stories.

Re-obtaining original inputs is not a reconstruction of generated rewrites. Missing historical generator weight revisions, stochastic generation, continuation/error behavior and four repair records prevent an exact-output guarantee from seed 42 alone. This release neither runs generation nor presents substitute newly generated examples as the thesis data.
