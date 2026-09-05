# STAGE 3 — Literature Corpus: Search Execution, Screening, and PRISMA Flow

**Execution date:** 10 August 2026 (fallback run) · **Scopus re-run:** 10 August 2026 (access obtained same day) · **Protocol:** Stage2_Protocol.md
**Access note (disclosed per protocol §11):** Initial execution used the fallback (ScienceDirect + SpringerLink + Crossref API + IEEE Xplore) because Scopus was in Preview mode. **Full Scopus document-search access was subsequently obtained and all six protocol query families were executed on Scopus the same day** (§1b below) — Scopus is now the primary index of record. Web of Science remains unavailable (free personal Clarivate account without Core Collection entitlement); WoS absence is disclosed as a limitation, mitigated by Scopus + multi-source fallback coverage.

## 1b. Scopus Primary Searches (executed 10 Aug 2026, institutional access, exact protocol syntax)

| Family | Scopus advanced query (all with `PUBYEAR > 2011 AND (DOCTYPE(ar) OR DOCTYPE(re)) AND LANGUAGE(english)`) | Records |
|---|---|---|
| **A — Core (geopolymer × AI)** | `TITLE-ABS-KEY(("geopolymer*" OR "alkali-activated" OR "alkali activated") AND ("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network*" OR "data-driven"))` | **774** |
| **B — Trustworthy AI** | geopolymer block AND ("explainable" OR "XAI" OR "interpretab*" OR "SHAP" OR "uncertainty quantification" OR "calibrat*" OR "robustness" OR "reproducib*") | **403** |
| **C — Physics/chemistry-informed** | (geopolymer block OR "cementitious") AND ("physics-informed" OR "physics-guided" OR "chemistry-informed" OR "knowledge-guided" OR "scientific machine learning" OR "hybrid mechanistic") | **42** |
| **D — Multi-objective/inverse design** | (geopolymer block OR "low-carbon binder*") AND ("inverse design" OR "multi-objective optimi*" OR "Bayesian optimi*" OR "active learning" OR "materials informatics" OR "generative") | **123** |
| **E — Sustainability/carbon** | (geopolymer block OR "low-carbon binder*") AND ("machine learning" OR "artificial intelligence") AND ("carbon" OR "CO2" OR "sustainab*" OR "life cycle" OR "embodied carbon" OR "mineraliz*" OR "valoriz*") | **367** |
| **F — Autonomy (Context)** | ("materials discovery" OR geopolymer/cement/construction blocks) AND ("AI agent*" OR "agentic" OR "autonomous laborator*" OR "self-driving laborator*" OR "closed-loop experiment*" OR "digital twin") | **180** |

Interpretation: Scopus Family A (774) vs ScienceDirect harvest (320) confirms substantial non-Elsevier literature (Springer, MDPI, Wiley, T&F, ASCE, ACS) — consistent with the Crossref sweep findings. The C count (42, including OPC-cementitious hits) and the near-empty geopolymer share of F independently confirm the Stage-1 maturity map: physics-informed and autonomous stages are thin. **Next required action: export the Scopus Family A record set (CSV) and merge/dedup against the existing 393-record corpus.**

---

## 1. Search Log (verbatim, reproducible)

| # | Database | Query (Family A core) | Filters | Date run | Records |
|---|---|---|---|---|---|
| S1 | ScienceDirect | Title-abs-key: `("geopolymer" OR "alkali-activated") AND ("machine learning" OR "deep learning" OR "artificial intelligence" OR "neural network")` | 2012–2026; Research + Review articles | 2026-08-10 | **320** (all harvested) |
| S2 | SpringerLink | `"geopolymer" AND ("machine learning" OR "deep learning" OR "neural network")` | 2012–2026; content-type Article | 2026-08-10 | **950 identified** (full-text matching inflates count; top 20 relevance-ranked records harvested; full CSV export pending — flagged) |
| S3 | Crossref API | `query.bibliographic="geopolymer machine learning"` + `type:journal-article`, 2012–2026 | relevance-ranked | 2026-08-10 | top **60** harvested |
| S4 | Crossref API | `query.bibliographic="alkali-activated machine learning prediction"` + same filters | relevance-ranked | 2026-08-10 | top **40** harvested |
| S5 | IEEE Xplore | `geopolymer machine learning` | all years | 2026-08-10 | **13** (all conference papers → 0 core-eligible, EC4; documented as negative evidence) |

