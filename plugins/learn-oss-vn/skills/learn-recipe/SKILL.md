---
name: learn-recipe
description: Dùng khi người dùng chọn một kỹ thuật từ open-source để học qua recipe HTML, cần đào sâu hoặc hỏi đáp/thực hành theo recipe hiện có, hay cập nhật bài khi source thay đổi. Khảo sát toàn repo và lập catalogue thuộc learn-catalogue; không kéo mọi coding task vào workflow học tập.
---

# Learn Recipe

Viết bài để cả người dùng và người đọc cộng đồng hiểu mechanism, tự thử và áp dụng. Ưu tiên dễ học → chia sẻ hữu ích → tự tin contribute; không coi bài viết xong là người đọc đã làm chủ.

## Khôi phục và chọn phạm vi

Đọc [learning-contract.md](references/learning-contract.md) và [project-memory.md](references/project-memory.md). Khôi phục recipe/ID, roots, source baseline, câu hỏi, corrections và lựa chọn đã lưu. Kiểm source/diff, tests và contributor documentation liên quan. Có thể bắt đầu trực tiếp từ topic; thiếu catalogue đầy đủ không chặn bài, chỉ bổ sung index tối thiểu cần thiết.

Chọn một vấn đề đủ nhỏ để giải thích bằng scenario xuyên suốt. Phân biệt behavior trong code, rationale có nguồn và suy luận của tác giả. Không tự sửa implementation khi chỉ được giao giải thích/viết bài.

## Giải thích và tạo bài

Đọc [recipe.md](references/recipe.md) để phân tích source, thực hành và áp dụng. Đọc [visual-explanation.md](references/visual-explanation.md) và [html.md](references/html.md) trước mọi HTML edit.

Tạo/cập nhật `<learning-root>/<category>/<recipe-slug>.html`: glossary trực quan → diagram đã render → step-by-step dùng cùng input/state → code tương ứng → thử nghiệm và giới hạn. Mỗi runtime bước trên hình khớp walkthrough và source symbol. Có failure/edge case liên quan; diagram tĩnh dùng ví dụ đọc quan hệ thay vì trình tự giả.

Bài tự chứa context, glossary, code/setup/commands thiết yếu, expected observations, trade-offs và kết luận. Người đọc không cần chat, file lab riêng hay agent để nghĩ hộ phần còn thiếu. Viết rõ cách dùng ở project khác và constraint/convention riêng của repo gốc.

## Hỏi đáp, kiểm và bàn giao

Khi người dùng chưa hiểu, bổ sung trace/diagram tại chỗ, lưu diễn biến trong records và tích hợp giải thích dùng chung vào bài. Thực hành/sửa source chỉ trong phạm vi được giao, không quiz hay PR bắt buộc.

Kiểm code trích từ HTML cuối, diagram/steps, source claims và rendering theo html.md; báo đúng phạm vi đã chạy/chưa xác minh. Cập nhật catalogue, records và snapshot bị ảnh hưởng, không xóa reasoning cũ. Handoff link bài, điều đã kiểm, câu hỏi còn mở và bước tiếp theo; không tự publish hoặc nhận người dùng đã hiểu chỉ vì agent hoàn thành.
