# Research Thread 5 — Technical Feasibility

**Agent:** general-purpose subagent | **Run:** 2026-09-29 | **Items covered:** 6, 7, 8, 9 (per `research/Research_Plan.md`)

## Prompt given

> You are researching for a fictitious-company business assignment. The company's claimed technical architecture: a JEPA-style (Joint Embedding Predictive Architecture) self-supervised world model trained on satellite fleet telemetry, a constrained RL rollout planner trained inside that world model, an LLM agent for reading security advisories, and federated learning across satellite operators (raw telemetry never leaves the operator). Use WebSearch/WebFetch. This is a business-school assignment, not an engineering build — the goal is to find enough real research to make the technical moat argument credible and identify real limitations to acknowledge, not to design the system.
>
> Research items 6, 7, 8, 9 from the project's research/Research_Plan.md:
>
> 6. Confirm the operational analogue exists: does NIST IR 8270 or ESA's on-board software maintenance documentation describe a real multi-step process resembling "ingest advisory → map to component → score → validate → schedule patch window → uplink → monitor → rollback"? Pull specifics.
>
> 7. Is there enough public satellite telemetry data to plausibly bootstrap a JEPA-style world model from cold start? Look at: the ESA-ADB (ESA Anomaly Detection Benchmark) dataset, the OPS-SAT telemetry dataset/benchmark, and any paper discussing how much time-series data JEPA-style models typically need (e.g. MTS-JEPA paper, V-JEPA). Give a realistic verdict: is public data alone sufficient, or does it genuinely require design-partner data too?
>
> 8. Federated learning across heterogeneous clients (in this case, very different satellite platforms/fleets) — does naive parameter averaging (FedAvg) break down with high heterogeneity? What's the standard fix in the literature (e.g. FedProx, personalization layers/adapters, clustered federated learning)? This doesn't need to be satellite-specific — general federated learning heterogeneity literature is fine, just say so.
>
> 9. What's the realistic computational/practical overhead of differential privacy (DP-SGD) or secure aggregation on top of federated learning? Is this considered practical at moderate data volumes and moderate client counts (dozens, not millions), or is it still a research-stage cost?
>
> Return a clean markdown section, one subsection per item, each with: Finding / Source URL / whether it's satellite-specific or general-ML literature applied by analogy / any real limitation or caveat that should be acknowledged honestly in the business plan (e.g. cold-start risk, JEPA explainability, heterogeneity risk). Do not write files — return markdown in your final message.

## Approach followed

Searched for the operational-process claim against NIST IR 8270 and ESA's on-board software maintenance concept documents specifically (rather than accepting the claimed 8-step pipeline at face value), for satellite telemetry dataset papers (ESA-ADB, OPS-SAT-AD) cross-referenced against JEPA data-scale reference points (V-JEPA 2, MTS-JEPA), and for general federated-learning/differential-privacy literature applied by analogy to the satellite-fleet heterogeneity problem. Every finding was explicitly labeled satellite-specific vs. general-ML-literature-applied-by-analogy, and real limitations (no documented automated rollback, JEPA explainability, DP's privacy-utility trade-off) were surfaced rather than smoothed over.

## Sources visited

- https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8270.pdf
- https://csrc.nist.gov/pubs/ir/8270/final
- https://csrc.nist.gov/pubs/ir/8401/final
- https://www.esa.int/esapub/bulletin/bullet91/b91deni.htm
- https://www.researchgate.net/publication/258389277_On-Board_Software_Maintenance_for_GOCE_ESA's_Gravity_Mission
- https://www.researchgate.net/publication/280114386_Adaptive_On-board_Software_Maintenance_the_GOCE_Mission_Recovery_Cases
- https://arxiv.org/abs/2406.17826
- https://github.com/kplabs-pl/ESA-ADB
- https://github.com/esa/anomaly-dataset
- https://www.nature.com/articles/s41597-025-05035-3
- https://arxiv.org/abs/2407.04730
- https://arxiv.org/abs/2506.09985
- https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
- https://arxiv.org/html/2602.04643v1
- https://www.researchgate.net/publication/370658529_ON_THE_CONVERGENCE_OF_FEDAVG_ON_NON-IID_DATA
- https://arxiv.org/pdf/1812.06127
- https://proceedings.mlsys.org/paper_files/paper/2020/file/1f5fe83998a09396ebe6477d9475ba0c-Paper.pdf
- https://github.com/marswhu/HFL_Survey
- https://arxiv.org/pdf/2403.16460
- https://link.springer.com/article/10.1007/s11042-026-21541-x
- https://dl.acm.org/doi/10.1145/3133956.3133982
- https://arxiv.org/pdf/2303.00654
- https://pytorch.org/blog/clipping-in-opacus/
- https://arxiv.org/pdf/2201.12328
- https://arxiv.org/pdf/2607.28191
- https://proceedings.mlr.press/v162/chen22c/chen22c.pdf

