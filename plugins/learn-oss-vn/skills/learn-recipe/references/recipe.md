# Từ kỹ thuật trong repo đến bài học áp dụng được

## Đọc đủ mechanism

Theo một input từ entrypoint qua các calls, state/data ownership và output; xem tests/failure branches thay vì chỉ đọc một function. Với conventions/practices, đối chiếu CONTRIBUTING/config/CI và các ví dụ đại diện để phân biệt quy tắc project với lựa chọn cục bộ. Không suy luận ý định maintainer khi chỉ có implementation.

Xác định một kết quả học rõ và prerequisites thực sự cần. Nếu topic quá rộng, tách thành recipes theo insight; không viết toàn bộ testing/concurrency trong một bài. Giữ glossary và giải thích nền cần thiết tại chỗ để người mới tiếp cận được.

## Nội dung bài

Tổ chức theo câu hỏi người đọc cần giải quyết, không theo toàn bộ thứ tự khảo sát của agent. Mỗi section có một câu hỏi trung tâm và dẫn tự nhiên sang câu hỏi tiếp theo; heading nói rõ điều sẽ hiểu, không nhất thiết viết dưới dạng câu hỏi. Chọn điểm vào theo topic: API có thể mở bằng usage example ngắn, algorithm bằng input/output trực quan, convention bằng annotated diff. Không bắt người đọc học hết glossary hoặc interfaces trước khi thấy kỹ thuật giúp ích thế nào.

Trong section, đặt explanation, diagram, worked example và code phục vụ cùng câu hỏi gần nhau. Trước hoặc sau snippet, chỉ rõ object/biến/method nào tương ứng với bước hay state trên hình; không để người đọc tự nối từ tên class. Section chỉ dùng những thành phần giúp trả lời câu hỏi đó, không lặp một bộ mục cố định cho mọi section.

Phân biệt hai đường đọc trong cùng HTML:

- **Hiểu mechanism:** vấn đề, glossary cần dùng, visual worked example, code cốt lõi, kết luận và giới hạn quyết định cách áp dụng. Người đọc theo được từ input tới output mà chưa cần build repo.
- **Tự kiểm và đào sâu:** full lab, setup, evidence, proof, edge cases bổ sung và contribution checks. Có link/summary rõ để tìm và quay lại; code thiết yếu vẫn đầy đủ trong HTML. Không giấu prerequisite hoặc cảnh báo làm thay đổi nghĩa của mechanism trong phần tùy chọn.

Bao phủ các nội dung sau trong những section phù hợp; đây không phải thứ tự hay bộ headings bắt buộc:

1. **Vấn đề và trực giác:** điều đang khó, vì sao đáng học, scenario cụ thể và kết quả có thể tự đạt được. Nêu repo/baseline và prerequisites.
2. **Glossary + mechanism:** theo visual-explanation.md; giải thích khái niệm khi xuất hiện và dùng cùng dữ liệu giữa visual, numbered flow, walkthrough và code. Giải thích invariant/điều kiện đúng ngay nơi dùng, không chỉ đưa link.
3. **Code thật:** paths/symbols và excerpts đủ context; mô tả wiring/callers, state transitions và boundaries. Ghi rõ phần rút gọn/minh họa; không làm nó trông như code upstream nguyên vẹn.
4. **Thử và quan sát:** cho thấy một lần chạy/kiểm nhỏ nhất có ý nghĩa trước suite mở rộng hoặc mutation testing; dùng lại setup/fixture, không bắt tạo thêm một implementation giả chỉ để bài trông dễ hơn. Code thực hành đầy đủ trong HTML, setup, commands, expected observations, failure diagnosis, giới hạn tài nguyên và cleanup. File tải xuống chỉ là tiện ích thêm. Đối chiếu predictions với evidence thực thi nếu đã chạy.
5. **Trade-offs và kết luận:** so alternatives thực sự liên quan trên cùng điều kiện; nêu tại sao chọn/không chọn, khi nào không dùng, chi phí và giới hạn. Dimension không áp dụng thì nói ngắn gọn, không bịa số/chart để lấp mục.
6. **Áp dụng và contribute:** nguyên lý tái sử dụng so với convention/constraint riêng; một variation hoặc change nhỏ gợi ý, checks cần chạy theo repo, và bước cần trao đổi với maintainer khi liên quan. Không tự nhận issue đang mở hoặc hứa PR được chấp nhận.

Đặt kết luận cốt lõi ngay sau worked example/code liên quan, không bắt đi qua full lab mới biết nên nhớ gì. Phần chuyên sâu giải thích thêm, không lặp lại cùng walkthrough dưới nhiều headings. Không đặt quota thời gian đọc, số diagram hoặc số test thay cho teaching quality.

Không phải mọi recipe đều có runtime algorithm: conventions hoặc DevOps practice có thể dùng worked example/config diff/CI flow, nhưng vẫn cần giải thích causal reasoning, giới hạn và cách kiểm. Không ép mọi topic có benchmark hay security audit riêng.

## Kiểm theo loại kỹ thuật

- **Testing:** nêu behavior/invariant mà test bảo vệ, fixture/setup và failure nào nó bắt được. Dùng existing tests làm evidence đúng phạm vi; test bổ sung phải mang nhãn, không nhận upstream đã kiểm case đó.
- **Benchmarking/resource efficiency:** nêu workload/input size, baseline so sánh, môi trường/version, warm-up/repetitions và variance phù hợp, tài nguyên/chi phí và cách đo lại. Phân biệt measured, calculated, illustrative; chưa có runtime thì viết protocol và giới hạn, không tạo measured results. Một lần đo không chứng minh scalability.
- **Concurrency/scalability:** trace interleavings, ownership, bounds/backpressure, cancellation và failure propagation khi liên quan. Phân biệt phạm vi một operation, một item, batch và process lifetime theo source; không mở rộng lời hứa correctness vượt boundary đã kiểm.
- **Security:** xác định trust/data boundary, dữ liệu nào đi đâu và các paths return/error/log liên quan; nêu assumptions. Mô phỏng trên fixture local được phép, không tự quét service bên ngoài hoặc đưa secrets vào bài.
- **Observability/DevOps/developer practices:** nối config/code với tín hiệu quan sát, đường diagnosis hoặc delivery/rollback; phân biệt cấu hình dự định với pipeline/deployment thực sự đã chạy. Commands có environment và scope rõ.

Đây là các câu hỏi phân tích có điều kiện, không phải quota mục phải điền trong mọi bài. Thực thi chỉ khi an toàn và được phép; thiếu công cụ thì ghi rõ phần chưa kiểm, vẫn giải thích phần có evidence.

## Theo câu hỏi của người học

Nếu người dùng phản biện hoặc source mới làm thay đổi kết luận, kiểm lại bằng evidence rồi cập nhật bài hiện hành cùng diagrams/code/tests liên quan. Giữ correction và lý do cũ trong history records. Nội dung chia sẻ không kể lại lỗi biên tập hoặc thông tin riêng của người học.

Có thể đề xuất variation/diagnosis nhỏ để áp dụng, với gợi ý và lời giải mở rộng. Tôn trọng yêu cầu không quiz, không bắt chạy thêm hoặc xin approval lại cho routine work đã được giao. Phân biệt người dùng tự làm, người dùng báo đã làm và agent thực hiện; không suy full understanding từ checks pass.