Full-text ScienceDirect variant of Family A (whole-document matching) returns 2,563 — recorded to document the title-abs-key restriction decision.

**Families B–F:** on ScienceDirect, Family A's harvested set was verified to subsume the B/D/E term hits (XAI/SHAP, multi-objective, CO₂/LCA items all present in the 320); Family C terms (physics-informed etc.) and Family F (autonomy) are captured through the same corpus plus Stage-1 context searches. Dedicated per-family Scopus counts remain pending Scopus access (flagged).

## 2c. CORPUS FREEZE — FINAL PRISMA NUMBERS (21 Aug 2026)

All screening stages complete: primary screen → 100% independent dual screen (κ_A=0.83, κ_B=0.689 pre-resolution) → adjudication of 59 disagreements (incl. 3 Author-1 tiebreaks, EC7 amendment) → full-text queue cleared (76 ledger entries; 11 rescued to INCLUDE after full-abstract/ML verification, 25 excluded EC3 [no ML — mostly Family-A keyword false positives via indexed keywords], 5 EC2, 3 EC7 venue-quality).

```
Identified (unique, all sources)      894  (+13 IEEE conference, excluded at source)
Excluded at screening                 104  (EC1:7 EC2:19 EC3:26 EC4:15 EC5:26 EC7:3 quality:1 other:7)
Context Corpus (reviews/adjacent)      58
FROZEN CORE CORPUS                    729 primary studies
  = 657 (Scopus set) + 72 (fallback-only: Springer/Crossref/SD records outside the Scopus Family-A net)
```

The corpus is FROZEN as of 21 Aug 2026. Any post-freeze additions (e.g., snowballing, pre-submission delta search) enter through a documented PRISMA amendment only. **Stage 5 full extraction now proceeds against these 729 studies** using schema v1.1.

## 2a. Merged PRISMA flow (10 Aug 2026 — superseded by §2c, retained for audit trail)

```
IDENTIFICATION
  Scopus Family A export (primary index)      n = 774
  Fallback sources (SD/Springer/Crossref)     n = 440 harvested
  IEEE Xplore                                 n = 13 (all conference → EC4 at source)

DEDUPLICATION (Scopus ↔ fallback, normalized-title matching)
  Scopus records matching already-screened fallback records   n = 326
  Fallback-internal duplicates (from initial run)             n = 47
  UNIQUE RECORDS, ALL SOURCES                                 n = 894
    = 774 Scopus + 120 fallback-only unique

SCREENING STATUS
  Screened with decisions (fallback pass + carried to Scopus matches):
    INCLUDE (core)                    283
    FULLTEXT-CHECK pending             35
    CONTEXT (reviews/adjacent)         22
    EXCLUDED (EC1–EC5/quality)         53
  New Scopus records auto-coded (title/doctype level):
    INCLUDE-PROVISIONAL               406  ← awaiting abstract-level + human dual screen
    CONTEXT-REVIEW                     36
    EXCLUDE-EC5 (auto, non-construction function)  6
  Fallback-only unique records retain their §2 decisions (71 INCLUDE among them)

CURRENT CORE CORPUS CANDIDATES: 283 confirmed + 406 provisional (+35 FT pending) → ceiling ≈ 724
```

## 2b. Abstract-Level Primary Screen of Provisional Records (10 Aug 2026)

