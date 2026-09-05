# SpringerLink Unharvested-Records Random-Sample Screen (M9) — 31 Aug 2026

**Purpose.** The original SpringerLink arm harvested only the top 20 relevance-ranked records of 950 full-text matches. To bound the yield of the unharvested remainder, a random sample of 50 ranks (seed 20260831, ranks drawn uniformly from 21–950) was screened against the protocol eligibility criteria.

**Re-execution.** Same query (`"geopolymer" AND ("machine learning" OR "deep learning" OR "neural network")`), content-type Article, 2012–2026, run 31 Aug 2026 on link.springer.com. Result count at re-execution: **978** (drift +28 since 10 Aug freeze — post-freeze publications; sampled ranks interpreted against the current ranking).

**Screening outcome (n = 50 sampled records, title + abstract-snippet level):**

| Category | n | Notes |
|---|---|---|
| Not eligible — out of material/topic scope (EC2) | 36 | OPC/blended concrete, soils without geopolymer binder, asphalt, rocks, house pricing, spillways, textiles, thermoelectrics, etc. — full-text matching inflates the count with studies that merely cite geopolymer work |
| Not eligible — review articles | 5 | concrete-ML reviews, green-construction review, bridge-engineering annual review |
| Not eligible — no ML method (EC3) | 2 | experimental/statistical only |
| **Eligible-type studies** | **7** | geopolymer/AAM + ML + construction function |
| — of which already in Core Corpus via Scopus | 7 | title-match 1.00 to corpus records (incl. Jagad & Thoriya conformal study, rank 345; phosphogypsum GPC, rank 120; fly-ash GPC soft computing 85196161609; RCPT geopolymer 105027164063; bauxite-residue ANN 85164146987; AAC ANN/M5P 85131576343; lateritic geopolymer-soil AI 85130122744) |
| **Eligible AND new to corpus** | **0** | — |

**Estimate.** New-eligible yield in the sample: 0/50. One-sided exact 95% upper bound for the new-eligible proportion: 5.8%, i.e., at most ≈54 of the ~928 unharvested records — but the observed mechanism (every eligible Springer-published study in the sample was Scopus-indexed and captured by Family A) indicates the true number is near zero. Springer's full-text matching accounts for the large raw count: 86% of sampled matches were out of scope or reviews.

**Conclusion for §21 / Supplementary Note S7.** The SpringerLink depth limitation is bounded: the unharvested remainder is dominated by out-of-scope full-text matches, and its eligible content is duplicative of the Scopus arm. Point estimate of missed unique studies: 0 (95% upper bound ≈54; expected value given the Scopus-subsumption mechanism: ≈0).
