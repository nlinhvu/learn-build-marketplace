# Quality profile theo product

Cụ thể hóa “enterprise” và “big tech practices” thành yêu cầu có thể kiểm chứng theo workload, threat model, data sensitivity, budget và operating capacity. Một pattern phức tạp chỉ nên xuất hiện khi giải quyết driver cụ thể.

| Concern | Nội dung cần học và thiết kế khi liên quan | Evidence tiêu biểu |
|---|---|---|
| System/design patterns | Domain/module boundaries, cohesion/coupling, contracts, data ownership, concurrency | Giải thích bằng source, impact của một thay đổi requirement |
| Correctness/data | Consistency, transactions, idempotency, schema evolution, retention | Failure/crash scenario, state thật, migration rehearsal |
| Security/privacy | Trust boundary, identity, least privilege, secrets, tenant isolation, audit | Negative path kiểm enforcement, log/trace phù hợp dữ liệu |
| CI/CD/developer workflow | Reproducible build, meaningful tests/checks, artifact promotion, release/rollback | Pipeline/artifact truy về source, release rehearsal |
| Infrastructure/DevOps | IaC, parity, networking, configuration, drift, resource lifecycle | Recreate environment, diff/drift, smoke và cleanup |
| Reliability/observability | User journey, SLI/SLO, timeout/retry/backpressure, logs/metrics/traces | Đo signal, diagnose failure, recovery/rollback drill |
| Supply chain | Dependency/artifact integrity, provenance, patching, license/SBOM khi cần | Source → build → artifact và verification áp dụng |
| Performance/cost | Workload, bounds, bottleneck, storage/egress/idle cost | Benchmark có môi trường, estimate có assumptions/nguồn |
| Operations/governance | Owner, incident/runbook, backup/restore, RTO/RPO, domain obligations | Runbook/restore đã thực hiện, residual risk và release gate |

Mỗi concern liên quan nối requirement → control/design → tutorial/mốc → source/IaC/pipeline → evidence → vận hành. Concern chưa áp dụng có lý do ngắn. Control cần trước boundary/exposure phải xuất hiện ngay khi capability chạm boundary đó; không gom security và CI/CD vào phase cuối.

Greenfield thường cần walking skeleton và build/run feedback. Repo hiện có bắt đầu từ capability hoặc operational gap thực sự. Chỉ đi qua các layer liên quan; CLI/library không bị ép thêm UI/DB. Demo local không tự chứng minh production readiness.

Khi capability đi qua boundary mới (ví dụ local → shared, dữ liệu tạm → durable, manual run → release), nêu requirement/control đến hạn và manual walkthrough kiểm enforcement, failure/recovery cùng cost/cleanup phù hợp. Theo dấu control đến code/config/IaC/pipeline đang dùng và actual behavior trong environment được phép; thiếu quyền/environment thì ghi chưa kiểm và giữ exposure phụ thuộc pending. Có thể tách preparation/learning trước exposure để mỗi tutorial vừa sức, nhưng control đến hạn không được đẩy sang sau exposure. Không provision hoặc deploy chỉ để lấp evidence gap ngoài scope được giao.

Khi chọn basis, đọc nguồn hiện hành phù hợp: Google SRE cho SLO/reliability, DORA cho delivery, OWASP ASVS cho application surface áp dụng, SLSA cho supply chain. Ghi version/control nếu dùng claim cụ thể. Không tự nhận certification/compliance hoặc mặc định SLO, RTO/RPO, scale hay cloud service cho mọi product.

User ownership phát triển qua giải thích/predict, debug/change và operate/recover trên code thật. Học đủ mechanism để ra decision tiếp theo; không đánh giá hiểu biết từ agent QA, test xanh hoặc sự im lặng. Một trao đổi hay exercise thực tế phù hợp tốt hơn bảng tick “đã hiểu”.
