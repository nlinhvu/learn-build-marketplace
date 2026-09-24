---
name: learn-onboard
description: Dùng khi người dùng muốn tạo/cập nhật documentation từ source dù thiếu docs gốc để hiểu, sử dụng và contribute vào project; gồm mục đích, glossary, concepts, guides, API reference, architecture, patterns và best practices có evidence. Catalogue kỹ thuật thuộc learn-catalogue; bài học sâu một mechanism thuộc learn-recipe.
---

# Learn Onboard

Giúp developer trả lời: project giải quyết vấn đề gì, dùng thế nào, những khái niệm/patterns nào tổ chức codebase và làm sao sửa đúng để contribute. Từ source không có docs gốc, tạo bộ documentation gồm hướng dẫn/tra cứu cách dùng và kiến thức contributor theo yêu cầu. Không hứa tái tạo nguyên bản hay đầy đủ như docs upstream.

## Khôi phục và xác định nguồn

Đọc [learning-contract.md](references/learning-contract.md), [project-memory.md](references/project-memory.md) và [onboarding.md](references/onboarding.md). Khôi phục source root, learning root, docs root, baseline, audience, trang hiện có và phạm vi nguồn được phép đọc. Mặc định onboarding người dùng/developer tích hợp project; thêm contributor path khi được yêu cầu hoặc hữu ích sau đường bắt đầu.

Khi yêu cầu có contribute, architecture, patterns hoặc best practices của codebase, đọc thêm [contributor-docs.md](references/contributor-docs.md). Tạo các trang contributor có nội dung trong cùng bộ docs, song song với usage/reference; không chỉ dẫn sang catalogue hoặc chờ người dùng chọn recipe mới viết.

Source, tests, examples, build metadata và API comments là đủ để bắt đầu; không yêu cầu thư mục docs gốc. Nếu người dùng loại trừ docs, ghi rõ paths và giữ exclusions trong mọi search/read, kể cả bản sinh sẵn, lịch sử Git và bản online của tài liệu bị loại trừ. Không xoá thư mục để mô phỏng thiếu docs. Đã đọc nguồn bị loại trừ thì nói rõ giới hạn đó, không nhận đánh giá độc lập chỉ từ source.

## Khảo sát và viết docs

Theo [onboarding.md](references/onboarding.md), lập capability map từ entry points, public contracts, configuration và tests. Khi tạo/cập nhật bộ docs hoặc một chapter hướng dẫn/tra cứu, đọc [documentation-contract.md](references/documentation-contract.md): dùng task ledger để xác định phạm vi và dùng chapter contract để viết nội dung. Yêu cầu nguồn docs có vai trò như reference của project là phạm vi rộng; đường first-run là điểm bắt đầu, không phải toàn bộ deliverable. Giải thích mục đích bằng scenario cụ thể và evidence, không suy ra ý định maintainer từ tên repo.

Mặc định tạo site HTML nhiều trang tại `<learning-root>/onboarding/`, với `index.html` riêng; liên kết từ learning index mà giữ catalogue/recipes hiện có. Người dùng chọn Markdown, AsciiDoc/Antora hoặc docs root khác thì làm theo, giữ chất lượng nội dung và kiểm định tương ứng. Đọc [visual-explanation.md](references/visual-explanation.md) và [html.md](references/html.md) trước HTML edits. Overview/concepts dùng hình giải thích quan hệ; Getting Started/guides có ví dụ hoàn chỉnh; reference dùng bảng và snippets theo nhu cầu, không ép mọi trang thành recipe hoặc full lab.

Với bộ docs, hoàn thiện các task trong phạm vi theo từng batch: source trace → guide/reference → kiểm artifact → cập nhật ledger → task tiếp theo. Coverage ghi riêng scope, độ sâu nội dung và evidence thực thi; một family có ví dụ đại diện chưa có nghĩa mọi task/adapter của nó đã được hướng dẫn. Checkpoint giữ toàn bộ phần còn lại và vị trí resume, không đổi chúng thành ngoài phạm vi. Với yêu cầu giải thích read-only hoặc chỉ một trang, giữ đúng phạm vi đó.

Khi người dùng muốn một bộ docs có vai trò gần reference của project hoặc nêu mục tiêu chất lượng, cố định trước các câu hỏi/tác vụ acceptance từ public source và crosscheck chúng với inventory public modules/API/config/tests để không tự chọn mẫu quá hẹp. Review **câu trả lời trong trang public**, không lấy nhãn actionable do tác giả tự ghi trong ledger làm điểm. Với site rộng, dùng reviewer độc lập nếu có; đưa cả task bị bỏ sót lẫn task trả lời thiếu về batch tiếp theo và chấm lại candidate mới theo cùng tiêu chí. Nếu phải dừng trước target, bàn giao partial và giữ gaps in scope.

## Kiểm và bàn giao

Đối chiếu mục đích, public API, dependencies, defaults, conditions, examples và troubleshooting với baseline. Thử đường đọc theo task ledger, gồm bootstrap không dựa vào cache chưa được chuẩn bị. Kiểm navigation/local links, rendering và code từ artifact cuối trong context mô tả khi khả dụng. Tách source-reviewed, syntax-checked, compiled và runtime-verified; không cần credentials để viết phần có thể chứng minh từ source, không bịa kết quả external service.

Cập nhật coverage và records: roots, exclusions, pages/capabilities, source anchors, checks, câu hỏi chưa rõ và phần cần tiếp tục. Khi source đổi, review các trang chịu ảnh hưởng, giữ URL/IDs và giải thích đúng hiện tại. Bàn giao entry page, nhóm docs đã viết và giới hạn; kết nối tới catalogue/recipe khi người dùng muốn học implementation sâu hơn, không bắt hoàn thành chúng trước onboarding.
