# Context dự án được lưu bền vững

Giữ toàn bộ nội dung có ý nghĩa của mỗi discussion để user và agent mới khôi phục intent, reasoning, status và next action mà không cần chat cũ. Mọi record mới là HTML phong phú theo [html.md](html.md); dùng [learning-contract.md](learning-contract.md) cho ownership, roots, authority và decisions.

## Nơi quản lý từng record

Dùng learning root đã chọn. Chỉ tạo record khi có nội dung; reuse record tương đương và path hiện có. Đọc legacy format làm evidence, không tự convert/duplicate khi chưa được giao.

| Artifact | Nội dung quản lý |
|---|---|
| `index.html` | Product snapshot, catalogue thích nghi, checkpoint hiện tại, record index |
| `discussions/NNNN-topic.html` | Lịch sử topic, gồm non-ADR decisions, explanations, câu hỏi còn mở |
| `adrs/NNNN-slug.html` | Architectural choices có giá trị lâu dài, rejected alternatives, supersession |
| `user-stories/US-NNNN-slug.html` | Actor goals, rules, acceptance, walkthroughs, kết quả quan sát |
| `decisions/NN-topic.html` | Trang dạy/so sánh phong phú của một câu hỏi và disposition |
| `tutorials/NN-topic.html` | Bài học hiện hành, code checkpoints, progress, QA, ownership evidence |
| `explainers/topic.html` | Phân tích sâu tùy chọn, bổ sung nội dung thiết yếu tại chỗ |

Skill đang trao đổi cập nhật records tương ứng. Blueprint ghi product/story intent; guide chi tiết capability hiện tại; pair ghi implementation/QA/learning thực tế. Sync summary/link mà không nhân đôi toàn history hoặc tạo checklist tiến độ cạnh tranh.

Dùng stable identifiers/anchors. Lấy số chưa dùng tiếp theo theo loại record; không tái dùng/đánh lại ID. Link records liên quan hai chiều. Khi nâng decision thành ADR, giữ nguyên discussion và trỏ ADR làm record chính thức của decision.

## Lưu ngay trong discussion

Sau mỗi exchange có nội dung thực chất, lưu thông tin mới trước câu hỏi tiếp hoặc phần phụ thuộc. Cũng lưu trước khi yield với câu hỏi mở, chuyển skill hay kết phiên. Cập nhật topic hiện có, không tạo report mỗi message; design chưa xong và nội dung chưa thành decision vẫn cần record.

Giữ mọi requirement, constraint, glossary definition, user statement/correction, story/edge case, option/trade-off, selection/rejection/deferral cùng lý do, objection, explanation/worked trace, assumption, experiment/evidence và giới hạn, learning need, câu hỏi còn mở. Gộp wording trùng mà không mất nghĩa. Trích nguyên lời user khi nó định nghĩa contract. Không bịa transcript, approval, alternative, history thiếu hay learning evidence; không lưu secrets/dữ liệu cá nhân không cần thiết.

Giữ nội dung phong phú đã phát triển trong discussion: glossary, rendered visuals, cost/security reasoning, conclusions. Mở rộng phần bị ảnh hưởng và reuse visual còn đúng thay vì dựng lại cả trang mỗi exchange. Fields dưới đây tổ chức nội dung; html.md quy định độ sâu giải thích.

## Topic records

Mỗi topic page gồm:

- Stable ID, title, scope/related links và status: exploring, awaiting-answer, settled, deferred hoặc superseded.
- Current position phân biệt observed facts, accepted choices, candidates, issues chưa giải quyết.
- Entries có ngày/stable anchor: source/attribution; substance và visual explanation; options thật, trade-offs/disposition; conclusion/rationale; authority hoặc chưa có; learning evidence và mức hỗ trợ cần; affected work/revisit triggers.
- Resume: một câu hỏi pending, đã hỏi chưa, câu trả lời còn thiếu, independent work được phép, next action; câu hỏi deferred khác với trigger riêng.

Topic có thể chỉ là explanation, không có decision. Local choice vẫn giữ reasoning dù không cần ADR. Future topic chỉ giữ chi tiết đã thực sự trao đổi.

