# Giải thích bằng glossary, diagram và ví dụ xuyên suốt

## Người đọc hiểu mechanism trước khi đọc sâu code

**Visual glossary là nội dung dạy chính, không phải chương từ vựng bắt buộc ở đầu bài.** Giải thích mỗi khái niệm cốt lõi tại nơi cần dùng: nghĩa dễ hiểu, vai trò/trách nhiệm, ví dụ trong scenario và vị trí có nhãn trên diagram. Biểu diễn điều trừu tượng bằng cấu trúc dữ liệu, payload, phần dung lượng đã dùng/còn lại hoặc reference tới object. Một hình có thể giải thích nhiều khái niệm; không cần mỗi từ một hình. Text cards và chữ cái tra cứu không tự tạo thành visual glossary. Glossary tổng hợp có thể giúp tra cứu, không thay giải thích tại chỗ.

Chọn một input/scenario cụ thể và dùng nhất quán tên đối tượng, dữ liệu và state giữa glossary, diagram, walkthrough, code và test. Dùng nhãn có nghĩa tại chỗ, tránh bắt người đọc nhớ thêm mã A/B/C nếu tên object/biến đã đủ. Giải thích khái niệm bằng ví dụ nó là gì trước khi nói nó không phải gì. Ví von ngắn là tùy chọn; bỏ nếu làm sai invariant.

## Diagram phải mang lập luận

| Điều cần hiểu | Visual phù hợp |
| --- | --- |
| Ai gọi ai, gửi dữ liệu gì | Sequence diagram hoặc flow có nhãn actors/payloads |
| State đổi khi nào, điều kiện kết thúc | State diagram, timeline hoặc trace table |
| Race, ownership, cancellation | Interleaving có lanes và state từng bước; stepper khi hữu ích |
| Một thuật toán biến đổi input thế nào | Diagram kèm trace dữ liệu qua từng bước |
| Học khái niệm nào trước, module nào phụ thuộc nhau | Dependency graph và ví dụ đọc một nhánh |
| Bao nhiêu, đắt/chậm ở đâu | Biểu đồ có đơn vị và tỉ lệ, assumptions/evidence rõ |

Render bằng inline SVG/HTML/CSS hoặc renderer khả dụng. ASCII art hay Mermaid source trong code block chỉ là phần hỗ trợ, không thay diagram đã render. Mỗi visual trả lời một câu hỏi: quan hệ components, đường đi của payload hoặc state trước/sau bước quyết định; không mặc định chuyển từng dòng code thành một box hoặc gom mọi góc nhìn vào một hình. Mũi tên ghi ý nghĩa; boundaries, legend và thứ tự không phụ thuộc riêng vào màu.

Ví dụ: bài đóng gói theo budget có thể vẽ các item theo weight trong vùng capacity, giữ cùng item ở các frame trước/sau overflow; counter hiển thị riêng để phân biệt tổng dự kiến với item đã append. Bài về aliasing có thể vẽ hai reference trỏ vào cùng object để thấy vì sao mutation ảnh hưởng cả hai. Đây là cách chọn representation, không phải template bắt mọi recipe theo batching hoặc có nhiều hình.

## Diagram ↔ step-by-step ↔ code

Với algorithm/runtime flow:

1. Nêu input và state ban đầu, cùng assumptions ảnh hưởng đến kết quả. Phân biệt **trace của một scenario** với **flow tổng quát**: trace ghi rõ nhánh đang theo; flow tổng quát thể hiện các nhánh ảnh hưởng kết quả, điều kiện trên arrows và điểm gặp lại. Không vẽ một nhánh rồi mô tả như mọi input đều đi qua nó.
2. Đánh số các bước quan trọng trên hình. Phần walkthrough ngay cạnh/bên dưới dùng cùng số, cùng thuật ngữ.
3. Mỗi bước giải thích **ai thực hiện → nhận gì → làm gì → state/output đổi thế nào → vì sao bước tiếp theo xảy ra**. Nối rõ object/biến/method trong snippet với bước hoặc state trên hình; source link đơn lẻ không thay lời giải thích mối liên hệ. Người đọc lần được cả hai chiều từ hình tới code.
4. Theo cùng scenario đến kết quả quan sát được. Nếu dữ liệu đi theo nhánh nội bộ/out-of-band, vẽ riêng với line style, nhãn và legend; giải thích khác biệt với payload chính.
5. Đặt failure/edge case liên quan cạnh success case hoặc trong một trace đối chiếu. Chỉ ra bước phân nhánh, invariant bị vi phạm/được giữ, cách phát hiện và hệ quả.

Số bước theo mechanism, không cố định bảy bước. Với dependency map hoặc visual tĩnh không có trình tự thực thi, dùng hướng dẫn đọc và ví dụ đi qua quan hệ; không bịa runtime sequence.

Ảnh không có mũi tên tới một actor chưa chứng minh dữ liệu không thể bị lộ. Claims về boundary/security cần đối chiếu source, gồm đường return/error/log liên quan và giả định trust. Trình bày rõ phạm vi đã kiểm, không suy thành bảo đảm toàn hệ thống.

## Khi lượng và chi phí là bài học

Giữ tỉ lệ, đơn vị, axes và cùng scale khi so sánh. Nếu vùng quan trọng quá nhỏ, dùng thêm zoom có nhãn thay vì bóp méo tỉ lệ mà không nói. Phân biệt số đo thực, số tính từ assumptions và dữ liệu minh họa. Measurement có baseline, ngày, môi trường/workload và cách đo lại; không mượn số của một repo khác.

Nêu chi phí liên quan: số operations/requests, memory, CPU, I/O, latency, complexity, engineering effort hoặc vận hành. Không bịa monetary cost hay biểu đồ định lượng cho topic chỉ có quan hệ cấu trúc. Không gọi một phép tính là benchmark đã chạy. Failure case chưa quan sát phải ghi là phân tích/minh họa, không bịa sự cố production.

## Giữ đường đọc dễ nhất

Đường đọc cốt lõi đi theo câu hỏi của người đọc: thấy vấn đề/kết quả, hiểu mechanism rồi biết khi nào áp dụng. Không buộc mọi glossary, diagram và code thành các khối tách xa nhau theo một thứ tự cố định. Đặt giải thích khái niệm, hình, walkthrough và snippet liên quan gần nhau, kết lại bằng điều vừa hiểu. Full lab, proof và phân tích bổ sung có đường vào rõ nhưng không chắn đường tới kết luận. Giữ prerequisites và cảnh báo thiết yếu tại nơi cần dùng.

Tự đọc hình cùng caption trước prose/code: có nhận ra input, đối tượng nào đổi, vì sao đổi và output/quan hệ chính không? Nếu hình chỉ chép prose/code vào các box nối tiếp mà không làm rõ quan hệ hoặc state, đổi representation hoặc thêm một state view phù hợp. Sau đó kiểm walkthrough có bổ sung lý do thay vì chỉ chép labels. Không dùng số lượng SVG, màu sắc hoặc animation làm tiêu chí giàu visualization.

Stepper/animation chỉ thêm khi giúp theo dõi state. Có tiến/lùi/reset, nhãn keyboard-accessible và kết quả nhất quán khi đổi scenario. Bản tĩnh, captions và explanation vẫn đủ hiểu khi JavaScript không chạy. Kiểm lại hình, từng số bước, dữ liệu và code cùng nhau sau mỗi sửa đổi; không chỉ kiểm HTML có render.