## Full output

## Research Items 6–9: Findings

### 6. Operational analogue for "ingest advisory → map to component → score → validate → schedule → uplink → monitor → rollback"

**Finding:** Neither NIST IR 8270 nor NIST IR 8401 narrates the workflow as a single named pipeline the way the business plan phrases it, but the pieces of it are all real, documented, separately-sourced operational practices — the pipeline is a reasonable *synthesis*, not an invented process.

- **NIST IR 8270** (*Introduction to Cybersecurity for Commercial Satellite Operations*, final, July 2023) maps satellite cybersecurity outcomes to NIST SP 800-53 controls via the CSF. Directly relevant crosswalk entries pulled from the actual PDF text:
  - `ID.RA-1` "Asset vulnerabilities are identified and documented" → SP 800-53 CA-2, CA-7, CA-8, RA-3, RA-5, SA-5, SA-11, SI-2, SI-4, SI-5 (this is the "ingest/map" step).
  - `ID.RA-2` "Cyber threat intelligence is received from information-sharing forums and sources" (this is literally the advisory-ingestion step — receiving external advisories).
  - `PR.IP-12` "A vulnerability management plan is developed and implemented" → RA-1, RA-3, RA-5, SI-2 (SI-2 is NIST's "Flaw Remediation"/patch-management control family — this is the "score → schedule → patch" step).
  - Body text explicitly states: "software on a space vehicle can often be patched or modified from the ground" (p.472-473), and lists response/recovery plans (`PR.IP-9`) as a required control for when communications/systems are compromised.
  - The document does **not** spell out an automated scoring/prioritization algorithm or an explicit rollback procedure — those are gaps, not present in the source.
- **NIST IR 8401** (*Satellite Ground Segment: Applying the Cybersecurity Framework to Assure Satellite Command and Control*, Dec 2022) extends this to ground-segment supply-chain risk management (assessing suppliers/third parties, audits, response and recovery planning) but again as a controls profile, not a step-by-step runbook.
- **ESA's On-Board Software Maintenance (OBSM) concept** (documented for Cluster and GOCE missions) is the closest real match to the full pipeline, and it is a genuinely multi-step ground process:
  1. Need identified (post-launch anomaly or planned adaptation) → new code/patch written in a Software Development Environment.
  2. **Validated** on the Software Development and Validation Facility (SdeVF, an emulated target processor) and then at system level on a full spacecraft simulator (SimVF) before anything is sent.
  3. Patch is generated as a **delta**: the new memory image is diffed against the tracked on-board memory state, and only the differences are converted into memory-patch telecommands.
  4. **Uplinked** as those telecommands.
  5. Ground continuously tracks on-board configuration state ("the on-board configuration of each of the four spacecraft must always be known by the ground so that it could be reconstructed at any time if needed") — this is the monitoring/traceability step.
  6. **No explicit rollback procedure is described** in the available ESA sources (Cluster OBSM bulletin, GOCE OBSM papers) — configuration is tracked so a prior state *could* be reconstructed, but a formal automated rollback step is not documented.

**Satellite-specific.** Both NIST docs are satellite/space-specific; ESA OBSM is satellite-specific and operationally real (not hypothetical — used on Cluster and GOCE).

**Caveat to state honestly:** The full 8-step pipeline as phrased ("ingest → map → score → validate → schedule → uplink → monitor → rollback") is a plausible *composite* of real practices from two different sources (NIST controls framework + ESA OBSM operations), not a single documented end-to-end process anywhere. Automated scoring/prioritization and rollback are the weakest-evidenced steps — real practice appears to rely on human judgment and configuration-tracking rather than automated rollback.

Sources: [NIST.IR.8270 PDF](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8270.pdf) · [NIST IR 8270 CSRC page](https://csrc.nist.gov/pubs/ir/8270/final) · [NIST IR 8401 CSRC page](https://csrc.nist.gov/pubs/ir/8401/final) · [The Cluster On-Board Software Maintenance Concept, ESA Bulletin 91](https://www.esa.int/esapub/bulletin/bullet91/b91deni.htm) · [On-Board Software Maintenance for GOCE (ResearchGate)](https://www.researchgate.net/publication/258389277_On-Board_Software_Maintenance_for_GOCE_ESA's_Gravity_Mission) · [Adaptive On-board Software Maintenance: the GOCE Mission Recovery Cases](https://www.researchgate.net/publication/280114386_Adaptive_On-board_Software_Maintenance_the_GOCE_Mission_Recovery_Cases)

---

### 7. Is public satellite telemetry data enough to bootstrap a JEPA-style world model from cold start?

**Finding — realistic verdict: public data alone is not sufficient; design-partner (proprietary fleet) data is genuinely required.**

- **ESA-ADB** (European Space Agency Benchmark for Anomaly Detection in Satellite Telemetry, Kotowski et al., 2024): first large-scale, real, curated multivariate satellite telemetry dataset. ~17.5 years of telemetry across **3 ESA missions**, 844 annotated events (148 anomalies). Built by Airbus DS + KP Labs + ESA over an 18-month funded project — i.e., even the *benchmark-construction* itself needed a dedicated multi-institution engineering effort to curate.
- **OPS-SAT-AD** (OPS-SAT benchmark, Nature Scientific Data 2025): telemetry from a single CubeSat mission (OPS-SAT). Only **2,123 short univariate fragments across 9 channels**, ~20% anomalous. This is a small, single-platform, univariate-heavy dataset — nowhere near the scale or channel diversity (multi-sensor, multi-bus, multi-platform) a fleet-wide world model would need.
- Both public satellite datasets combined are: (a) small by deep-learning standards, (b) drawn from only a handful of missions/platforms (3 ESA missions + 1 CubeSat), (c) oriented toward *anomaly detection/classification*, not the dense, continuous, multi-sensor state trajectories JEPA-style predictive world models are trained on.
- **JEPA data-scale reference points:**
  - **V-JEPA 2** (Meta, 2025): pretrained on **>1 million hours of video** (VideoMix22M, >1M hours + 1M images) to learn a general world model. Even the much smaller **action-conditioned fine-tuning stage** (V-JEPA 2-AC) needed **62 hours of unlabeled robot video** just to adapt the pretrained model to a narrow downstream task — and that's fine-tuning an already-pretrained foundation model, not training from scratch.
  - **MTS-JEPA** (Feb 2026, multivariate time-series anomaly prediction JEPA): validated on standard time-series anomaly benchmarks (MSL, SMAP, SWaT, PSM) — these are the same order of magnitude/genre as ESA-ADB/OPS-SAT (small, curated, anomaly-labeled), suggesting JEPA *can* be applied to satellite-scale time series, but at that data scale the published results are for downstream anomaly-prediction tasks, not demonstrations of learning a broad, generalizable "world model" of satellite behavior from cold start.

**Verdict for the business plan:** Public data (ESA-ADB + OPS-SAT-AD) is enough to prototype, benchmark, and demonstrate a JEPA-style architecture works on satellite telemetry (analogous to MTS-JEPA's use of small labeled benchmarks). It is **not** enough, by scale or platform diversity, to bootstrap a broad, fleet-general self-supervised world model the way V-JEPA needed internet-scale video. The credible claim is: public data de-risks the architecture choice and enables early prototyping; a real deployable world model requires ongoing proprietary telemetry from design-partner operators — this is a legitimate "why federation/data partnerships matter" argument, not just an assumption.

**General-ML-literature-applied-by-analogy:** the V-JEPA/MTS-JEPA data-scale reasoning is general ML literature (video/generic time-series), applied by analogy to the satellite domain — flag this explicitly in the plan.

**Caveat to state honestly:** cold-start risk is real; JEPA's explainability is also a known open issue (predictive latent-space models are harder to interpret/audit than forecast-based approaches) — worth a one-line acknowledgment alongside the data-scale caveat.

Sources: [European Space Agency Benchmark for Anomaly Detection in Satellite Telemetry (arXiv)](https://arxiv.org/abs/2406.17826) · [ESA-ADB GitHub](https://github.com/kplabs-pl/ESA-ADB) · [ESA anomaly-dataset GitHub](https://github.com/esa/anomaly-dataset) · [The OPS-SAT benchmark for detecting anomalies in satellite telemetry (Nature Scientific Data)](https://www.nature.com/articles/s41597-025-05035-3) · [OPS-SAT-AD arXiv](https://arxiv.org/abs/2407.04730) · [V-JEPA 2 arXiv](https://arxiv.org/abs/2506.09985) · [Introducing V-JEPA 2 world model (Meta AI blog)](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/) · [MTS-JEPA arXiv](https://arxiv.org/html/2602.04643v1)

---

### 8. Does FedAvg break down under high client heterogeneity, and what's the standard fix?

**Finding — yes, confirmed, and this is general (non-satellite-specific) federated-learning literature applied by analogy.**

- Standard **FedAvg** is known to suffer "client drift": under non-IID (statistically heterogeneous) data across clients, multiple local SGD steps pull each client's model toward its own local optimum; naive averaging fails to correct this, causing slower convergence, oscillation, or outright divergence. This is shown both empirically and theoretically (Li et al., "On the Convergence of FedAvg on Non-IID Data").
- **Standard fix #1 — FedProx** (Li, Sahu, Talwalkar, Smith, MLSys 2020, "Federated Optimization in Heterogeneous Networks"): adds a proximal term to the local objective that penalizes local models for drifting too far from the global model, and explicitly allows variable amounts of local work per device (handles both statistical *and* systems heterogeneity — directly relevant to "very different satellite platforms" with different compute/comms budgets). Provides convergence guarantees under non-identical client distributions.
- **Standard fix #2 — personalization layers / adapters**: a well-established family of methods keeps shallow/general layers shared and globally aggregated (capturing transferable features) while deeper or head layers stay client-specific/local, balancing global generalization with per-client personalization. This maps naturally onto "shared physics-like backbone, per-fleet/per-platform adapter heads."
- **Standard fix #3 — clustered federated learning**: groups clients by similarity (e.g., FedAC) and trains separate models per cluster rather than one global model — useful when heterogeneity is too extreme for a single shared model to be meaningful, at the cost of higher communication (naive cluster-identification costs scale ~O(K×d), K× vanilla FL communication).

**General-ML-literature applied by analogy** — none of this is satellite-specific; it's standard federated learning heterogeneity literature (FedProx, personalization/adapter surveys, clustered FL surveys), applied here to "different satellite platforms/fleets" as the heterogeneity source. State this explicitly in the plan.

**Caveat to state honestly:** picking the right fix (FedProx vs. personalization vs. clustering) is itself a design/tuning problem with real trade-offs (clustering adds material communication overhead; personalization requires deciding which layers are "general" vs "platform-specific" and that's an empirical, not obvious, split for satellite telemetry). This is a solvable, well-studied problem, not a novel research risk — the moat argument should present it as "known techniques, applied," not as something invented in-house.

Sources: [On the Convergence of FedAvg on Non-IID Data](https://www.researchgate.net/publication/370658529_ON_THE_CONVERGENCE_OF_FEDAVG_ON_NON-IID_DATA) · [Federated Optimization in Heterogeneous Networks (FedProx, arXiv)](https://arxiv.org/pdf/1812.06127) · [FedProx MLSys proceedings PDF](https://proceedings.mlsys.org/paper_files/paper/2020/file/1f5fe83998a09396ebe6477d9475ba0c-Paper.pdf) · [Heterogeneous Federated Learning survey (GitHub)](https://github.com/marswhu/HFL_Survey) · [FedAC: Adaptive Clustered Federated Learning](https://arxiv.org/pdf/2403.16460) · [A Systematic Survey on Clustering in Federated Learning](https://link.springer.com/article/10.1007/s11042-026-21541-x)

---

### 9. Practical overhead of DP-SGD / secure aggregation at moderate scale (dozens of clients)

**Finding — both are practical today at moderate scale (dozens of clients), with a real but bounded cost; this is general federated-learning/privacy literature, not satellite-specific.**

- **DP-SGD compute overhead:** A naive per-example-gradient implementation can be extremely slow (historically 10–100x slowdown reported with early TensorFlow Privacy implementations, worst case ~70x). However, modern efficient implementations have closed this gap substantially:
  - **Opacus** (PyTorch's DP library): ~1.95x slowdown on MNIST, ~2.64x on CIFAR-10.
  - JAX implementations using `vmap`-style primitives: as low as **~1.25–1.5x slowdown** vs. non-private training.
  - So DP-SGD today is a real but bounded (roughly 1.5–3x) compute tax, not a research-stage blocker, for models of the scale this project would realistically train.
- **DP privacy-utility trade-off (separate from compute cost):** DP-SGD causes real accuracy degradation, especially pronounced on non-IID or small per-client datasets — directly relevant here since satellite operators are exactly the "few clients, heterogeneous, possibly small local datasets" regime where DP hurts utility most. This is a real caveat, not just a compute-cost caveat.
- **Secure aggregation (SecAgg) overhead:** Bonawitz et al.'s original "Practical Secure Aggregation" protocol (ACM CCS 2017) — the foundational reference — demonstrated low runtime/communication overhead even at much larger scale than "dozens of clients" (e.g., ~1.73x communication expansion for 2^10 ≈ 1000 users with 2^20-dim vectors; ~1.98x for 2^14 ≈ 16,000 users). At dozens of clients (well below the regime the protocol was stress-tested at), overhead is expected to be smaller still. More recent protocols report per-round client communication cost that stays roughly constant regardless of client count, and some report overhead reduced to ~1.25% of earlier approaches, with active-adversary-security variants adding only ~1.005–1.013x over semi-honest baselines.

**Verdict for the business plan:** At "dozens of clients / moderate data volumes" — i.e., exactly this project's realistic operator-consortium scale — both DP-SGD and secure aggregation are **practical, not research-stage**, for the compute/communication overhead itself. The genuine open risk is the **privacy-utility trade-off of DP** (accuracy loss under small/heterogeneous per-operator datasets), which is a modeling risk, not an infrastructure-cost risk, and should be acknowledged as such rather than papered over.

**General-ML-literature applied by analogy** — none of these sources are satellite-specific; they are general federated-learning/DP infrastructure literature. State this explicitly in the plan.

Sources: [Practical Secure Aggregation for Privacy-Preserving Machine Learning (Bonawitz et al., ACM CCS 2017)](https://dl.acm.org/doi/10.1145/3133956.3133982) · [How to DP-fy ML: A Practical Guide to Machine Learning with Differential Privacy](https://arxiv.org/pdf/2303.00654) · [Enabling Fast Gradient Clipping and Ghost Clipping in Opacus (PyTorch blog)](https://pytorch.org/blog/clipping-in-opacus/) · [Toward Training at ImageNet Scale with Differential Privacy](https://arxiv.org/pdf/2201.12328) · [Secure Aggregation for Privacy-Preserving Federated Learning on Clinical EEG Data (10/40/70-client benchmark)](https://arxiv.org/pdf/2607.28191) · [The Fundamental Price of Secure Aggregation in Differentially Private Federated Learning](https://proceedings.mlr.press/v162/chen22c/chen22c.pdf)

---

**Overall note for the report:** Item 6 has a genuine satellite-specific operational analogue (NIST IR 8270/8401 controls crosswalk + ESA OBSM process), but the full 8-step pipeline as phrased is a composite/synthesis, not a single documented process — say so. Item 7's verdict is "public data de-risks the architecture but does not remove the need for design-partner data" — a defensible, honest moat argument. Items 8 and 9 are both real, well-established general ML/federated-learning literature applied to this domain by analogy; both should be labeled as such rather than presented as satellite-specific findings.
