# Catalogue có evidence và lộ trình học

## Khảo sát có thể tiếp tục

1. Ghi baseline và phạm vi repo. Đọc entrypoints, sơ đồ module/package, tests, benchmarks, config, CI/CD, CONTRIBUTING và conventions đã được project ghi nhận. Tôn trọng instructions trong repo; không chạy scripts lạ chỉ vì chúng xuất hiện trong source.
2. Lập coverage theo subsystem và loại evidence. Mỗi phần ghi đã kiểm kê/đã đọc sâu/chưa khảo sát, files hoặc symbols đại diện và việc tiếp theo. Với repo lớn, đi nhiều lượt và checkpoint; chưa đọc không đồng nghĩa không tồn tại kỹ thuật.
3. Tìm các vấn đề code thực sự giải quyết, theo luồng đến callers/tests trước khi đặt tên recipe. Không tạo đủ số lượng tùy ý hoặc biến mỗi function thành một bài. Tách các cơ chế độc lập; gộp những entries cùng dạy một insight.
4. Nêu các vùng còn thiếu và tiếp tục khảo sát khi scope yêu cầu toàn repo. Khi dừng do giới hạn phiên/công cụ, ghi rõ phạm vi đã đạt, không tuyên bố catalogue exhaustive.

## Categories và entries

Dùng categories phù hợp từ: design patterns, best practices, coding techniques, coding conventions, testing, benchmarking, security, scalability, concurrency, resource efficiency, observability, DevOps và developer practices. Đặt folder slug bằng English; thêm/tách category theo repo khi giúp tra cứu. Không ép các topic không có evidence vào catalogue để lấp danh sách.

Mỗi entry có:

- Stable ID, tên theo vấn đề/kỹ thuật, kết quả người đọc sẽ hiểu hoặc tự làm được.
- Category chính, tags liên quan; một canonical path `<category>/<recipe-slug>.html` khi bài đã viết.
- Source/test/doc anchors và baseline hỗ trợ entry; rationale maintainer có nguồn hay chỉ là inference.
- Prerequisites là khái niệm/recipe cụ thể, độ khó và lý do (kiến thức cần có, số boundary/state phải theo dõi).
- Trạng thái evidence: đã xác minh hoặc ứng viên cần khảo sát; trạng thái bài: chưa viết, draft, đã kiểm trong phạm vi nêu rõ, hoặc cần review do baseline thay đổi.

Entry chưa có bài không tạo link chết; dùng tên/ID để chọn. Topic nền tảng được đề xuất chỉ để hỗ trợ học phải ghi rõ không phải kỹ thuật đã phát hiện trong implementation. Không biến recipe status thành chứng nhận người dùng đã học xong.

## Trang index phục vụ người mới

Mở đầu bằng project giải quyết gì, phạm vi khảo sát và vài khái niệm để đọc bản đồ. Dùng glossary tại chỗ và diagram cho subsystem/dependency khi chúng giúp người đọc định hướng. Sau đó có catalogue theo category và đường học theo prerequisites, không nhất thiết trùng thứ tự folder.

Catalogue nhiều entries cần lớp quét nhanh: ID/tên, một câu vấn đề hoặc kết quả học, prerequisites chính, độ khó và trạng thái bài. Dùng rows/cards gọn hoặc mục lục theo category; evidence, rationale và coverage sâu có thể mở rộng tại entry. Không bắt đọc nhiều đoạn của từng bài để so sánh lựa chọn; tránh boilerplate prerequisites lặp lại. Không buộc có search/filter bằng JavaScript nếu navigation tĩnh đã đủ.

Đề xuất điểm bắt đầu dễ hiểu, tác động lớn, có ví dụ quan sát được. Nếu bài đã viết, điểm bắt đầu và đường học có link rõ tới bài, không chỉ vòng về entry; bài chưa viết cho chọn bằng ID, không tạo link giả. Người dùng được chọn bài khác; giải thích prerequisite thiếu thay vì cấm chuyển bài. Dependency graph phải phản ánh điều thực sự cần để học, không nối mọi bài thành chuỗi hoặc vòng không giải thích được.

Public index chứa source baseline, coverage, document status và đường học chung. Snapshot về câu hỏi đang mở, lựa chọn cá nhân và learning evidence nằm ở `records/index.html`, không trộn vào bản catalogue để chia sẻ.

Khi recipe mới phát hiện insight hoặc source thay đổi, cập nhật entries/dependencies liên quan. Đọc lại phần bị ảnh hưởng trước khi đổi trạng thái cần review thành đã kiểm; không đánh dấu cả catalogue mới chỉ vì commit hash đổi.
