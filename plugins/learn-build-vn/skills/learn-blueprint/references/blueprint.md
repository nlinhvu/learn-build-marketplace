# Blueprint và catalogue thích nghi

Trang chính phải giúp user trả lời: product phục vụ ai, hệ thống gồm gì, request/data đi đâu, code được release thế nào, chất lượng cần đạt và bước tiếp cần học gì. Giữ chi tiết sâu trong sections mở rộng. Viết nội dung invariant/decision cần dùng ngay trên trang, thêm link source/ADR làm provenance. Dùng [learning-contract.md](learning-contract.md) cho root, câu hỏi và nội dung tự đủ.

## Catalogue

Nối catalogue outcomes với việc user tự làm được mà không cần AI coding agent. Tại product milestone, đánh giá enterprise acceptance và ownership toàn product theo contract chung; giữ gaps dù delegated implementation đã xong.

Link capability entries tới user stories đã trao đổi và scope status theo [project-memory.md](project-memory.md). Ghi actor goals, rules, edge cases ngay trong discovery, gồm candidate/deferred flows. Catalogue tóm tắt outcomes; story records giữ intent thay đổi theo thời gian. Không chờ có tutorial mới lưu story hoặc bịa walkthrough tương lai để điền đủ.

Mỗi mục có outcome/demo dự kiến, learning outcome gắn mechanism, technical prerequisite, learning prerequisite, target environment và quality concern liên quan. Nêu user sẽ tự giải thích/thay đổi/debug/vận hành được gì và kiến thức đó chuẩn bị cho architecture decision nào ở bước tiếp; giữ đường đi tới enterprise target đã chọn, không dừng catalogue ở local demo. Ghi language/framework/library/infra dưới nhãn Observed, Decided, Candidate hoặc Deferred khi biết; không điền stack cho đủ box. Command, exact file/symbol và exercise chỉ cần khi viết guide đến lượt.

Một tutorial thêm capability hoặc operational outcome demo được từ baseline rõ ràng, không phụ thuộc tutorial tương lai. Nó có thể kế thừa code của tutorial trước. Checkpoint là bước nhỏ có thay đổi/quan sát được; không nhất thiết tự tạo một capability độc lập. Tách tutorial nếu nhiều mechanism mới khiến user phải chọn khi chưa hiểu prerequisites.

Đếm baseline và conditional tutorials riêng. Hai alternatives loại trừ nhau không cùng trở thành commitment. Ghi ngày/assumptions của estimate và unknown có thể đổi tổng. Khi chưa đủ thông tin, vẫn cung cấp catalogue hữu ích theo phần đã biết.

Ví dụ minh họa: job API có create → status → recovery; kiến thức đi từ contract/data ownership → lifecycle → crash window/idempotency. Queue technology có thể chờ evidence về workload và recovery. Nếu mất dữ liệu đã vi phạm requirement hiện tại thì sửa scope hiện tại, không tự đẩy sang tương lai.

## Feedback vào blueprint

Khi chọn tutorial kế tiếp, dùng transition trong [learning-contract.md](learning-contract.md): đọc behavior/evidence và learning gap ở tutorial hiện tại, xác định decision nào thật sự đến hạn và prerequisite nào cần experiment trước. Catalogue vẫn giữ toàn cảnh tới enterprise target với future outcomes, dependencies và conditional branches ở mức preview; chỉ chi tiết implementation cho tutorial đến lượt đủ cơ sở. Không lấp unknown bằng stack commitment.

Sau tutorial hoặc khi assumption bị phủ định, đối chiếu capability thật, evidence, kiến thức còn vướng và dependency của bước sau. Có thể thêm/bỏ/tách/gộp/đổi thứ tự tutorial. Chỉ sửa phần bị ảnh hưởng; không sinh lại toàn bộ chương trình mỗi vòng.

Chưa có decision mới thì ghi candidate/impact, đánh dấu target cũ cần xem lại. Khi user chọn, cập nhật target/catalogue và lưu choice với authority/supersession links theo project-memory.md. Giữ rationale trước cùng rejected alternatives. Không hạ requirement theo implementation sai. Giữ một link active tutorial, với progress/evidence chi tiết tại đó, tránh checklist cạnh tranh.
