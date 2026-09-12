# Giải thích bằng glossary, diagram và ví dụ xuyên suốt

## Người đọc hiểu mechanism trước khi đọc sâu code

**Visual glossary là nội dung dạy chính.** Với mỗi khái niệm cốt lõi: nghĩa dễ hiểu, vai trò/trách nhiệm, ví dụ trong scenario và vị trí có nhãn trên diagram. Nối các khái niệm lại để giải thích vì sao thuật toán hoạt động. Không chỉ liệt kê định nghĩa rồi đặt một hình không liên quan bên cạnh. Glossary chung có thể giúp tra cứu; phần cần để hiểu bài vẫn ở tại chỗ.

Chọn một input/scenario cụ thể và dùng nhất quán tên đối tượng, dữ liệu và state xuyên suốt glossary → diagram → walkthrough → code → test. Ví von ngắn là tùy chọn; bỏ nếu cần thêm giải thích hoặc làm sai invariant.

## Diagram phải mang lập luận

| Điều cần hiểu | Visual phù hợp |
| --- | --- |
| Ai gọi ai, gửi dữ liệu gì | Sequence diagram hoặc flow có nhãn actors/payloads |
| State đổi khi nào, điều kiện kết thúc | State diagram, timeline hoặc trace table |
| Race, ownership, cancellation | Interleaving có lanes và state từng bước; stepper khi hữu ích |
| Một thuật toán biến đổi input thế nào | Diagram kèm trace dữ liệu qua từng bước |
| Học khái niệm nào trước, module nào phụ thuộc nhau | Dependency graph và ví dụ đọc một nhánh |
| Bao nhiêu, đắt/chậm ở đâu | Biểu đồ có đơn vị và tỉ lệ, assumptions/evidence rõ |

Render bằng inline SVG/HTML/CSS hoặc renderer khả dụng. ASCII art hay Mermaid source trong code block chỉ là phần hỗ trợ, không thay diagram đã render. Hình component trang trí không thay causal flow. Mũi tên ghi ý nghĩa; boundaries, legend và thứ tự phải đọc được mà không cần đoán theo màu.

## Diagram ↔ step-by-step ↔ code

Với algorithm/runtime flow:

1. Nêu input và state ban đầu, cùng assumptions ảnh hưởng đến kết quả.
2. Đánh số các bước quan trọng trên hình. Phần walkthrough ngay cạnh/bên dưới dùng cùng số, cùng thuật ngữ.
3. Mỗi bước giải thích **ai thực hiện → nhận gì → làm gì → state/output đổi thế nào → vì sao bước tiếp theo xảy ra**. Gắn source symbol và đoạn code tương ứng; người đọc lần được cả hai chiều từ hình tới code.
4. Theo cùng scenario đến kết quả quan sát được. Nếu dữ liệu đi theo nhánh nội bộ/out-of-band, vẽ riêng với line style, nhãn và legend; giải thích khác biệt với payload chính.
5. Đặt failure/edge case liên quan cạnh success case hoặc trong một trace đối chiếu. Chỉ ra bước phân nhánh, invariant bị vi phạm/được giữ, cách phát hiện và hệ quả.

Số bước theo mechanism, không cố định bảy bước. Với dependency map hoặc visual tĩnh không có trình tự thực thi, dùng hướng dẫn đọc và ví dụ đi qua quan hệ; không bịa runtime sequence.

Ảnh không có mũi tên tới một actor chưa chứng minh dữ liệu không thể bị lộ. Claims về boundary/security cần đối chiếu source, gồm đường return/error/log liên quan và giả định trust. Trình bày rõ phạm vi đã kiểm, không suy thành bảo đảm toàn hệ thống.

## Khi lượng và chi phí là bài học

Giữ tỉ lệ, đơn vị, axes và cùng scale khi so sánh. Nếu vùng quan trọng quá nhỏ, dùng thêm zoom có nhãn thay vì bóp méo tỉ lệ mà không nói. Phân biệt số đo thực, số tính từ assumptions và dữ liệu minh họa. Measurement có baseline, ngày, môi trường/workload và cách đo lại; không mượn số của một repo khác.

Nêu chi phí liên quan: số operations/requests, memory, CPU, I/O, latency, complexity, engineering effort hoặc vận hành. Không bịa monetary cost hay biểu đồ định lượng cho topic chỉ có quan hệ cấu trúc. Không gọi một phép tính là benchmark đã chạy. Failure case chưa quan sát phải ghi là phân tích/minh họa, không bịa sự cố production.

## Giữ đường đọc dễ nhất

Trực giác ngắn → visual glossary + diagram → walkthrough cụ thể → code → giới hạn và áp dụng. Đây là gợi ý tổ chức, không bắt mọi bài có cùng headings. Phần chuyên sâu có thể mở rộng; prerequisites thiết yếu và kết luận nằm trên đường đọc chính.

Stepper/animation chỉ thêm khi giúp theo dõi state. Có tiến/lùi/reset, nhãn keyboard-accessible và kết quả nhất quán khi đổi scenario. Bản tĩnh, captions và explanation vẫn đủ hiểu khi JavaScript không chạy. Kiểm lại hình, từng số bước, dữ liệu và code cùng nhau sau mỗi sửa đổi; không chỉ kiểm HTML có render.
