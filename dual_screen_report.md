# Dual-Screening Agreement Report

**Date:** 21 August 2026 · **Inputs:** completed worksheets from Verifier A (Pooja Bhardwaj/Chaggar, 472 records) and Verifier B (472 records — **identity to be confirmed**, file received as "verifierB_PC"; sheet was assigned to S. Amritphale) · **Method:** Cohen's kappa vs the primary screen; A↔B kappa on the 50-record blind calibration block.

## Results

| Comparison | n comparable | % agreement | Cohen's κ | Reading |
|---|---|---|---|---|
| Verifier A ↔ primary (full 8-code) | 437 | 95.2% | **0.830** | Almost perfect / excellent |
| Verifier A ↔ primary (binary in/out) | 437 | 96.8% | 0.788 | Substantial |
| Verifier B ↔ primary (full 8-code) | 447 | 91.5% | **0.689** | Substantial (just below the pre-registered 0.7 trigger) |
| Verifier B ↔ primary (binary in/out) | 447 | 95.3% | 0.652 | Substantial |
| **Verifier A ↔ Verifier B (calibration block)** | 50 | 98.0% (49/50) | **0.933** | Almost perfect |

Records excluded from kappa: UNSURE codes (A: 1, B: 6), not-found/blank (A: 3), and records whose primary decision was itself FULLTEXT-pending.

## Interpretation

1. **Verifier A's κ = 0.83** validates both the criteria sheet and the primary screen — well above the 0.7 pre-registered threshold.
2. **Verifier B's κ = 0.689 is driven by one systematic pattern, not noise:** 12 of B's 36 disagreements are `REVIEW → INCLUDE` — B coded review/survey papers as INCLUDE instead of tagging them REVIEW. This is a criterion-interpretation issue (the REVIEW tag), not a scope disagreement: those papers are all in-scope, just mis-binned. Sensitivity check: excluding this single pattern, B's raw agreement rises to ≈94%. Per the pre-registered rule, the response to κ<0.7 is expansion or adjudication — since 100% dual coverage already exists, the correct action is **adjudication of the 59 disagreements with a criterion clarification on REVIEW**, then recomputation of B's κ for the manuscript.
3. **A↔B calibration κ = 0.933 (49/50 identical)** — inter-verifier consistency is excellent.

## Integrity item — RESOLVED (21 Aug 2026)

Verifier B identity confirmed by the team lead: **S. Amritphale** completed sheet B. The two-independent-verifier design holds as registered. One residual note for the methods section: a few of B's notes have tool-like phrasing ("no clear ML/statistical method keyword detected in title+abs") — if any software assistance was used during his screen, it should be named in the methods (tool-assisted human screening is fully acceptable when disclosed). Confirm with him in the adjudication call and record the answer here.

## Adjudication outcome (applied 21 Aug 2026)

Both verifiers returned the adjudication sheet. Of 57 unique disputed records: 25 → INCLUDE, 10 → REVIEW (Context), 9 → EC2, 8 → EC5, 1 → EC1 (a retraction notice caught by Verifier B — a genuine catch the primary screen missed), 1 → EC4, and **3 residual items awaiting the Author-1 tiebreak** (CR47 biodiesel review: EC5 vs EC2 code choice; CR53 & CR12: quality-flagged venues vs Verifier B's INCLUDE). All 54 settled decisions are applied to `corpus_master.csv` and `corpus_screening.csv`.

Post-adjudication consensus agreement for Verifier B: 99.6% (κ = 0.98). **For the manuscript, report the pre-resolution κ (A: 0.83; B: 0.689) plus the consensus process** — post-consensus κ approaches 1 by construction and should not be presented as an independent agreement measure.

Corpus state after adjudication (Scopus set): **INCLUDE 646 · CONTEXT 50 · FULLTEXT-pending 41 · EXCLUDED 34** (+71 fallback-only includes).

## Actions

- `screening_disagreements.csv` (59 rows) → three-way resolution: for each, the tiebreak discussion records a final decision + one-line rationale. The 12 REVIEW→INCLUDE cases can be batch-resolved after confirming the papers are reviews.
- 9 UNSURE/not-found records → added to the full-text check queue (now 41 + 9 = 50 pending full-text decisions).
- After resolution + full-text checks → **corpus freeze**, final PRISMA numbers, and Stage 5 full extraction begins.
