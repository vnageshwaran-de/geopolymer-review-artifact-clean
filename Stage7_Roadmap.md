# STAGE 7 — Clean-Technology Roadmap for Trustworthy AI in Low-Carbon Geopolymer Development

**Date:** 21 August 2026 · **Basis:** Stage 6 gap chain (G6 data → G1/G2/G7 trust ladder → G8 deployment, with G3 physics + G4 LCA couplings and G5 autonomy as acceleration layer). Horizons are indicative (I: 0–2 y, E: 2–5 y, F: 5–10 y) and every item names the gap it discharges and its validation requirement.

---

## 1. Immediate priorities (0–2 years) — *make existing models honest*

| # | Priority | Gaps | What "done" looks like |
|---|---|---|---|
| I1 | **FAIR geopolymer-AI benchmark**: consolidated, provenance-tracked, leakage-safe dataset with fixed splits, oxide-composition completeness, and environmental-inventory fields (seeded by this review's open artifact) | G6 | ≥3 independent groups reporting on identical splits |
| I2 | **Calibration-by-default**: conformal prediction intervals + PICP/width reporting alongside R²/RMSE (already demonstrated on geopolymer data at negligible cost) | G1 | journals/reviewers request coverage metrics; the 9-paper practice becomes the norm |
| I3 | **Applicability-domain reporting** imported from QSAR: leave-one-source-out and leave-one-precursor-out validation, out-of-range test protocols, degradation ladders (CV → held-out → external → prospective) | G2, G7 | every performance claim bounded by a stated validity domain |
| I4 | **Terminology discipline**: the Type I–V physics-integration scale and simulated-vs-physical adaptive labels adopted in reporting | G3, G5 | claims audit-able; ~50% inflation rate measurably falls |
| I5 | **Time-split meta-validation** using this corpus (train ≤2023 literature, test 2024–2026 results) — executable now, no new experiments | G7 | published degradation estimate for the field's standard models |

## 2. Emerging priorities (2–5 years) — *couple the models to chemistry and carbon*

| # | Priority | Gaps | What "done" looks like |
|---|---|---|---|
| E1 | **Physics-constrained surrogates inside optimization loops**: extend the verified frontier (thermodynamic hybrids, equation-embedded NNs, PINN transport models) from prediction into NSGA-II/BO design loops, with constraint-violation audits | G3 | model recommendations provably chemistry-feasible; ablations isolate the physics contribution |
| E2 | **ML-LCA integration with uncertainty propagation**: regionalized waste-stream inventories; emission-factor uncertainty carried through to Pareto fronts; ISO-14040/44-consistent boundaries as the entry ticket for "low-carbon" claims | G4 | the 25-paper carbon-objective subfield reports factor uncertainty; ISO-grade share rises from ~0.3% |
| E3 | **Cross-laboratory round-robin**: shared blind mix set, all published models predict, results public | G7, G2 | first field-wide real-world error bar |
| E4 | **Early-age-updating models as loop enablers**: 7d→28d posterior frameworks standardized to break the verification-tempo barrier | G5, G1 | validated acceleration of qualification cycles |
| E5 | **Augmentation adjudication**: controlled benchmark resolving the GAN-helps vs GAN-harms contradiction (real-only tests + constraint compliance) | G9, G6 | evidence-based guidance on when synthetic tabular data is admissible |

## 3. Frontier opportunities (5–10 years) — *close the loop, then scale it*

| # | Priority | Gaps | What "done" looks like |
|---|---|---|---|
| F1 | **First geopolymer self-driving laboratory**, entry point: one-part dry-powder binders (robot-friendly dosing; no activator-solution handling), early-age surrogate targets, calibrated-UQ acquisition | G5 (presupposes I1–I3, E1, E4) | ≥2 physical propose→synthesize→test→update cycles with per-cycle uncertainty reduction — the field's first closed loop |
| F2 | **Digital twins of curing and durability evolution** for AAM structures, fed by monitoring (AE, embedded sensing) + PINN transport models | G5, G3 | twin-predicted vs measured service-life indicators on a pilot element |
| F3 | **LLM/agentic support systems** — grounded in the 2026 entry points (LLM-built knowledge graphs; foundation-model tabular predictors): literature-to-inventory extraction agents feeding E2, protocol-drafting copilots for F1. Explicitly prospective; no autonomous-agent claims until F1-class loops exist | G5, G4, G6 | agent-extracted inventories match human curation at audited accuracy |
| F4 | **Transferable foundation models for waste-derived binders**: pre-trained across precursor chemistries with OOD guarantees, fine-tuned to local waste streams | G2, G6 | out-of-range performance bounds certified per deployment region |

## 4. Deployment priorities — *give model outputs somewhere to go* (parallel track, starts now)

| # | Priority | Gaps | What "done" looks like |
|---|---|---|---|
| D1 | **Performance-based acceptance protocols** that consume prediction intervals: acceptance = predicted property with declared coverage + conformity testing plan | G8, G1 | one AI-designed AAM mix passes a performance-based approval at pilot scale |
| D2 | **Digital material passports** for AAM mixes: provenance, oxide composition, LCA inventory, prediction intervals, validity domain | G8, G4, G6 | passport schema adopted by ≥1 procurement pilot |
| D3 | **Demonstration ladder**: lab → precast elements (low regulatory friction) → non-structural site applications → structural pilots, each with published model-vs-reality audits | G8, G7 | public model-audit trail across TRLs |

## 5. Standards & governance needs

1. **Reporting standard for AI-in-construction-materials studies** (checklist: data provenance, splits, validity domain, calibration metrics, environmental boundary, code/data availability) — the review's scorecard is a draft of exactly this.
2. **LCA disclosure rule**: "low-carbon/sustainable" claims in AI-materials papers require boundary-explicit quantification (journal policy lever; CTEP could lead).
3. **Standards-body engagement** (RILEM TC / ASTM / EN): performance-based AAM acceptance with explicit treatment of model-based evidence and uncertainty — currently zero engagement across 729 papers.
4. **Benchmark governance**: community stewardship of the FAIR dataset (I1) with versioning, leakage policing, and contribution credit.
5. **Provenance & integrity**: retraction propagation into compiled datasets (this corpus caught one retraction only via human dual-screen), authorship/AI-assistance disclosure norms.

---

**Roadmap logic in one line:** honest models first (I1–I5), chemistry- and carbon-coupled models second (E1–E5), closed loops third (F1–F4), with the deployment track (D1–D3) and governance levers (§5) running in parallel from day one because they are the slowest — and, for a clean-technology outcome, the point.

*Stage 7 complete. STOP per protocol. Stage 8 (manuscript blueprint: final title confirmation, abstract architecture, section structure, figures/tables, contribution statement) next on approval.*
