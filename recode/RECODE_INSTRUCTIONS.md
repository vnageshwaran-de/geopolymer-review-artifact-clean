# Independent Coding-Reliability Recode — Instructions (v1.0, 31 Aug 2026)

**Purpose.** A referee-grade check of the corpus coding: you independently code 70 randomly sampled, year-stratified studies **blind** to the original codes. Per-axis agreement (Cohen's κ or % agreement) will be reported in Supplementary Table S9. Disagreement is informative, not a problem — please do NOT try to guess "the expected answer"; code exactly what the title + abstract supports.

**Time estimate.** ~2–3 minutes per record ≈ 2.5–3.5 hours. Feel free to split across sittings.

**File.** `recode_worksheet_blind_70.csv` — one row per study, with title, abstract, venue, year. Fill in the empty columns only. Base every judgment on the title + abstract text provided (that is the depth at which the original coding was performed — full-text lookup is not wanted here, it would break comparability).

## Column guide

1. **M_material_system** — main precursor system(s), semicolon-separated if several apply:
   `fly-ash` · `slag` · `FA-slag` · `metakaolin/clay` · `red-mud` · `tailings` · `biomass-ash` · `recycled-aggregate` · `one-part` · `stabilized-soil` · `mixed/other-AAM`
2. **T_primary_task** — ONE primary label, using this priority order (highest applicable wins):
   `experiment-selection` (active/sequential learning) > `inverse-design` > `multi-objective-optimization` > `optimization` > `classification` > `microstructure/image-analysis` > `prediction`
3. **P_physics_type_I_to_V** — conservative; ambiguity resolves DOWN:
   `I` data-driven only · `II` oxide/chemistry quantities used merely as input features · `III` domain knowledge shapes the model structure or feature construction (e.g., knowledge graph) · `IV` constraints/equations embedded in loss or architecture (PINN etc.) · `V` coupled mechanistic simulation (e.g., thermodynamic modelling) + ML.
   Code what the abstract *demonstrates*, not the label the authors use.
4. **E_env_function** — semicolon-separated, quantification required (the word "sustainable" alone earns nothing):
   `none-explicit` · `waste-valorization` · `durability` · `cost` · `carbon` · `LCA`
5. **D_deployment_stage** — furthest stage reached: `lab-prediction` · `validated-model` · `recommendation/decision-support` · `process-optimization` · `pilot` · `adaptive` · `autonomous`
6. **SC_*_YN columns** — `Y` only if the abstract gives concrete evidence of the practice; otherwise `N`:
   explainability (SHAP/PDP/importance) · uncertainty (intervals/Bayesian/conformal) · calibration (coverage/reliability evaluated) · robustness (perturbation/sensitivity tests) · OOD_or_transfer (out-of-distribution, cross-domain, transfer, extrapolation testing) · external_validation (data independent of training source) · physical_consistency (outputs checked against physical plausibility) · reproducibility (code/data repository stated)
7. **notes** — optional; flag anything ambiguous.

**Independence rules.** Work alone; do not consult the released artifact, the manuscript, or each other; return the file as-is by email when done.
