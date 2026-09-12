# HTML giàu nội dung để hiểu và làm chủ độc lập

Giải thích phong phú bằng visual là đặc trưng cốt lõi của mọi output HTML: blueprint, tutorial, decision, discussion, ADR, user story và explainer. Nội dung phải giúp user hiểu và tự làm việc trên product thật, phục vụ ưu tiên cao nhất trong [learning-contract.md](learning-contract.md).

## Nội dung để người đọc reasoning

Mỗi topic có nội dung thực chất phải có:

- **Glossary chi tiết tại chỗ:** nghĩa dễ hiểu, responsibility/ownership, ví dụ cụ thể từ product và vị trí trong flow.
- **Context và causal explanation:** vấn đề, vì sao quan trọng, mechanism hoạt động thế nào, constraints và hệ quả với code/vận hành.
- **Visual đã render và worked example:** diagrams, graphs, flows có nhãn boundary, arrow/state, caption/legend. Trace input cụ thể → state trung gian → output, gồm failure liên quan và source symbols thật.
- **Alternatives so sánh được:** ưu/nhược trên cùng dimensions, gồm engineering/learning effort, runtime/resource/operating và migration costs, security/trust/data implications, reliability, reversibility khi liên quan. Nêu assumptions/unknowns; giá tiền dùng nguồn hiện hành. Nói rõ khi chưa có monetary cost hoặc dimension không áp dụng.
- **Kết luận có reasoning:** evidence hỗ trợ điều gì, vì sao chọn/bác bỏ/hoãn options, consequences, limits và next action/câu hỏi còn mở. Không bịa decision để kết thúc trang.

Nêu invariant/decision/prerequisite thật và hệ quả ngay nơi dùng. Link hỗ trợ provenance/đào sâu; người đọc không phải hỏi lại trong chat để hiểu phần thiết yếu. Giữ code, explanation, visual và QA cần thiết tại chỗ. Details dùng cho phân tích sâu, alternatives, history; tổ chức độ sâu chứ không rút mất nội dung.

Chọn visual theo quan hệ: sequence diagram cho interactions, state diagram cho lifecycle, dependency/ownership graph cho boundary/thứ tự, trace table cho algorithm, comparison table cho trade-off. Interactive stepping/so sánh scenario hữu ích với race và nhiều transition. Render bằng inline SVG/HTML hoặc renderer khả dụng; Mermaid source chưa render không tính là diagram. Box component trang trí không giải thích causality. Graph định lượng cần evidence hoặc assumptions có nhãn; không ép quota chart hoặc bịa số.

## Records bền vững cũng là HTML phong phú

Theo [project-memory.md](project-memory.md) về fields/lifecycle. Đặt current position và resume link trước; giữ entries lịch sử có ngày, stable IDs và nhãn rejected/disproved/superseded. Giữ glossary, worked traces, visuals, cost/security analysis và conclusions của chúng. Metadata update ngắn không cần lặp cả explanation. Record outline xác định nội dung cần giữ, không cho phép chỉ xuất ledger trạng thái.

Nội dung dạy hiện hành giải thích baseline/target hiện tại, không kể lịch sử sửa văn bản. Phần history giữ reasoning/corrections cũ với link tới current position để người đọc không nhầm claim cũ là guidance hiện hành.

## Structure và code

Reuse HTML/CSS của project; dùng [learn.css](../assets/learn.css) làm nền khi cần. HTML semantic với `lang="vi"`, UTF-8, viewport, title, navigation, main/section, heading hierarchy và stable IDs. Theo quy ước tiếng Việt/technical terms/code trong learning-contract.md. Mở đầu bằng outcome và next action. Có caption, controls dễ tiếp cận; code/table rộng scroll riêng với scroll cue; tránh tràn ngang toàn trang.

Code có exact paths/symbols và scoped edits đầy đủ. Escape ký tự HTML nhưng giữ cú pháp ngôn ngữ sau decoding và whitespace trong pre/code; không thêm lớp Java/JSON/shell escaping. Kiểm code trích từ HTML cuối cùng trong baseline/fragment context được mô tả. Một scratch implementation khác không chứng minh snippet bàn giao đúng; compile không chứng minh runtime.

Local links/fragments tính từ vị trí file thật. Interaction phải chạy bằng cách mở đã hướng dẫn; tránh CDN bắt buộc hoặc external request ngoài scope.

## Kiểm trước handoff

1. Dùng formatter/HTML5 validator khả dụng. Kiểm structure, escaping, accessibility semantics, duplicate IDs, links/fragments. Parser tự viết hoặc xmllint chỉ là check giới hạn, không phải HTML5 validation.
2. Mở browser ở desktop/mobile và xem screenshot; thử details, interaction, keyboard/focus, code/table scrolling, contrast, overflow.
3. Đọc độc lập từng trang theo content bar ở trên. Theo input thật qua visual/code đến success/failure; kiểm glossary, reasoning, trade-off, cost/security và conclusions khớp source/decision.
4. Ghi đúng phạm vi/evidence còn thiếu. Tool không có thì kiểm phần khả dụng, đánh dấu rendering/execution chưa xác minh. Sau edit kiểm lại phần và links bị ảnh hưởng.

Records và tutorials được kiểm như nhau. Artifact đẹp không tự chứng minh product đúng hoặc user đã làm chủ.
