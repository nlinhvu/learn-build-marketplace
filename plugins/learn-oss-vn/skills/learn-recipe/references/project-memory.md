# Giữ context qua session, không đưa thông tin cá nhân vào bài chia sẻ

## Hai nơi đọc, hai mục đích

- `<learning-root>/index.html`: catalogue công khai, source baseline, coverage và trạng thái tài liệu; không nhúng thông tin riêng về người học.
- `<learning-root>/onboarding/index.html`: entry của docs onboarding và navigation tới các trang concepts/getting started/guides/reference đã viết. Learning index link tới đây mà không thay catalogue hiện có.
- `<learning-root>/records/index.html`: snapshot cho session tiếp theo, gồm roots, active recipe/ID, baseline, câu hỏi đang mở, lựa chọn, evidence học đã quan sát và bước tiếp theo; liên kết các topic records.
- `<learning-root>/records/<topic-slug>.html`: nội dung trao đổi có ý nghĩa, gồm explanations/visuals đã phát triển, corrections, lý do chấp nhận/bác bỏ/hoãn, non-ADR choices, câu hỏi chưa giải quyết và evidence. Giữ ADR hoặc user story thực sự liên quan, không bịa decision/story cho một câu hỏi giải thích đơn thuần.

Các paths là mặc định; giữ records tương đương hiện có. Chỉ tạo files có nội dung, không tạo cả bộ folders rỗng. Mọi learning records mới là HTML.

Với onboarding, snapshot ghi thêm docs root/format, audience, nguồn được phép và paths bị loại trừ, active page/capability, page IDs/paths, coverage và anchors theo baseline. Khi quay lại hoặc đổi skill, giữ source exclusions và phân biệt trạng thái đã khảo sát, đã viết, source-reviewed, compiled, runtime-verified. Dùng chung records với catalogue/recipe nếu cùng learning root; không tạo lịch sử song song.

## Lưu khi trao đổi, không chỉ lúc kết phiên

Ghi nội dung ở topic hiện có với stable IDs, ngày và attribution. Phân biệt lời người dùng, quan sát từ công cụ, suy luận và đề xuất agent. Giữ phần giải thích chưa thành decision, nguyên văn correction khi wording quyết định nghĩa, alternatives đã cân nhắc thực sự và lý do disposition. Không bịa rationale bị mất do thiếu lịch sử.

Recipe hiện hành trình bày hiểu biết đúng hiện tại cho người đọc chung. Giải thích bổ sung hữu ích được tích hợp tại chỗ, không kể lại chuyện chỉnh bài. History giữ reasoning/diagram cũ có nhãn superseded/disproved, link tới phần thay thế; không xóa vì dọn bố cục. Update metadata nhỏ không cần lặp toàn bộ bài, nhưng không rút một discussion có nội dung thành vài status fields.

Snapshot ghi current position và next action ngắn, dẫn tới records chi tiết. Tách trạng thái catalogue/recipe, evidence thực thi và khả năng người dùng. Agent chạy tests, user im lặng hoặc đồng ý không là bằng chứng đã hiểu. Câu hỏi đã hỏi vẫn pending cho tới khi có câu trả lời thật; không tự đánh dấu giải quyết vì đổi session hoặc tạo được bài.

## Khôi phục

Đọc snapshot và topic/recipe liên quan; kiểm source/diff đối với baseline đã ghi. Xác định phần chưa biết, phần cần review, câu hỏi đang chờ và bước tiếp theo. Source mới không tự xóa evidence cũ: giữ ngày/baseline của kết quả cũ, đánh dấu phần guidance bị ảnh hưởng để kiểm lại. Không đọc lại mọi records không liên quan hoặc bắt người dùng kể lại thông tin còn trên đĩa.

## Ranh giới chia sẻ

Public recipe/catalogue không chứa absolute paths cá nhân, secrets, thông tin người học hoặc links thiết yếu tới records riêng. Câu hỏi cá nhân có thể được tổng quát hóa thành explanation cho cộng đồng, còn nguyên context lưu riêng khi được phép.

Các ranh giới chia sẻ này cũng áp dụng cho docs onboarding, kể cả khi xuất Markdown/AsciiDoc; tài liệu công khai phải đọc được mà không cần records hoặc lịch sử chat.

**Thư mục `records/` không tự làm dữ liệu private.** Nếu cả repo/site được publish thì records cũng có thể lộ. Trước khi chia sẻ, xác định đúng tập files gồm recipe/catalogue công khai và assets cần thiết; loại records cá nhân khỏi tập đó và kiểm HTML/source code/comments, không chỉ giao diện hiển thị. Ẩn bằng CSS/details hoặc không đặt link không bảo vệ nội dung.

Không tự xóa records, publish, đổi permissions hoặc chuyển chúng ra ngoài root được giao. Với task read-only, chỉ đề xuất updates và ghi rõ chưa persist. Handoff khi không ghi được phải nêu context nào chưa lưu để người dùng không tin rằng session sau đã có nó.
