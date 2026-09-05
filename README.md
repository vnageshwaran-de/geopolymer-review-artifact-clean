# Trustworthy AI for Low-Carbon Geopolymers — Research Artifact

Open research artifact accompanying:

> Nageshwaran V., Bhardwaj (Chaggar) P., Amritphale S.S. (2026). *From Property Prediction to Clean-Technology Deployment: A Systematic Review and Roadmap for Trustworthy AI in Low-Carbon Geopolymer Development.* (Under preparation for Clean Technologies and Environmental Policy.)

This repository releases the complete evidence chain of the systematic review so that every quantitative claim in the paper can be re-examined, and so the coded corpus can seed a community FAIR benchmark (roadmap item I1 in the paper).

## Contents

| File | Description |
|---|---|
| `corpus_screening.csv` | Screening ledger for all harvested records (pipe-delimited): per-record decision + reason code |
| `corpus_master.csv` | 774 Scopus-set records with merged screening decisions, DOI, EID, citations |
| `corpus_fallback_only.csv` | 120 unique records identified only via supplementary sources |
| `extraction_master.csv` | The frozen 729-study core corpus, coded on the six taxonomy axes (M/T/E/trust/P) + depth tier |
| `extraction_deep.csv` | Full-template deep-extraction rows (v1.1 schema) incl. trustworthy-AI scorecard |
| `extraction_pilot.csv` | Pilot extraction rows (schema v1.0) |
| `physics_type_verification.csv` | Claimed-vs-verified audit of all physics/chemistry-informed claims |
| `carbon_lca_audit.csv` | Environmental-treatment audit of the 76 most environmentally engaged studies |
| `adjudication_final.csv` | Final consensus decisions for all dual-screening disagreements |
| `dual_screen_report.md` | Inter-rater agreement analysis (Cohen's kappa) and adjudication record |
| `Stage2_Protocol.md` | Pre-registered systematic-review protocol (incl. dated amendments) |
| `Stage3_Corpus_Report.md` | Search log, PRISMA counts, corpus freeze record |
| `Stage6_Research_Gaps.md` | Evidence-based gap framework (full six-step chains) |
| `Stage7_Roadmap.md` | Clean-technology roadmap (full version) |
| `merge_corpus.py` | Reproducible corpus merge/deduplication script |
|  Publication figures F1–F8 (flat, prefixed `F*.png`) | Publication figures (PRISMA, maturity ladder, trust heatmap, audits, roadmap) |
|  Manuscript tables (flat, prefixed `T*.csv`) | Manuscript tables T1–T7 |
| `manuscript/latex_submission/` | Submission-ready manuscript: LaTeX source, bibliography, class files, compiled PDF, figures |
| `manuscript/word_submission/` | Submission-ready manuscript, cover letter, and supplementary materials (.docx) with figures |
| `recode/` | Blind coding-reliability recode worksheets, completed recodes (human and procedural), and scoring script (Supplementary Table S9) |

## Provenance & integrity notes

- Search executions: Scopus (primary index) + ScienceDirect + Crossref + SpringerLink, 10 Aug 2026; corpus frozen 21 Aug 2026.
- Screening: primary screen by the first author; **100% independently dual-screened** by two co-authors (κ = 0.830 / 0.689 pre-resolution); all disagreements adjudicated by consensus.
- Verifier worksheets are not included to respect screeners' working files; the consensus outcomes and agreement statistics are fully reported.
- A retraction notice identified during screening is excluded and flagged in the ledger.

## License & citation

Data and documentation: CC BY 4.0. Code: MIT. Please cite the paper above (and this repository) when reusing the corpus or audit instruments. Versioned archive: Zenodo DOI **[to be added]**.
