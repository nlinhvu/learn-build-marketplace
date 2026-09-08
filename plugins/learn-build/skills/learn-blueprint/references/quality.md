# Product-specific quality profile

Translate “enterprise” and “big tech practices” into verifiable requirements based on workload, threat model, data sensitivity, budget, and operating capacity. Introduce a complex pattern only when it addresses a specific driver.

| Concern | What to learn and design when relevant | Typical evidence |
|---|---|---|
| System/design patterns | Domain/module boundaries, cohesion/coupling, contracts, data ownership, concurrency | Source-based explanation and impact of a requirement change |
| Correctness/data | Consistency, transactions, idempotency, schema evolution, retention | Failure/crash scenarios, actual state, migration rehearsal |
| Security/privacy | Trust boundaries, identity, least privilege, secrets, tenant isolation, audit | Negative paths checking enforcement, logs/traces appropriate to the data |
| CI/CD/developer workflow | Reproducible builds, meaningful tests/checks, artifact promotion, release/rollback | Pipeline/artifacts traceable to source, release rehearsal |
| Infrastructure/DevOps | IaC, parity, networking, configuration, drift, resource lifecycle | Environment recreation, diff/drift, smoke checks and cleanup |
| Reliability/observability | User journeys, SLI/SLO, timeout/retry/backpressure, logs/metrics/traces | Measured signals, failure diagnosis, recovery/rollback drills |
| Supply chain | Dependency/artifact integrity, provenance, patching, licenses/SBOM when needed | Source → build → artifact and applicable verification |
| Performance/cost | Workload, bounds, bottlenecks, storage/egress/idle costs | Benchmarks with environment context, estimates with assumptions/sources |
| Operations/governance | Owners, incidents/runbooks, backup/restore, RTO/RPO, domain obligations | Executed runbooks/restores, residual risks, release gates |

For each relevant concern, connect requirement → control/design → tutorial/milestone → source/IaC/pipeline → evidence → operations. Give a short reason for concerns that do not apply yet. Controls required before a boundary or exposure must appear as soon as the capability reaches that boundary. Do not reserve security and CI/CD for a final phase.

Greenfield work often needs a walking skeleton and build/run feedback. Existing repositories start with a real capability or operational gap. Include only relevant layers; do not force a UI or database onto a CLI/library. A local demo alone does not establish production readiness.

When a capability crosses a new boundary, such as local → shared, temporary → durable data, or manual run → release, identify requirements and controls now due. Include a manual walkthrough of enforcement, failure/recovery, and appropriate cost/cleanup checks. Trace controls to actual code/configuration/IaC/pipelines and observed behavior in an authorized environment. If access or the environment is unavailable, mark it unverified and keep dependent exposure pending. Separate preparation/learning from exposure when needed to keep tutorials manageable, but never defer a required control until after exposure. Do not provision or deploy outside assigned scope merely to fill an evidence gap.

When choosing a basis, consult appropriate current sources: Google SRE for SLO/reliability, DORA for delivery, OWASP ASVS for applicable application surfaces, and SLSA for supply chains. Record versions/controls for specific claims. Do not assert certification/compliance or prescribe the same SLO, RTO/RPO, scale, or cloud service for every product.

User ownership develops through explaining/predicting, debugging/changing, and operating/recovering real code. Teach enough mechanism to support the next decision. Do not infer understanding from agent QA, passing tests, or silence. A suitable discussion or practical exercise is more useful than an “understood” checkbox.
