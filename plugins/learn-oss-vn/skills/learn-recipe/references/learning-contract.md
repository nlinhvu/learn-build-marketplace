# Học dễ, chia sẻ hữu ích, áp dụng đúng

## Ưu tiên và người đọc

Thứ tự ưu tiên: **dễ học và hiểu đúng → giúp cộng đồng hiểu và áp dụng → tự tin contribute vào open-source**. Người đọc có thể chưa biết project và không có lịch sử chat. Recipe là bài học độc lập, không phải ghi chú riêng hoặc workflow xây product mới. Giảm tải nhận thức bằng ví dụ xuyên suốt và độ sâu mở rộng, không bằng cách bỏ mechanism, prerequisites hoặc giới hạn quan trọng.

Giữ technical terminology và specialized words bằng tiếng Anh. Toàn bộ source/test code, identifiers, comments, docstrings, test names, assertions và runtime strings dùng tiếng Anh. Phần trao đổi, hướng dẫn, giải thích, nhãn diagram, kết luận và records còn lại dùng tiếng Việt. Giữ nguyên API names, commands, paths, log output và trích dẫn để không làm sai evidence.

## Codebase là nguồn kiểm chứng, không phải giáo điều

Ghi repo, commit/version và local modifications ảnh hưởng đến nhận định. Phân biệt behavior đọc/quan sát được, rationale được maintainer ghi nhận, và phân tích/suy luận của tác giả. Không suy từ tên class ra design pattern, từ một chỗ dùng ra convention toàn repo, hoặc từ code tồn tại ra best practice phổ quát. Điều chưa biết vẫn là unknown; phần rút gọn, minh họa hoặc đề xuất phải mang nhãn tương ứng.

Đối chiếu external API/version với nguồn chính thức phù hợp khi cần. Dùng public source permalinks theo commit nếu có; không tạo link giả cho thay đổi local. Ghi attribution và kiểm license/notice của đoạn code hoặc hình định chia sẻ; không tự gán license của repo cho toàn bộ nội dung bài hay sao chép docs upstream hàng loạt.

## Phạm vi và quyền thực hiện

Learning root mặc định `<invocation-workspace>/docs/learn-oss`; đường dẫn được chỉ định có ưu tiên. Source root có thể khác. Giữ roots đã ghi khi đổi working directory. Tái sử dụng tài liệu canonical; không tự move/migrate chúng.

Khảo sát/viết recipe không cấp quyền sửa source, mở PR, publish, deploy, scan hệ thống công khai hoặc chạy workload tốn phí. Thực hành trong môi trường local/cô lập được phép, với giới hạn tài nguyên và cleanup. Với yêu cầu read-only, chỉ đưa findings/đề xuất cập nhật, không nhận đã lưu records.

Catalogue và bài chi tiết dùng cùng IDs và source baseline nhưng không buộc nhau hoàn chỉnh. Người dùng có thể chọn topic trực tiếp; tạo catalogue tối thiểu khi cần, rồi làm phần hữu ích. Hỏi một thông tin đang thiếu khi nó quyết định phạm vi hoặc tính đúng; không hỏi lại dữ liệu đã có hoặc bắt xác nhận những lựa chọn biên tập thông thường.

## Học và tiếp tục

Giải thích → dự đoán một state/output → đối chiếu source/experiment → áp dụng một biến thể là cách học gợi ý, không phải quiz bắt buộc. Bài luôn cung cấp đủ setup, code, thao tác và cách kiểm để người đọc thử mà không cần agent nghĩ hộ. Có thể giảm gợi ý theo nhu cầu; không từ chối giúp đỡ hoặc bắt thực hành lại điều người dùng đã biết.

Agent viết bài/chạy tests không chứng minh người dùng đã hiểu hoặc có thể contribute. Lưu evidence người dùng thực sự làm/giải thích, mức trợ giúp và khoảng trống còn lại riêng với evidence thực thi. Khi người dùng nói chưa hiểu, bổ sung một trace/diagram cụ thể tại chỗ; không chỉ lặp lại định nghĩa.

Trước khi kết phiên, lưu nội dung trao đổi có ý nghĩa và snapshot theo [project-memory.md](project-memory.md). Trước khi tạo/sửa HTML, đọc [visual-explanation.md](visual-explanation.md) và [html.md](html.md). Hai skill tự chứa các references này; không yêu cầu cài skill hay công cụ của một agent cụ thể.
