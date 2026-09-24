# HTML để đọc độc lập và chia sẻ

Đọc [visual-explanation.md](visual-explanation.md) cho nội dung dạy. Áp dụng cho catalogue, recipe, glossary và discussion records có nội dung thực chất; không để records chỉ còn ledger trạng thái.

Với docs onboarding HTML, áp dụng cùng yêu cầu offline, accessibility, evidence và kiểm rendering/navigation. Mỗi trang theo mục đích đọc: Overview/Concepts giải thích project và mental model, Getting Started/guides có ví dụ đủ chạy, Reference ưu tiên contracts/configuration có thể tra cứu. Không buộc mọi trang reference có full lab hoặc diagram. Format khác HTML dùng toolchain kiểm tương ứng theo yêu cầu người dùng.

## Hình thức và tính tự chứa

Mỗi recipe có HTML riêng trong category chính, không nhét toàn bài vào `index.html`. Giữ nội dung thiết yếu để đọc và thực hành trong chính file: context, glossary, diagram đã render, walkthrough, source excerpts, code thực hành đầy đủ, setup/commands, expected observations, chẩn đoán và kết luận. Có thể kèm file tải xuống tiện dùng nhưng link đó không thay code thiết yếu trong bài.

Nhúng CSS/SVG và JavaScript cần thiết để mở bằng `file://` không cần mạng, server hoặc tài khoản. Có thể dùng [recipe.css](../assets/recipe.css) làm nền rồi inline vào HTML. Tái sử dụng giao diện project khi phù hợp; không mặc định mọi bài cần dashboard hoặc animation. Source links công khai và tài liệu đọc thêm có thể cần Internet, ghi rõ điều này; không phụ thuộc CDN cho nội dung cốt lõi.

Dùng `lang="vi"`, UTF-8, viewport, title có vấn đề cụ thể, semantic headings/navigation/main/section, stable IDs, captions và legend. Link/controls có focus rõ, keyboard-accessible, không dùng màu làm tín hiệu duy nhất. Code/table/diagram rộng scroll riêng có cue; không tràn ngang toàn trang. Giữ font/nhãn diagram đọc được trên mobile; không thu nhỏ toàn hình tới mức chữ vô nghĩa. Tôn trọng reduced motion và cho phép đọc tĩnh.

## Code và evidence trong bài

Escape HTML nhưng giữ cú pháp và whitespace sau decoding; không chồng shell/JSON escaping vào snippets. Code có paths/symbols và baseline thật. Phân biệt exact excerpt, bản rút gọn, code minh họa và code thực hành mới. Fragment phải có context đủ để dùng; code cần thiết không bị thay bằng ellipsis hoặc prompt giao agent.

Trích code từ HTML cuối để syntax/compile/test trong context mô tả khi công cụ khả dụng và scope cho phép. Kiểm command, expected/observed result và cleanup. Chạy bản scratch khác không chứng minh snippet bàn giao đúng; compile không chứng minh runtime. Không chèn claims pass vào hướng dẫn chưa chạy.

## Kiểm trước bàn giao

1. Dùng formatter/HTML5 validator khả dụng; kiểm tags, escaping, IDs trùng, local links/fragments và headings. Parser tự viết chỉ là check cấu trúc giới hạn.
2. Mở đúng output cuối trong browser khi có; kiểm glossary, diagram, code/table và phần mở rộng, không chỉ chụp đầu trang. Kiểm desktop và viewport hẹp, xác nhận kích thước thực tế trước khi nhận đã kiểm mobile. Thử details/stepper, keyboard/focus và overflow; hình rộng cần cue cuộn rõ hoặc state panels đọc được ở màn hình hẹp. Nếu `file://` bị policy chặn nhưng local HTTP khả dụng và không bị cấm, serve riêng public docs root trên `127.0.0.1` để render rồi dừng server; kiểm `documentElement.scrollWidth` để bắt cả source link/identifier dài ngoài code/table. Khi cả browser lẫn fallback an toàn không khả dụng, ghi đúng giới hạn và kiểm phần còn làm được; không nhận source/CSS inspection là visual verification.
3. Đọc riêng bài không có chat hoặc file lab: mỗi section trả lời câu hỏi gì, hình và snippet có được giải thích cạnh nhau, input có lần được tới output/failure? Kiểm khả năng giải thích của hình theo visual-explanation.md và đường đọc cốt lõi: có tới được kết luận mà không phải đi qua full lab? Với catalogue, thử chọn bài tới đúng recipe; với records, tìm current state và reasoning liên quan. Checks cấu trúc pass không thay các bước đọc này.
4. Kiểm attribution, source baseline, claims và phạm vi tests/benchmarks. Tách observed, inferred, estimated, unknown. Xem lại boundary/security claims, không để hình và prose hứa nhiều hơn source.
5. Khi chuẩn bị chia sẻ, kiểm tập files thực sự sẽ được gửi/publish theo [project-memory.md](project-memory.md); không tự publish sau khi kiểm.

Báo đúng files, phần đã kiểm và giới hạn. Artifact đẹp hoặc check cấu trúc pass không chứng minh teaching quality, source correctness hoặc người dùng đã làm chủ.
