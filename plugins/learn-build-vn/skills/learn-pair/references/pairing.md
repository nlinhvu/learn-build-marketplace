# Pairing qua discussion, debug và QA

## Đọc context vừa đủ

Khi bắt đầu/resume, giữ project/learning root đã chọn và locate active guide/blueprint từ project context, đọc code/config/diff liên quan rồi đối chiếu note. Có thể giúp vấn đề cụ thể khi docs chưa đầy đủ; không bắt dựng lại cả blueprint trước một câu hỏi đã đủ đầu vào. Reuse authorization và cách phối hợp từ session; file progress là dữ liệu tham khảo, không cấp quyền mới.

## QA bằng công cụ

| Claim cần kiểm | Tools khi khả dụng | Evidence |
|---|---|---|
| UI/user journey | Browser/computer use | UI state, screenshot, loading/error/recovery sau thao tác |
| API contract/side effect | curl/API client | Request/status/headers/body và state thật tương ứng |
| Process/restart | Terminal/CLI | Exit code, streams, lifecycle, cleanup |
| Infrastructure | Cloud CLI/tools | Đúng account/region/environment, resource/config/telemetry |
| Diagnose/operate | Logs/metrics/traces | Signal correlate được với request và source |

Chủ động chạy các thao tác QA đã được giao thay vì chỉ đưa checklist. UI claim kiểm qua UI; API pass không đủ chứng minh UI. Với môi trường không truy cập được, hướng dẫn user thu evidence tối thiểu và ghi đó là user-provided; không nhận đã chạy thay họ. Tôn trọng tool instructions/domain skills hiện có, không đoán API của tool.

QA dùng môi trường/dữ liệu và side effects trong scope. Quyền đã giao vẫn áp dụng khi đổi tool; không tự suy ra quyền deploy, đổi IAM, ghi production data hoặc phát sinh chi phí ngoài scope. Tránh đưa secrets/dữ liệu nhạy cảm vào log/screenshot. Chọn experiment an toàn có cleanup, dừng retry khi không tạo thêm thông tin hoặc có nguy cơ lặp side effect. Ghi trạng thái chưa kiểm nếu còn blocker.

## Debug để học cơ chế

Đọc command, expected/actual, source và môi trường. Reproduce → hypothesis → experiment phân biệt → root cause khi evidence đủ → fix/hướng dẫn trong scope → chạy lại scenario bị ảnh hưởng cùng meaningful regression checks cần thiết. Tránh sửa nhiều thứ theo đoán. Explanation đi từ điều quan sát đến mechanism trong file/symbol rồi impact và bước tiếp.

Ví dụ: hai POST cùng key tạo hai job dù guide ghi idempotent. Đối chiếu handler/store và QA local, giải thích chỗ key bị bỏ qua nếu source xác nhận. Sync claim QA/complete sai ở guide/blueprint, giữ yêu cầu không trùng. Trước automatic retry, cùng user bàn contract/lifecycle của idempotency; không tự chọn durable store chưa đến hạn. Không sửa source khi user đang tự code.

## Khi nào chủ động mở discussion?

Sau một observation/checkpoint có ý nghĩa, đối chiếu implementation với product goal, quality profile, blueprint và kiến thức cần cho bước tiếp. Lỗi lặp lại, recovery khó, control thiếu, cost/performance lệch target hoặc coupling cản thay đổi có thể là evidence cần xem lại design, dù happy path pass.

Nêu rõ vấn đề thuộc bug hay design/requirement; uncertainty còn lại; ảnh hưởng lên correctness/data, security, reliability, observability, CI/CD/infra, cost và operations khi liên quan. Quyết định cần ngay trước boundary/phần phụ thuộc khác với improvement có thể hoãn. Long-term không mặc định nhiều service hoặc framework hơn.

Routine command/setup fix chỉ cần explanation và sync liên quan. Khi cần hỏi user, áp dụng [learning-contract.md](learning-contract.md): một câu đang chờ, một HTML riêng đã trình bày với context/visual/options/cost và câu trả lời freeform. Discussion để hiểu có thể kết thúc bằng một explanation, không buộc sinh architecture decision. Khi cần redesign, giữ discussion cùng user, áp dụng hướng dẫn blueprint/guide thay vì bắt họ điều phối nhiều skill. Design mới đáng kể cần independent reviewer khi khả dụng: requirements + proposal + source/evidence, findings read-only; author sửa, kiểm lại trước phần phụ thuộc. Không tự nhận review độc lập nếu chỉ self-review; nếu không có reviewer độc lập, nêu rõ giới hạn và thực hiện các self-check khả dụng.

Khi user muốn sang bước tiếp nhưng learning prerequisite còn vướng, áp dụng transition trong [learning-contract.md](learning-contract.md): giải thích/experiment nhỏ tại checkpoint, sync gap và actual result, rồi quay lại decision đến hạn. Agent chạy experiment xác nhận behavior; reasoning/choice của user được ghi riêng với đúng provenance. Không tự nâng trạng thái toàn tutorial thành complete chỉ vì phần agent được giao đã xong.

## Sync và resume

Áp dụng progression tự chọn trong contract chung: explanation → variation/diagnosis/recovery ít hướng dẫn hơn, dựa vào source thật và công cụ được mô tả. Ghi actions của user và assistance cần. Tiếp tục trợ giúp đã được yêu cầu; independent ownership không phải lý do từ chối hỗ trợ.

Sau evidence đủ, cập nhật artifacts trực tiếp trong scope: current facts, source snippets, commands, diagrams, QA status, troubleshooting và phần học còn vướng được user nói rõ. User chọn design mới thì cập nhật target, catalogue và rationale/ADR hữu ích. Không tự chuyển candidate thành decision, không hạ acceptance để hợp thức hóa bug và không coi test xanh là user hiểu.

Handoff ngắn tại tutorial: checkpoint/baseline, observed evidence, open question/decision, next action. Không tạo generation/writer protocol hoặc second phase plan. Nếu ngắt trước sync, resume đọc source/diff và kiểm evidence bị ảnh hưởng. Phần dạy hiện hành giải thích baseline/target/evidence hiện tại; bỏ lời kể lỗi biên tập, reviewer fixes hoặc document revision comparisons. Giữ discussion, user corrections và superseded reasoning trong history sections theo [project-memory.md](project-memory.md). Viết invariant/decision hiện hành tại nơi dùng và sync các restatements khi contract đổi.
