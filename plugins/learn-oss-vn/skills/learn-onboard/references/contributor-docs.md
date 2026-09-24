# Bộ docs giúp developer contribute

Đọc khi người dùng cần hiểu codebase để sửa hoặc mở rộng project, gồm glossary, patterns và best practices. Output bổ sung kiến thức contributor cho bộ usage/reference docs. Contributor onboarding chưa cấp quyền sửa source hoặc gửi PR; có thể viết walkthrough thay đổi minh họa trong docs với evidence và lệnh kiểm phù hợp.

## Tổ chức kiến thức theo nhu cầu contributor

Giữ cùng docs root, source baseline, navigation và coverage với phần hướng dẫn sử dụng. Với yêu cầu cả hai, entry page có hai đường đọc rõ: sử dụng project và hiểu code để contribute. Tạo files chứa kiến thức thực chất, không chỉ trang contribution instructions link tới các tài liệu chưa viết.

| Trang/nhóm gợi ý | Nội dung cần giúp người đọc làm được |
| --- | --- |
| `glossary.html` | Hiểu domain terms và từ riêng của codebase; phân biệt các khái niệm dễ nhầm qua ví dụ và symbols thật |
| `architecture.html` | Tìm module/subsystem chịu trách nhiệm, hướng dependencies, public API/SPI và internals; lần một runtime flow qua boundaries |
| `patterns/<pattern>.html` | Nhận ra pattern đang giải quyết vấn đề gì, các roles ánh xạ vào classes/methods nào và áp dụng/mở rộng nó đúng cách |
| `practices/<topic>.html` | Hiểu conventions/invariants cần giữ khi sửa code, rationale có evidence, ví dụ phù hợp và counterexample gây lỗi |
| `contributing/index.html` | Chọn change surface và test scope cho một loại thay đổi, chuẩn bị build/test, lần code và kiểm regression |

Điều chỉnh/gộp trang theo quy mô; không tự bịa đủ một taxonomy cố định. Đưa các concepts cần thiết ngay cạnh usage examples, rồi link tới glossary/contributor detail; không bắt người đọc học internals trước Getting Started. Catalogue và recipe hiện có có thể cung cấp đường học sâu hơn nhưng không thay nội dung cốt lõi của bộ docs.

## Glossary gắn với code và lifecycle

Mỗi khái niệm cốt lõi có nghĩa dễ hiểu, vai trò, ví dụ, source symbol và quan hệ với khái niệm khác. Phân biệt thuật ngữ chung với nghĩa riêng trong project; những cặp dễ nhầm cần ví dụ đối chiếu, không chỉ hai định nghĩa từ điển. Diagram thể hiện quan hệ metadata/instance, interface/implementation, owner/resource hoặc thời điểm lifecycle khi điều đó quyết định behavior.

Ví dụ ở một container DI, cần kiểm source để phân biệt metadata mô tả object với object đã khởi tạo, hoặc hook sửa definitions với hook xử lý instances. Đây là hướng phân tích, không phải kết luận áp đặt lên mọi repo. Giữ glossary tra cứu được qua stable anchors và links từ các trang sử dụng thuật ngữ đó.

## Patterns phải được chứng minh

Tìm pattern từ cộng tác giữa các symbols và behavior quan sát được. Trình bày vấn đề → roles và source anchors → trace có input/state/output → điểm mở rộng → constraints/trade-offs. Một class mang tên `Factory`, `Adapter` hay `Template` chưa chứng minh design pattern tương ứng. Phân biệt pattern phổ biến, idiom riêng của project và cách diễn giải của tác giả.

Nếu nhận định pattern/convention xuất hiện rộng, đối chiếu nhiều usages độc lập và exceptions có liên quan; một example chỉ chứng minh example đó. Giải thích điều contributor cần giữ khi thêm implementation mới: contract, ordering, lifecycle, ownership, error propagation hoặc concurrency tùy source. Counterexample chỉ ra invariant bị vi phạm và test/trace giúp phát hiện; không bịa regression đã xảy ra.

## Best practices và conventions có phạm vi

Tách rõ ba loại nhận định: rule được project quy định, practice thấy trong source/tests và đề xuất của tác giả. Dẫn evidence tương ứng, nêu phạm vi áp dụng và exceptions. Không gọi mọi implementation hiện có là best practice hoặc nâng convention của project thành quy tắc phổ quát.

Ưu tiên điều ảnh hưởng tới thay đổi thực tế: API/SPI compatibility, extension vs override, nullability, resource lifecycle, error handling, thread safety, test fixtures và module boundaries khi có source hỗ trợ. Không thêm một checklist generic chỉ để đủ đề mục. Best practice phải trả lời được: làm gì, vì sao, áp dụng ở đâu, vi phạm thì quan sát gì và kiểm bằng cách nào.

Khi docs folders bị loại trừ, chỉ dùng project instructions và các nguồn code/comments/tests/build metadata được phép. Giữ các runtime/project instructions bắt buộc; thiếu rationale từ docs đã loại trừ thì ghi unknown. Không đọc lại reference guide online để bổ sung convention hoặc nhớ tên pattern rồi gán vào code.

## Walkthrough để contribute

Chọn một thay đổi nhỏ đại diện cho subsystem đã khảo sát, chẳng hạn thêm một implementation của SPI hoặc kiểm một nhánh validation. Tài liệu chỉ rõ điểm vào, đường gọi, files/symbols cần xem, behavior trước/sau mong muốn, invariant cần giữ và vị trí đặt regression test. Chỉ gọi patch/example là đã kiểm nếu có thực thi tương ứng; một hướng dẫn contributor có thể hoàn chỉnh mà chưa thực hiện patch vào repo gốc.

Lấy commands từ build/CI và tests thật, phân biệt test hẹp với full suite, public API regression với integration checks. Build toolchain và test prerequisites theo baseline; không mặc định lệnh toàn repo chạy được khi docs modules đã bị xoá. Nêu giới hạn kiểm chứng và phần maintainer policy không có evidence. Nếu user đang cân nhắc architecture/provider cho application của họ, giữ lựa chọn pending; docs có thể mô tả alternatives mà không quyết định thay họ.

Trước bàn giao, thử đường đọc glossary → architecture → pattern/practice → change walkthrough → regression test. Contributor phải tìm được chỗ thay đổi và hiểu vì sao làm vậy từ bộ docs; danh sách symbols hoặc links đơn thuần chưa đủ. Coverage ghi riêng usage docs và contributor knowledge đã viết/kiểm, không dùng độ phủ một bên để nhận hoàn thành bên kia.
