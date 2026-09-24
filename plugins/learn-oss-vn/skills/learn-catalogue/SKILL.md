---
name: learn-catalogue
description: Dùng khi người dùng muốn tìm những kỹ thuật đáng học trong một open-source repo, lập catalogue recipes theo category và prerequisites, hoặc cập nhật bản đồ học tập khi source thay đổi. Bộ docs về mục đích/cách dùng project thuộc learn-onboard; viết sâu một recipe thuộc learn-recipe.
---

# Learn Catalogue

Lập bản đồ học từ code thật: dễ hiểu trước, hữu ích cho cộng đồng tiếp theo, rồi hỗ trợ tự tin contribute. Catalogue rộng, recipe chi tiết theo lựa chọn; không biến toàn bộ repo thành giáo trình phải học tuần tự.

Nếu yêu cầu chính là onboarding hoặc tạo documentation để developer hiểu và sử dụng project từ source, dùng `learn-onboard` khi khả dụng. Catalogue có thể link tới docs onboarding hiện có, nhưng không thay chúng bằng danh sách kỹ thuật đáng học.

## Khôi phục phạm vi

Đọc [learning-contract.md](references/learning-contract.md) và [project-memory.md](references/project-memory.md). Xác định repo/source baseline, learning root, catalogue/records hiện có và phần đã khảo sát. Đọc project instructions, source, tests và contributor documentation liên quan; thiếu repo thì hỏi đường dẫn cần thiết, không đoán kỹ thuật từ tên project.

## Khảo sát và lập catalogue

Dùng [catalogue.md](references/catalogue.md) cho coverage, phân loại, entry và prerequisites. Khảo sát các subsystem để tìm kỹ thuật có evidence; phân biệt phát hiện đã xác minh, ứng viên cần đọc thêm và kiến thức nền hỗ trợ. Không dừng ở vài files nổi bật rồi nhận đã tìm hết.

Tạo/cập nhật `<learning-root>/index.html` với bản đồ project dễ hiểu, catalogue theo category, đường học đề xuất, source baseline và coverage. Cho người đọc quét nhanh vấn đề/kết quả học, prerequisites và trạng thái bài; mở sâu khi cần source anchors và lý do độ khó. Mỗi recipe có stable ID; bài đã viết có link trực tiếp tới file canonical trong category chính. Chỉ tạo bài chi tiết được chọn.

Trước khi viết HTML, đọc [visual-explanation.md](references/visual-explanation.md) và [html.md](references/html.md). Catalogue cần giải thích các khái niệm/quan hệ để người mới chọn được bài, không chỉ bảng tên. Với dependency map dùng ví dụ đọc quan hệ, không bịa runtime sequence.

## Kiểm và bàn giao

Đối chiếu entries với source đã khảo sát, liên kết/prerequisites và giới hạn coverage. Lưu câu hỏi, corrections, lựa chọn và phần còn mở theo memory contract; public catalogue không nhúng learning state cá nhân. Nêu bài bắt đầu hợp lý cùng lý do, cho người dùng chọn hoặc làm theo lựa chọn đã có. Khi khả dụng, `learn-recipe` đọc cùng catalogue/records để viết bài; không yêu cầu người dùng sao chép context giữa skills.
