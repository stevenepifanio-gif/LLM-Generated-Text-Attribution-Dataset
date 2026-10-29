# License and redistribution review

Review date: 2026-10-29. Decision: release technical metadata and helper files only; withhold all 3,054 original inputs and 15,270 generated rewrites. Public availability or an open model weight license is not treated as permission to redistribute third-party prose.

| Domain | What was checked | Release decision |
|---|---|---|
| Yelp | The upstream card marks its license as other. Yelp's dataset agreement provides limited academic access and restricts third-party sharing in section 4(D); section 5 addresses derivatives. No applicable additional public-redistribution permission was found. | Reviews and generated rewrites withheld. |
| Arxiv | arXiv supports different per-version licenses and has a separate CC0 metadata policy. Stored derived abstracts lack a verified paper/version/field crosswalk to the applicable official metadata or article license. The summarization mirror card is not sufficient evidence for these exact texts. | Abstract inputs and rewrites withheld pending record-level mapping. This does not mean that all arXiv content is nonredistributable. |
| News | Frozen evidence maps 704 normalized unique inputs to a 730-record RAIDAR file with Reuters50-50 lineage. UCI currently marks Reuter_50_50 CC BY 4.0 and identifies it as an RCV1 subset; NIST's Reuters corpus page states copyright and agreement-based access. These notices and the exact article/version chain have not been reconciled for this subset. | News originals and rewrites withheld; the review does not assert that redistribution is categorically forbidden. |

Model terms are separate: Qwen2-7B and Mistral-v0.2 cards identify Apache 2.0; Gemma has custom terms and disclaims ownership of generated outputs; DeepSeek-LLM and Llama3 have their own model agreements. None provides missing rights to the input prose or guarantees that a rewrite is free of third-party rights. Historical accepted terms and complete original weight revisions were not recovered. This package contains no model weights and grants no license to the withheld texts.

No blanket MIT, CC BY or CC0 license is assigned to the underlying corpus. No project-wide open-source/content license has been selected for the newly prepared metadata/documentation/helper code; publicly hosting them must not be represented as a license grant for third-party texts. The publisher may separately choose an appropriate license for material it owns. Public accessibility does not by itself grant unrestricted reuse.

Primary references (links, not copied agreement texts):

- [Yelp dataset card](https://huggingface.co/datasets/Yelp/yelp_review_full)
- [Yelp dataset agreement](https://s3-media0.fl.yelpcdn.com/assets/srv0/engineering_pages/f64cb2d3efcc/assets/vendor/Dataset_User_Agreement.pdf)
- [arXiv licenses and metadata policy](https://info.arxiv.org/help/license/index.html)
- [Summarization source card](https://huggingface.co/datasets/ccdv/arxiv-summarization)
- [UCI Reuter_50_50](https://archive.ics.uci.edu/dataset/217/reuter+50+50), attribution: Zhi Liu, Reuter_50_50, DOI 10.24432/C5DS42
- [NIST Reuters corpus permissions](https://trec.nist.gov/data/reuters/reuters.html)
- [RAIDAR repository](https://github.com/cvlab-columbia/RaidarLLMDetect)
- [Gemma terms](https://ai.google.dev/gemma/terms)
- [DeepSeek model agreement](https://raw.githubusercontent.com/deepseek-ai/DeepSeek-LLM/main/LICENSE-MODEL)
- [Llama3 agreement](https://raw.githubusercontent.com/meta-llama/llama3/main/LICENSE)

Before adding any text, obtain and record applicable permissions, attribution and model-use obligations, perform a semantic privacy review, and prepare a separately versioned release. The present scripts intentionally never restore prose into this upload folder.