All 406 INCLUDE-PROVISIONAL Scopus records were screened at title+abstract+keyword level (pattern-assisted, manually verified edge cases; one auto-flag false positive caught and corrected — logged):

- **394 → INCLUDE-ABSTRACT-CONFIRMED** (geopolymer/AAM term + ML method + construction-relevant function all verified present)
- **12 → FULLTEXT-CHECK-ABS** (no ML method detectable in abstract — suspected EC3/EC2: MCDM/fuzzy-AHP, particle-packing, purely statistical modeling)
- **1 → EC5** initially, reversed on manual abstract read (durability ML study; auto-pattern had matched incidental abstract text) — retained as INCLUDE

**Primary-screen state of the 774-record Scopus set + merged decisions:**
INCLUDE (confirmed, both passes): **639** · Context reviews: 53 (+2 adjacent) · Full-text pending: 41 (29 carried + 12 new) · Excluded: 36 · intra-set duplicates: 3

**Total core-corpus candidates including 71 fallback-only INCLUDEs: ≈ 710 primary studies** — pending the co-author dual screen (dispatched 10 Aug 2026: 472-row worksheets to Bhardwaj and Amritphale, 50-record shared calibration block, criteria one-pager attached) and the 41 full-text checks.

Implication: proper Scopus coverage roughly **doubles** the candidate corpus versus the Elsevier-weighted fallback — exactly why the Scopus re-run was required for Q1 defensibility. The 406 provisional records carry full abstracts in `corpus_master.csv`, ready for the protocol's abstract-level screen and the 20% human dual-screen.

**Files:** `scopus_familyA_export.csv` (raw export, 774), `corpus_master.csv` (774 records: matched decisions + new auto-codes, with DOI/EID/citations), `corpus_fallback_only.csv` (120 unique non-Scopus records), `corpus_screening.csv` (original screening ledger), `merge_corpus.py` (reproducible merge script).

## 2. PRISMA 2020 Flow (initial fallback execution — retained for audit trail)

```
IDENTIFICATION
  ScienceDirect (harvested)     n = 320
  SpringerLink (harvested)      n = 20   (of 950 identified; export pending)
  Crossref API (harvested)      n = 100
  IEEE Xplore                   n = 13   (screened at source: all conference → EC4)
  Records harvested             n = 440  (+13 IEEE screened out at source)

DEDUPLICATION
  Cross-source duplicates removed        n = 47
  Unique records                         n = 393

TITLE/ABSTRACT SCREENING (this pass)
  Excluded                               n = 53
    EC1 preprint/SSRN                      3
    EC2 out of material scope             14
    EC3 statistical-only                   1
    EC4 conference/proceedings            14
    EC5 non-construction function         18
    Quality-flagged venues                 3
  Routed to Context Corpus (reviews/adjacent)  n = 22
  Unsure → full-text assessment          n = 35
  Title/abstract INCLUDED (Core candidates)    n = 283

CURRENT STATUS
  CORE CORPUS (provisional)     n = 283  (+ up to 35 pending full-text checks)
  CONTEXT CORPUS                n = 22 from this search + 18 competitor reviews from Stage 1
```

## 3. Corpus File

`stage3/corpus_screening.csv` — 440 records, pipe-delimited: `id | source | year | venue | title | decision`. Every record carries its screening decision and duplicates are linked to their retained ID (e.g., `DUPLICATE-SD200`). This file is the seed of the open research artifact; DOI columns are populated for all Crossref records and will be completed for SD/SP records during Stage-5 extraction.

## 4. Observations Already Evident From the Corpus (preview for Stage 5 synthesis)

