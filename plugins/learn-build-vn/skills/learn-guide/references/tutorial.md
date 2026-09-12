# Contract của tutorial hiện tại

## Phần mở đầu

Nêu capability tăng thêm, demo và learning outcomes, baseline/source đã đọc, prerequisite, environment và giới hạn hiện tại. Cho lệnh setup/start/stop cần thiết, dữ liệu an toàn và trạng thái ban đầu để lặp lại walkthrough. Khi dùng version/tool mới, kiểm compatibility với project; không tự upgrade chỉ để có latest.

## Checkpoint có thể làm theo

Mỗi checkpoint trả lời tại chỗ:

1. Vấn đề đang giải quyết và vì sao bước này đứng ở đây.
2. Context/glossary và nội dung cụ thể của invariant/decision tại chỗ. Với mechanism/architecture mới: visual đã render và worked example input → các bước/state trung gian → output gắn symbol thật, gồm branch/failure liên quan; giải thích vì sao thuật toán hoặc boundary vận hành như vậy.
3. Exact path, symbol và code cần thêm/thay/xóa. Dùng đoạn hoàn chỉnh ở scope chỉnh sửa hoặc diff có anchor rõ; không để ellipsis che logic cần implement. Liên kết full source để đối chiếu; phần code và explanation thiết yếu vẫn có ngay trong checkpoint.
4. Command/thao tác chạy, expected UI/API/CLI/state/log và cách nhận biết failure. Phân biệt expected với observed; ghi baseline/environment cho evidence đã chạy.
5. Troubleshooting từ symptom về nguyên nhân khả dĩ, bước kiểm và xử lý; code có thể khác guide sau implementation.

Checkpoint chưa nhất thiết là capability độc lập, nhưng phải có bước quan sát/kiểm chứng phù hợp. Tutorial hoàn chỉnh phải demo được không cần code ở tutorial tương lai.

Ví dụ: tutorial thêm status lookup cho job API đang có create. Checkpoint giải thích lifecycle → thêm lookup bằng API thật của store → wire GET handler → QA known/unknown id. Retry và durable store chỉ là preview nếu chưa đến hạn; không buộc user chọn queue trước status lookup.

## Decision và quality tại nơi liên quan

Decision đã chốt được trình bày đầy đủ nội dung/rationale tại nơi dùng, cùng context/evidence, trade-off, cost/security, reversibility và trigger xem lại. Nếu cần user quyết định, theo [learning-contract.md](learning-contract.md): một câu hỏi và một HTML riêng, trình bày trước khi hỏi, freeform và chờ câu trả lời. Dùng tag long-term/cost/short-term/code ít thay đổi nhất đúng ý nghĩa; không buộc tạo nhiều alternatives cho routine choice.

Gắn quality vào thay đổi thật: security/trust/secret boundary, correctness/data, timeout/retry/recovery, telemetry, cost driver/bounds, build/CI/CD/IaC và release/rollback khi liên quan. Nêu control nào cần ngay, gap nào chưa đạt và environment đã kiểm. “Enterprise” là requirement cùng evidence, không phải quota patterns hoặc số diagram.

## Manual QA và learning

Dùng user-story records theo [project-memory.md](project-memory.md) làm acceptance inputs. Phát triển walkthrough của capability hiện tại trước dependent implementation instructions; future flows chỉ giữ detail đã biết. Map story tới checkpoints, giữ actions/expectations thiết yếu ngay trong tutorial. Lưu thay đổi requirement và lý do trong story/discussion records; internal-only change không có actor flow dùng operational/verification scenario.

Walkthrough gồm actor, setup/reset, thao tác thật theo thứ tự, expected/actual, một negative/failure path phù hợp, evidence, cleanup/rollback. Dùng UI thật cho UI claim; curl/CLI cho API/process; cloud tools theo scope cho infra. Agent có thể chạy QA hoặc hướng dẫn user khi thiếu quyền/tool.

Manual QA phải còn là walkthrough quan sát behavior thật khi bỏ các lệnh test runner; assertions/unit tests là checks bổ sung.

Áp dụng independent-ownership loop trong [learning-contract.md](learning-contract.md). Có cơ hội hữu ích để vận dụng mechanism ngoài việc copy ví dụ: behavior variation nhỏ, fault diagnosis hoặc recovery bằng công cụ được hướng dẫn. Nêu observable outcome và hints/explanation tùy chọn; user có thể từ chối hoặc yêu cầu hỗ trợ thêm. Tách product/QA evidence với phần user tự làm và mức assistance cần.

## Kiểm artifact và đường lỗi trước handoff

Với code/snippets mới hoặc đã đổi, kiểm phần runnable có rủi ro bằng chính code trích từ HTML cuối cùng trong scratch/baseline cô lập khi tools khả dụng. Compile kiểm cú pháp/API; chạy scenario cần thiết kiểm behavior. Với wire output như JSONL, đưa nhiều event qua parser tương ứng để bắt lỗi delimiter/escaping. Không bắt prebuild toàn product hoặc gọi service có phí ngoài scope; phần không chạy được phải ghi rõ phạm vi chưa kiểm, không coi ready nếu uncertainty phá checkpoint phụ thuộc.

Trace cả nhánh thành công và failure qua các layer thật: callback phát error event có consume exception hay exception vẫn thoát caller; terminal, transcript/state và exit code nào thực sự xảy ra? Fake provider trả error như data không chứng minh provider thật ném exception được xử lý. Chọn reproduction nhỏ cho đường lỗi khác semantics đó, giữ acceptance khi fail. Manual walkthrough ghi đúng network/account prerequisite; prompt model không đảm bảo tool call hay input lỗi cụ thể, nên nêu expected có điều kiện và cách kích hoạt local có kiểm soát khi cần quan sát failure. Không gắn nhãn offline cho đường còn gọi service.

## Sync và handoff

Khi implement khác guide, sync snippets/commands/diagrams/QA/explanation theo facts và requirements. Code sai acceptance thì tutorial còn chưa đạt; không đổi expected để che bug. Thay đổi design đáng kể quay về discussion; quyết định đã chốt mới cập nhật target/next tutorials. Future guide chỉ viết khi đủ đầu vào.

Khi sync, bỏ editorial history khỏi tutorial, thay claim sai bằng explanation đúng của baseline/target hiện hành. Giữ discussion, user corrections và reasoning bị superseded trong linked records theo project-memory.md. Explainer không thay prerequisite tại chỗ. Cuối bài nêu kiến thức user có thể dùng để quyết định bước tiếp, không chỉ dẫn ID ở trang khác.

Handoff theo transition trong [learning-contract.md](learning-contract.md): gắn một behavior/trace cụ thể với mechanism cần reasoning và decision nó chuẩn bị. Với phần chưa thực hành, viết hoạt động dự kiến và evidence còn thiếu; không viết hộ câu trả lời của user.
