# STAGE 6 — Evidence-Based Research Gaps

**Date:** 21 August 2026 · **Evidence base:** frozen corpus n=729 (Stage 3), corpus-wide coding (Stage 5 Batch 1), deep extraction (16 full rows) and three cluster audits (physics n=23, carbon/LCA n=76, UQ/adaptive characterized). Every Evidence line cites corpus-derived numbers, not impressions. Structure per protocol: Evidence → Gap → Root cause → Scientific/Environmental consequence → Research opportunity → Validation requirement.

---

## G1 — The calibration desert

**Evidence.** UQ appears in 5.9% of 729 studies; explicit calibration evaluation (PICP/MPIW/CWC/Winkler) in 1.2% (9 papers); the calibrated-conformal exemplars trace to ~2 author groups (extraction_deep DEEP-06/07, PILOT-01). 62.1% of studies exhibit no detectable trust practice at all.
**Gap.** Predictions carry no usable reliability information: the field reports accuracy (R²) without validity of confidence.
**Root cause.** Benchmark culture rewards leaderboard metrics; conformal/Bayesian tooling only recently became accessible for tabular data; no journal reporting requirement.
**Consequence.** Mix-design decisions (and any future autonomous loop) cannot budget risk; a model with R²=0.95 and unknown coverage is unusable for engineering acceptance, blocking standards adoption of AI-designed geopolymers.
**Opportunity.** Corpus-wide adoption of distribution-free conformal prediction (already demonstrated on geopolymer data: PICP 0.97 at 90% nominal, MPIW ≈1.2 MPa — DEEP-07); calibration reporting as standard practice.
**Validation requirement.** Prospective coverage tests on newly synthesized (not held-out) mixes; report PICP/interval width at declared confidence levels alongside accuracy.

## G2 — Interpolation masquerading as prediction (validity-domain gap)

