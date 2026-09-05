# STAGE 2 — Systematic Review Protocol

**Project:** From Property Prediction to Clean-Technology Deployment: A Systematic Review and Roadmap for Trustworthy AI in Low-Carbon Geopolymer Development
**Target journal:** Clean Technologies and Environmental Policy (Springer)
**Protocol date:** 10 August 2026 · **Reporting standard:** PRISMA 2020
**Evidence policy:** Peer-reviewed published literature only. Preprints, theses, editorials, and non-archival web content are excluded from the evidence corpus at all stages.

---

## 1. Protocol Registration and Governance

- PROSPERO does not accept materials-science reviews; in lieu of registration, this protocol is frozen before searching (this document, version-controlled) and any post-hoc deviation will be disclosed in the manuscript's limitations section (§22 of the blueprint).
- Two-corpus design (prevents scope creep and reviewer objection #4 from Stage 1):
  - **Core Corpus (PRISMA-governed):** primary studies applying AI/ML to geopolymer / alkali-activated materials. Full extraction, quality assessment, scorecard.
  - **Context Corpus (narrative, clearly labeled):** (a) prior reviews (competitor set from Stage 1); (b) adjacent-domain evidence for trajectory stages absent in geopolymers (self-driving labs, digital twins, LLM agents in general materials science). Context items are never counted in PRISMA totals and never graded as geopolymer evidence — they feed the three-level evidence map only.

## 2. Database Selection (with justification)

| Database | Role | Justification |
|---|---|---|
| **Scopus** | Primary index | Broadest indexing of the venues that dominate this literature (Construction and Building Materials, Journal of Building Engineering, Materials, Ceramics International — top-5 venues per Nguyen et al. 2025); exports structured records for dedup/screening |
| **Web of Science** | Primary index (cross-check) | Independent coverage check against Scopus; citation chasing for snowballing |
| **ScienceDirect** | Full-text source | Elsevier hosts the two highest-yield journals (CBM ~30 papers, JOBE ~7+ in prior corpus); needed for full-text eligibility assessment and extraction |
| **SpringerLink** | Full-text source | CTEP itself, plus Silicon, Asian J. Civil Engineering, Archives of Computational Methods in Engineering, AI in Civil Engineering — high-yield Springer venues confirmed in Stage 1 |
| **IEEE Xplore** | Targeted (Family F only) | Stage 1 verified only 13 geopolymer-ML items (all conference). Retained solely for the autonomous/agentic query family and to document (auditably) that the computing literature holds no journal survey |
| **Crossref** | Verification layer | DOI/metadata verification of every included record; not a discovery source |
| **Google Scholar** | Supplementary only | Forward/backward snowballing and grey-area checks; hits admitted only if they resolve to a peer-reviewed published record indexed or verifiable via Crossref |

**Excluded databases (justified):** ACM Digital Library (zero relevant corpus expected; construction-materials AI publishes in engineering/materials venues — spot-check will be documented); Dimensions (redundant with Scopus/WoS for this domain; adds dedup burden without unique coverage). MDPI/Wiley/Taylor & Francis content is reached through Scopus/WoS indexing plus snowballing.

## 3. Search Window and Dates

- **Window: 1 January 2012 – 31 August 2026.** Rationale: 2012 = first published ML-geopolymer studies (established by Nguyen et al. 2025); the 2024–2026 span is the review's differentiating delta (Nguyen's corpus ends Dec 2023; Zheng's is narrative). End date set at search execution; exact execution dates will be recorded per database.
- All searches re-run once immediately before submission; delta-screening documented.

## 4. Database-Specific Search Strings

Conceptual families A–F from the master prompt, adapted per platform. Geopolymer block is shared:

`GEO := ("geopolymer*" OR "alkali-activated" OR "alkali activated" OR "one-part geopolymer" OR "alkali-activated material*" OR "alkali-activated binder*")`

### Scopus (TITLE-ABS-KEY syntax)

- **A (Core):** `TITLE-ABS-KEY(("geopolymer*" OR "alkali-activated" OR "alkali activated") AND ("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network*" OR "data-driven"))` — with `DOCTYPE(ar OR re)`, `PUBYEAR > 2011`, `LANGUAGE(english)`
- **B (Trust):** `TITLE-ABS-KEY(("geopolymer*" OR "alkali-activated") AND ("explainable" OR "XAI" OR "interpretab*" OR "SHAP" OR "uncertainty quantification" OR "calibrat*" OR "robustness" OR "reproducib*"))`
- **C (Physics):** `TITLE-ABS-KEY(("geopolymer*" OR "alkali-activated" OR "cementitious") AND ("physics-informed" OR "physics-guided" OR "chemistry-informed" OR "knowledge-guided" OR "scientific machine learning" OR "thermodynamic* AND machine learning" OR "hybrid mechanistic"))`
- **D (Design):** `TITLE-ABS-KEY(("geopolymer*" OR "alkali-activated" OR "low-carbon binder*") AND ("inverse design" OR "multi-objective optimi*" OR "Bayesian optimi*" OR "active learning" OR "materials informatics" OR "generative"))`
- **E (Sustainability):** `TITLE-ABS-KEY(("geopolymer*" OR "alkali-activated" OR "low-carbon binder*") AND ("machine learning" OR "artificial intelligence") AND ("carbon" OR "CO2" OR "sustainab*" OR "life cycle" OR "embodied carbon" OR "mineraliz*" OR "valoriz*"))`
- **F (Autonomy — Context Corpus):** `TITLE-ABS-KEY(("materials discovery" OR "geopolymer*" OR "cement*" OR "construction material*") AND ("AI agent*" OR "agentic" OR "autonomous laborator*" OR "self-driving laborator*" OR "closed-loop experiment*" OR "digital twin"))` — geopolymer/cement hits → Core screening; general-materials hits → Context Corpus.

### Web of Science
Same families with `TS=(...)` syntax, `DT=(Article OR Review)`, same window/language.

### ScienceDirect (simplified boolean, title-abs-keyword field)
Families A and E run verbatim minus wildcards (platform limitation noted); results cross-checked against Scopus export to catch platform-specific misses.

### SpringerLink
Family A and E keyword searches; plus a dedicated within-journal sweep of CTEP (journal 10098) for "geopolymer", "alkali-activated", "machine learning" to anchor journal-context citations.

### IEEE Xplore
Family F only: `("geopolymer" OR "cement") AND ("machine learning" OR "autonomous" OR "agent")`. Expected yield low (Stage 1: 13 items, all conference — conference items go to Context Corpus only, per EC4 below).

## 5. Eligibility Criteria

| ID | Type | Criterion | Rationale |
|---|---|---|---|
| IC1 | Inclusion | Peer-reviewed journal article (research or review) published (incl. online-first with DOI) between 2012-01-01 and search date | Quality floor; matches "published only" policy |
| IC2 | Inclusion | Material scope: geopolymer, alkali-activated material/binder/concrete/mortar/paste, one-part systems, geopolymer-stabilized soils | Direct alignment with survey scope |
| IC3 | Inclusion | Applies or evaluates an AI/ML method (prediction, XAI, UQ, optimization, inverse design, active learning, surrogate, agentic/autonomous) on the IC2 material — not merely "future work" mentions | Core Corpus definition |
| IC4 | Inclusion | English language | Screening feasibility; standard SR practice; noted as limitation |
| IC5 | Inclusion (Context only) | Reviews of AI×geopolymer/concrete; adjacent-materials autonomy/physics-informed evidence | Feeds competitor matrix + evidence map without inflating PRISMA counts |
| EC1 | Exclusion | Preprints, theses, book chapters without peer review, editorials, letters, retracted items | Published-only policy; verifiability |
| EC2 | Exclusion | OPC/conventional concrete studies without a geopolymer/AAM dataset or model | Material scope discipline |
| EC3 | Exclusion | Statistical-only studies (plain regression without ML claim) unless used as declared baseline in an ML study | Boundary of "AI"; prevents corpus dilution |
| EC4 | Exclusion (from Core) | Conference papers | Peer-review depth varies; Nguyen et al. precedent; IEEE items → Context only |
| EC5 | Exclusion | ML on geopolymers for non-construction functions (catalysis, adsorbents, dyes) unless environmental function is construction-relevant (e.g., CO₂ capture composites — flagged subset) | Keeps clean-technology construction focus; CO₂-capture subset retained because it serves Pillar 5 |
| EC6 | Exclusion | Duplicate publications / substantially overlapping datasets by same group (keep most complete; link others) | Prevents double counting in synthesis |
| EC7 | Exclusion (amendment, 21 Aug 2026) | Venue not indexed in Scopus or Web of Science at screening date | Quality floor; adopted during adjudication (Author-1 tiebreak, applied to 3 records); disclosed as a protocol amendment per PRISMA 2020 item 24b |

## 6. Screening Process

1. Export all records (RIS/CSV) → dedup by DOI, then fuzzy title match (recorded counts).
2. **Title/abstract screening** against IC/EC; decision log kept per record (include / exclude+reason / unsure→full text).
3. **Full-text assessment** for survivors; exclusion reasons coded (EC1–EC6 + "full text unavailable" — flagged, not silently dropped).
4. **Snowballing:** backward (references of included studies + Tier-1 reviews) and forward (citations via Scopus/WoS) — one full cycle.
5. **Dual-screening design (updated 10 Aug 2026):** the primary screener (Author 1, methods lead) screens 100% of records with logged decisions and reason codes. Two co-author verifiers — **Author 2 (Bhardwaj/Chaggar)** and **Author 3 (Amritphale)** — then independently second-screen the corpus, split half each (~447 records apiece), blind to the primary decisions. This achieves **100% dual coverage**. Inter-rater agreement (Cohen's kappa) is computed per verifier and reported in the methods. Disagreements are resolved by three-way discussion with Author 1 as tiebreaker; any criterion found ambiguous is sharpened and the affected slice re-screened. Fallback if verifier time is constrained: each verifier covers an independent 20% random sample (≈360 records total dual-screened, still exceeding the original single-sample design), with kappa-triggered expansion if agreement < 0.7.

## 7. PRISMA 2020 Flow (placeholders — never invented)

```
Identification:  Scopus [n=___]  WoS [n=___]  ScienceDirect [n=___]
                 SpringerLink [n=___]  IEEE Xplore [n=___]
                 Total records [n=___] → Duplicates removed [n=___]
Screening:       Title/abstract screened [n=___] → Excluded [n=___]
Eligibility:     Full texts assessed [n=___] → Excluded [n=___]
                 (reasons: EC1 [n=_], EC2 [n=_], EC3 [n=_], EC4 [n=_], EC5 [n=_], EC6 [n=_], unavailable [n=_])
Included:        Snowballing additions [n=___]
                 CORE CORPUS: primary studies [n=___]; prior reviews → Context [n=___]
```

All counts populated only from actual Stage 3 execution. No count will ever be estimated.

## 8. Study-Quality Assessment Framework

Each Core Corpus primary study is rated on the 16 items of master-prompt §21, grouped into five domains. Each item scored **0 / 0.5 / 1** (absent / partial / adequately reported) with written anchor definitions (below). Domain profiles are reported; **no single composite number is used for ranking**, because equal weighting across heterogeneous items cannot be methodologically justified (this reasoning stated in the manuscript). Instead studies are profiled (e.g., "high modeling rigor / no environmental relevance").

| Domain | Items (§21) | Example anchors for score = 1 |
|---|---|---|
| Problem & materials | 1 clear RQ; 2 material description | Precursor source + oxide composition + activator chemistry reported |
| Data | 3 dataset quality; 4 sample size; 5 feature transparency; 6 preprocessing transparency | Provenance stated; n reported; full feature list; preprocessing reproducible |
| Validation | 7 train/test separation; 8 CV quality; 9 external validation; 10 baseline comparison | Held-out test never touched in tuning; independent lab/dataset test; non-ML baseline |
| Trust | 11 uncertainty; 12 interpretability; 13 physical plausibility | UQ with method named; XAI beyond a single SHAP plot; predictions checked against chemistry |
| Openness & relevance | 14 reproducibility; 15 code/data availability; 16 environmental relevance | Artifact linked and resolvable; explicit environmental objective/quantification |

Items 11–14 simultaneously feed the **Trustworthy-AI Scorecard** (§26 of master prompt: explainability, uncertainty, calibration, robustness, OOD, external validation, physical consistency, reproducibility — each Yes/Partial/No per study).

## 9. Data Extraction Template

One row per Core study; machine-readable (CSV) — this file is the planned open research artifact. Columns:

- **Bibliographic:** authors; year; title; journal; DOI; country/institution
- **Material:** class; precursor(s); precursor origin (waste stream); oxide composition reported (Y/N); activator + concentration; liquid/solid ratio; additives; curing condition/temperature; age(s); mix-proportion completeness
- **Dataset:** n; #features; targets; experimental vs compiled; public/private; source (own lab / prior papers — which); missing-value handling; preprocessing; normalization; feature engineering
- **AI:** algorithm(s); hyperparameters reported (Y/N); optimization method; feature selection; ensemble strategy; training methodology; CV scheme; train/test split
- **Trustworthiness:** XAI (method); UQ (method); calibration; robustness test; external validation; OOD evaluation; physical constraints; sensitivity analysis
- **Sustainability:** carbon objective; energy objective; waste-utilization objective; LCA (standard? boundaries?); cost; CO₂ uptake; circularity; quantitative comparison vs OPC
- **Reproducibility:** dataset available; code available; hyperparameters reported; preprocessing reproducible; implementation reproducible
- **Codes (Section 10):** physics-integration Type; evidence level; AI-task class; deployment-maturity stage

## 10. Evidence Coding Schemes (fixed before extraction)

1. **Three-level evidence grade:** `G` demonstrated in geopolymers/AAMs · `A` demonstrated only in adjacent materials (Context Corpus) · `P` prospective (no published demonstration). Every capability claim in the manuscript carries a grade.
2. **Physics/chemistry integration (master-prompt §27):** Type I purely data-driven · II domain variables as ordinary features · III domain-guided model design · IV physics/chemistry-constrained learning · V hybrid mechanistic+ML. Conservative assignment: ambiguity resolves downward (e.g., Si/Al as plain input = Type II, never III).
3. **AI task:** prediction / classification / feature analysis / optimization / surrogate / inverse design / UQ / experiment selection / experiment planning / autonomous experimentation.
4. **Deployment maturity (Axis 6):** lab prediction → externally validated model → formulation recommendation → process optimization → pilot implementation → digital-twin integration → adaptive experimentation → semi-autonomous → autonomous.
5. **Invalid-comparison rule (§24):** cross-study numerical comparisons (R², RMSE) are reported only with dataset/split/metric context; where protocols differ, the manuscript states: *"Direct cross-study numerical comparison is not scientifically defensible because experimental and validation protocols differ."* Benchmark-audit table (§23 schema: Dataset / Material / N / Features / Target / Algorithms / Validation / Public? / External test? / Key limitation) tracks dataset reuse and leakage across studies.

## 11. Known Protocol Limitations (disclosed up front)

- English-only; journal-articles-only (conference and preprint exclusion may lag fastest-moving autonomy work — mitigated by Context Corpus).
- Screening primarily single-team with 20% double-pass, not fully independent dual review.
- Database access levels (Scopus/WoS institutional access) to be confirmed at Stage 3 kickoff; if unavailable, fallback = ScienceDirect + SpringerLink + Crossref + documented Google Scholar supplement, with the substitution disclosed.

---

*Stage 2 complete. STOP per protocol. Stage 3 (search execution, screening, extraction) awaits approval — note Stage 3 is the labor-intensive stage and requires database access decisions above.*