Khi đổi position, append entry giữ position cũ, rationale ban đầu, evidence/câu trả lời mới và successor link; cập nhật current summary. Gắn nhãn rõ ý tưởng rejected/disproved trong history. Sửa nội dung dạy hiện hành mà không xóa user corrections hoặc proposals bị bác khỏi record.

## Architectural decisions

Tạo ADR khi choice được chốt nếu nó ảnh hưởng architecture, shared contracts, data/trust boundaries hoặc migration cost đáng kể với rationale lâu dài. Bao gồm cả foundational blueprint choices. Ngưỡng ADR xác định reasoning nằm ở đâu, không xác định nó có được giữ hay không; routine choice nằm trong topic record.

ADR gồm ID/title, date/scope, related links, context/drivers, alternatives thật với visual explanation và phân tích cost/security/risk trên cùng dimensions, decision/conclusion/rationale, authority/acceptance evidence, consequences/limits, revisit triggers, supporting sources/versions. Status: proposed, accepted, rejected, deprecated hoặc superseded với successor link.

Decision/rationale đã accepted trở thành history được giữ. Choice thay đổi cần successor ADR với supersession links hai chiều; được cập nhật status/link/lỗi chính tả. Evidence phản bác mở discussion và đánh dấu target cần xem lại, không tự thay acceptance. Legacy authority/rationale không có thì ghi unknown.

## User stories và walkthroughs

Ghi ngay mọi actor goal, rule, failure/edge case đã trao đổi, kể cả blueprint discovery hoặc trước approval. Một goal thống nhất có thể trải qua nhiều tutorials. API consumer/operator cũng là actor; internal change không có actor flow có thể dùng operational/verification scenario.

Mỗi story gồm:

- Stable ID/title; actor, goal/value, trigger, preconditions, intended success/postconditions, rules, edge cases, detail chưa chốt.
- Link discussion/ADR, catalogue outcome và tutorial checkpoints.
- Tách scope status (candidate/accepted/deferred/superseded), delivery status (unimplemented/in-progress/implemented), verification (not-run/partial/passed/failed kèm baseline/environment/evidence).
- Walkthrough khi đến lượt: setup/reset và safe data; actor action theo thứ tự → system interaction/state → expected observable result; rendered flow qua boundaries liên quan và worked example; negative/failure/recovery cases; cleanup/rollback; actual results/limits; conclusion/next action.
- Requirement changes có ngày, rationale, authority, behavior trước và successor links.

Blueprint ghi intent đã biết, không bịa click-level detail tương lai. Guide phát triển acceptance/walkthrough cho capability hiện tại trước dependent implementation instructions; behavior còn mở đáng kể được giải quyết qua decision process. QA thiết yếu cũng phải nằm trong tutorial. Pair thêm observed results với who/when/baseline/environment; intended behavior không tự thành passed. Giữ evidence cũ khi expectations đổi.

## Snapshot và resume

Snapshot gọn trong `index.html` ghi roots, source baseline/revision/date đã kiểm, product scope và current/target state, active tutorial/checkpoint, readiness/implementation/QA status, ownership evidence/gaps, một câu hỏi pending, next action, deferred triggers. Index topic/ADR/story IDs với status/link, gồm cả superseded. Guide chưa có blueprint tạo entry point tối thiểu từ facts đã biết.

Khi resume:

1. Đọc project instructions và snapshot; giữ roots.
2. Đọc active tutorial và discussions/stories/ADRs liên quan cùng project-wide constraints áp dụng. Theo supersession links và dùng index tìm history cần thiết.
3. Kiểm source/config/diffs và evidence so với baseline ghi lại. Source xác định implemented facts; user decisions xác định intended behavior. Ghi mismatch mà không tự đổi nghĩa bên nào.
4. Tiếp tục next action, reuse settled choices, giữ câu đã hỏi pending. Chỉ mở lại khi có evidence mới, revisit trigger hoặc user yêu cầu.

Index legacy context khi chạm tới, không bịa reasoning không có. Nếu cấm ghi, đưa proposed updates chính xác và nói chúng chưa được lưu.

Trước handoff, kiểm coverage các exchange có ý nghĩa, links, statuses nhất quán. Người đọc phải khôi phục được điều đã muốn, chọn/bác bỏ và vì sao; phần còn uncertain; đã build/test gì; user tự làm được gì; bước tiếp theo.