**Evidence.** Corpus authors themselves concede high R² "mainly reflects dense interpolation within the… experimental envelope rather than unrestricted extrapolation" (DEEP-07). Only one dedicated out-of-range protocol exists in 729 papers (18% out-of-domain test set, DEEP-16); OOD/transfer signals in 8.0% of abstracts; the same few literature databases (594-, 672-, 676-record compilations) recirculate across dozens of studies.
**Gap.** Reported performance does not measure what deployment needs: behavior on new precursors, new labs, new regions.
**Root cause.** Random train/test splitting of compiled literature data; duplicated source datasets (Parakhiya's audit removed 37 duplicate records from a 594-record standard database); no applicability-domain reporting convention (unlike QSAR, where it is mandatory).
**Consequence.** Systematic optimism; models fail silently on the waste-stream variability that is precisely the clean-technology value proposition (local, variable industrial residues).
**Opportunity.** Import the applicability-domain discipline from cheminformatics; leave-one-source-out and leave-one-precursor-out validation; out-of-range protocols as default.
**Validation requirement.** Cross-laboratory round-robin: one shared blind mix set, predicted by all published models — the field has never run one.

## G3 — Physics-claim inflation over a thin genuine frontier

**Evidence.** Of 23+ "physics/chemistry-informed" claims audited, ≈50% deflate to ordinary feature engineering; verified Type III+ integration exists in ~10 of 729 papers (≈1.4%) (physics_type_verification.csv). The genuine frontier spans 2021 (ML+GEMS thermodynamics) to 2026 (equation-embedded NN inside four-objective NSGA-II).
**Gap.** Domain knowledge is invoked rhetorically but rarely structurally; reaction kinetics, thermodynamic constraints, and mass balance are almost never embedded in learning.
**Root cause.** No agreed terminology (the review's Type I–V scale addresses this); embedding physics requires dual competence that few groups hold; incentive to keyword-match trending terms.
**Consequence.** Models violate chemistry silently (no constraint stops a physically impossible mix recommendation); transferability across precursor chemistries stays poor — exactly where physics would help most.
**Opportunity.** Standardize the integration-type taxonomy; couple the verified exemplars (PINN transport models, thermodynamic hybrids, knowledge graphs) to the dominant prediction pipelines; physics-informed surrogates inside optimization loops.
**Validation requirement.** Constraint-violation audits of model recommendations; ablation evidence that the physics term (not extra features) drives improvement.

## G4 — The environmental quantification void

**Evidence.** 46.6% of the corpus has no explicit environmental variable. Within the 76 most environmentally engaged papers: ISO/boundary-explicit LCA 3% (2 papers; ≈0.3% corpus-wide), rhetoric-only 28%. The entire "carbon-as-objective" optimization subfield is 25 papers, and its carbon data are generic per-constituent emission factors without uncertainty (carbon_lca_audit.csv; DEEP-P04).
**Gap.** "Sustainable/low-carbon" claims are structurally unsupported: no system boundaries, no regionalized inventories, no factor uncertainty, no trade-off transparency.
**Root cause.** Disciplinary separation of LCA and ML communities; emission factors are copy-pasteable while LCA requires inventory work; journals accept "green" framing without quantification.
**Consequence.** For a clean-technology journal this is the central failure: AI optimizes carbon numbers that may be wrong by the margin being optimized; policy and procurement cannot rely on the outputs; greenwashing risk for the field's credibility.
**Opportunity.** ML-LCA coupling with uncertainty propagation from emission factors through Pareto fronts; regionalized waste-stream inventories; carbon-verified benchmark datasets.
**Validation requirement.** Any AI-optimized "low-carbon" mix must carry an ISO-14040/44-consistent cradle-to-gate assessment with factor uncertainty, and at least one physical batch verified for both strength and inventory data.

## G5 — Adaptive loops are simulated; the autonomous stage is empty

**Evidence.** Experiment-selection studies: 4 of 729 (0.5%), all retrospective/simulated on literature pools (2021→2025); the closest lab coupling is spot-validation of an AL-tuned GUI (DEEP-11). Digital twins for geopolymer materials: 0. Robotic/self-driving experimentation: 0. LLM involvement: 1 design-support paper (2026). Autonomous discovery: 0.
**Gap.** The trajectory's upper half (adaptive → twin → agentic → autonomous) has no physical demonstration in geopolymers, while adjacent materials science runs closed loops routinely.
**Root cause.** 28-day strength verification breaks loop tempo; heterogeneous waste feedstocks resist standardized robotic handling; no geopolymer lab has integrated the (existing) SDL stack; funding favors modeling papers over instrumentation.
**Consequence.** The claimed acceleration of clean-binder development never materializes physically; discovery remains bounded by literature data (G2).
**Opportunity.** Early-age surrogate targets (7d→28d posterior updating is already demonstrated, PILOT-01) to fix loop tempo; a first geopolymer SDL demonstration on one-part binders (dry powders = robot-friendly); LLM agents for literature-to-inventory extraction feeding G4.
**Validation requirement.** A physical closed loop completing ≥2 model-propose→synthesize→test→update cycles, reported with per-cycle uncertainty reduction — the field's first would be publishable in itself.

## G6 — Data infrastructure: recycled small data, invisible provenance

**Evidence.** Dominant datasets are literature compilations of 100–900 records recirculated across studies (multiple deep rows share source databases); dataset openness is commonly claimed but code availability was explicit in ~1% of abstracts and 0 of 11 deep-extracted papers stated a code repository; duplicate contamination is documented (37/594).
**Gap.** No shared benchmark, no canonical splits, no provenance tracking, no leakage control conventions; reproducibility is unverifiable.
**Root cause.** No community data standard (contrast: OPC concrete's open repositories); publication incentives favor new models over data curation.
**Consequence.** Cross-paper metric comparisons are scientifically indefensible (protocol §24); cumulative progress is illusory when 50 models are tuned on the same 600 rows.
**Opportunity.** A FAIR geopolymer-AI benchmark with fixed leakage-safe splits, provenance metadata, oxide-composition completeness, and environmental inventory fields — this review's open artifact is a seed.
**Validation requirement.** Benchmark adoption measurable by ≥3 independent groups reporting on identical splits.

## G7 — External and cross-laboratory validation deficit

**Evidence.** Explicit external validation signals: 3.7% of corpus; genuinely independent test sets in deep extraction: 2 of 16 (DEEP-10 independent test with honest degradation 6.23→7.86 MPa MAE; DEEP-11 experimental spot-checks). Interlaboratory validation: 0.
**Gap.** Models are never confronted with another lab's specimens, another country's fly ash, or a future point in time.
**Root cause.** Compiled-data culture (G6); no incentive to fund validation batches; lab-to-lab variability in AAM testing is itself under-characterized.
**Consequence.** Unknown real-world error bars; standards bodies (G8) have no basis to accept model-designed mixes.
**Opportunity.** Time-split validation (train pre-2024, test 2025+ publications) is available immediately from this corpus; funded round-robins next.
**Validation requirement.** Report degradation curves (CV → held-out → external-lab → prospective) as the standard evaluation ladder.

## G8 — The deployment disconnect

**Evidence.** D-axis coding: the corpus's most advanced deployment stage is "formulation recommendation/decision-support tool" (a handful of GUIs and recommenders); pilot implementation: 0; certification-oriented studies: 0; standards engagement: absent from all 729 abstracts.
**Gap.** No pathway connects AI-designed geopolymers to codes (which remain OPC-calibrated), certification, or procurement — the last mile of the clean-technology transition is unaddressed by the AI literature.
**Root cause.** AI papers end at metrics; standards work is slow, unrewarded, and requires the validation ladder (G1, G2, G7) that does not exist.
**Consequence.** Even perfect models cannot decarbonize construction if no acceptance framework consumes their outputs; CTEP's deployment mandate is precisely this hole.
**Opportunity.** Performance-based (rather than prescriptive) acceptance protocols with model uncertainty as an explicit input; digital material passports carrying provenance + LCA + prediction intervals.
**Validation requirement.** A documented case of an AI-designed AAM mix passing a performance-based approval process, even at pilot scale.

## G9 — Unresolved contradiction: synthetic data augmentation

**Evidence.** Direct conflict within the corpus: GAN/VAE augmentation reported to enable reliable mix design (DEEP-08, R²=0.959) versus CTGAN augmentation degrading accuracy and generalization (DEEP-09); multiple further augmentation papers (imputation+augmentation, Gaussian-noise, GP-guided boundary synthesis) report benefits without harm tests.
**Gap.** No controlled understanding of when synthetic tabular data helps, inflates optimism, or corrupts the physics of the learned mapping.
**Root cause.** Augmentation evaluated on the same small distributions it was fitted to; no agreed audit (train-on-synthetic/test-on-real-only is not universal).
**Consequence.** A popular workaround for G6 may be manufacturing confidence rather than knowledge.
**Opportunity.** Systematic augmentation benchmark on the G6 shared dataset with real-only test sets and physics-constraint violation checks (links G3).
**Validation requirement.** Synthetic-data papers must demonstrate real-only-test parity and constraint compliance before augmentation claims are accepted.

---

**Gap interdependency note for the roadmap (Stage 7):** G6 (data) underpins G1/G2/G7 (trust ladder), which underpin G8 (deployment); G3 (physics) and G4 (LCA) are the two content couplings that make the trust ladder worth climbing for a *clean-technology* outcome; G5 (autonomy) is the acceleration layer that presupposes all of it. This dependency chain is the roadmap's spine.

*Stage 6 complete. STOP per protocol. Stage 7 (clean-technology roadmap) next on approval.*