1. **Prediction-centric confirmation:** the overwhelming majority of the 283 core candidates are compressive-strength prediction studies — first direct corpus evidence for the §8 core thesis.
2. **The 2024–2026 delta is real and large:** well over half the corpus postdates the Nguyen et al. coverage window (ends Dec 2023), validating the review's timing claim.
3. **Trust practices are visibly thin but growing:** SHAP/XAI appears in dozens of 2024–2026 titles; explicit UQ appears in only a handful (e.g., SD10 amortised GP with UQ, SD261 prediction intervals, SD28 uncertainty analysis, SD314 Bayesian inference) — early signal for the trustworthy-AI scorecard.
4. **Physics/chemistry integration is an identifiable but small cluster:** SD17 (chemistry-informed DL), SD27 (PINN chloride diffusion), SD18 (physics-informed carbonation), SD126/SD187 (ML+thermodynamics), SD200 (chemistry-informed), SD54 (reactive-phase model), SD77/SD255/SD156 (knowledge-guided) — roughly 10 of 283.
5. **Multi-objective + carbon/cost optimization cluster:** ~20 studies (SD2, SD48, SD103, SD114, SD129, SD152, SD156, SD204, SD251, SD258, SD262, SD272, SD303, SD310…), several coupling NSGA-II/III with CO₂ objectives — Pillar 4 evidence base.
6. **Adaptive/autonomous evidence is nearly absent in geopolymers:** SD193 (sequential/active learning design of AAC), CR93 (active learning stacked ML), SD224 (Bayesian-optimization-assisted design), SD268 (tabular foundation models) are the only trajectory-stage-7 signals found; no digital-twin or agentic geopolymer study surfaced — confirming the Stage-1 maturity map and the roadmap positioning.
7. **Team's own paper (CR9, Materials 2026) enters the corpus on merit** through the Crossref sweep — to be disclosed and handled per COI norms in the manuscript.

## 5. Deviations and Pending Items (honest ledger)

- Scopus/WoS searches not executed (access) — **pending**; per-family PRISMA counts by database incomplete until then.
- SpringerLink harvest limited to top-20 relevance (of 950 full-text hits); full CSV export + title/abstract-restricted rescreen — **pending**.
- Screening was a single-pass title-level screen by one team; the protocol's 20% double-pass and abstract-level confirmation — **pending**.
- 35 FULLTEXT-CHECK records need full-text eligibility decisions.
- Forward/backward snowballing cycle — **pending** (planned after core corpus freeze).
- DOI completion for SD/SP records — **pending** (Stage 5 extraction pass).

*Stage 3 (initial execution) complete. STOP per protocol. Stage 4 (taxonomy development) can start from this corpus; pending items above do not block taxonomy design but must close before Stage 9 writing.*

## 2d. POST-FREEZE AMENDMENT — duplicate-report audit (31 Aug 2026, referee-response revision)

A systematic post-freeze duplicate audit (DOI matching incl. DOIs embedded in fallback record titles; title similarity with year+venue confirmation; full pair-level evidence in `stage5/duplicate_audit.csv`) identified **52 duplicate report pairs** inside the frozen 729-record Core Corpus. In every pair the duplicate is a fallback-harvest record (26 ScienceDirect, 24 Crossref, 2 SpringerLink) whose Scopus twin escaped the merge because the fallback title was abbreviated/truncated. Resolution: the Scopus record is canonical; duplicates are flagged in `extraction_master.csv` (`duplicate_of` column), never deleted.

**Corrected PRISMA accounting (records vs studies, per PRISMA 2020):**
- Records identified: 774 (Scopus A) + 440 (fallback: SD 320, Crossref 100, Springer 20) = 1,214 (+13 IEEE conference records excluded at source, EC4)
- Duplicate records removed before screening: 320 → **894 unique records screened**
- Removed during screening: 3 duplicates (DUPLICATE-SD265/277/71) · Excluded: 104 (EC1 4, EC2 21, EC3 28, EC4 14, EC5 31, EC7/venue-quality 6) · Context Corpus: 58 → **729 records included**
- Duplicate reports identified during synthesis: 52 → **677 unique primary studies** (all corpus-wide statistics recomputed on n = 677)

Check: 3 + 104 + 58 + 729 = 894 ✓ · 729 − 52 = 677 ✓
