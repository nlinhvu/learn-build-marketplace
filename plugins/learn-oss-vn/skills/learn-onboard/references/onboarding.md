# Documentation từ source cho người mới

## Xác định đầu vào và phạm vi

Ghi repo/commit hoặc version, local changes liên quan, source root và output root. Mặc định docs root là `<learning-root>/onboarding`; giữ đường dẫn canonical đã có hoặc người dùng chỉ định. Xác định người đọc từ yêu cầu: developer muốn dùng library/framework, người vận hành CLI/service, hay contributor muốn sửa implementation. Thiếu lựa chọn biên tập thì chọn đường bắt đầu đơn giản có evidence và nói rõ assumptions; không biến onboarding thành cuộc phỏng vấn kiến trúc product mới.

Khi source là bản copy không có `.git`, `git -C <source-root> rev-parse HEAD` có thể đi lên và trả commit của repository cha. Chỉ dùng Git HEAD làm source baseline khi `git rev-parse --show-toplevel` trỏ đúng source root; nếu không, lấy commit từ provenance đáng tin của fixture/checkout gốc hoặc ghi unknown. Không dựng public permalink với commit chưa chứng minh; tạm dẫn relative path/symbol trong records và trang.

Đọc project instructions và inventory trong phạm vi được phép trước khi viết. README và docs có thể là nguồn bổ sung nếu được phép; khi thiếu chúng vẫn tiếp tục từ source. Với chế độ loại trừ docs, lập tập paths được phép trước content search, đặt exclusions tương đối theo search root, tránh search toàn repo rồi mới lọc output. Không dùng symlink, generated site, cache, `git show` hoặc docs online để lấp lại nội dung bị loại trừ. External dependency cần tra cứu thì dùng nguồn chính thức đúng version trong phạm vi được phép; nếu bị cấm mọi nguồn ngoài repo, ghi unknown thay vì tra cứu.

Docs framework khác có thể làm mẫu information architecture khi được phép. Chỉ dùng mẫu để hiểu loại câu hỏi và cách điều hướng; taxonomy thực tế phải rút từ project đích. Không bê nguyên danh mục Spring vào một CLI, database hoặc frontend library. Tài liệu được sinh là bản diễn giải có source evidence, không phải official documentation hay phục hồi nguyên văn nội dung đã mất.

## Khảo sát từ public surface vào implementation

Tìm các nguồn sau theo cấu trúc thực tế, không cần đọc mọi file tuần tự:

| Câu hỏi cần trả lời | Evidence nên tìm |
| --- | --- |
| Project giúp ai làm gì? | Public entry points, API comments, examples và tests thể hiện input/output; README được phép đọc |
| Cài và khởi động thế nào? | Package/build manifests, dependency management, toolchain, launch entry point và examples chạy được |
| Những capability nào có thật? | Exported APIs, modules, adapters, registries và tests; module tồn tại chưa đủ chứng minh tích hợp hoạt động |
| Khái niệm nào cần hiểu? | Public types/contracts, ownership, lifecycle và đường đi của dữ liệu trong một use case |
| Cấu hình nào làm thay đổi behavior? | Config binding, defaults, validation, activation conditions, overrides và precedence |
| Khi lỗi thì kiểm gì? | Exceptions, validation branches, tests thất bại có chủ đích, logs và retry/timeout handling |
| Muốn mở rộng hoặc contribute thì đi đâu? | Extension interfaces, implementations tiêu biểu, test boundaries, build/CI và contribution instructions |

Từ inventory, lập task ledger theo [documentation-contract.md](documentation-contract.md): capability/use case → outcome → public API/config/test anchors → section trả lời → scope/depth/verification/next action. Ghi commit và relative path/symbol; không đưa paths máy cá nhân vào trang công khai. Trang có baseline cũ cần trạng thái stale nếu chưa kiểm lại.

Với mỗi capability cốt lõi, trace ít nhất một đường sử dụng từ entry point tới kết quả cùng điều kiện hoặc failure quan trọng. Với provider/plugin family, đọc contract chung và implementation đại diện để giải thích shared behavior; kiểm từng adapter trước khi gán cho nó capability, property hay guarantee riêng. Không suy rằng các adapters tương đương chỉ vì implement cùng interface.

Mục đích project cần đi từ vấn đề cụ thể tới kết quả và boundary: người dùng đang phải làm gì, project cung cấp phần nào, phần nào vẫn do application hoặc external service đảm nhiệm. Rationale về lịch sử/chiến lược chỉ trình bày như lời maintainer nếu có nguồn được phép; phần suy ra từ cấu trúc phải ghi là phân tích.

## Tổ chức bộ docs

Đường dẫn dưới đây là mặc định cho HTML, điều chỉnh theo quy mô và yêu cầu. Chỉ tạo trang có nội dung, dùng relative links giữa các trang và đặt đường quay lại entry page. Nội dung planned nằm trong coverage dưới dạng text, không có links tới file chưa tồn tại.

| Nhóm | Nội dung người đọc cần nhận được |
| --- | --- |
| `index.html` — Overview | Mục đích, audience, vấn đề/kết quả cụ thể, capability map dễ hiểu, boundaries và đường đọc tiếp |
| `concepts.html` — Concepts | Mental model, glossary tại chỗ và diagram giải thích components/data flow bằng cùng scenario |
| `getting-started.html` — Getting Started | Prerequisites, dependency/version, setup/config, code tối thiểu hoàn chỉnh, lệnh chạy, expected result và cách kiểm lỗi đầu tiên |
| `guides/<task>.html` | Tác vụ thực tế từ đầu đến cuối: khi cần, prerequisites, các bước, code/config, kết quả, lỗi/giới hạn và links tới reference |
| `reference/<capability>.html` | Public contract, options/configuration, defaults/conditions, behavior và extension points để tra cứu nhanh |
| `troubleshooting.html` | Triệu chứng → nguyên nhân có evidence → cách kiểm → hướng xử lý, không bịa incident hoặc lỗi chưa đọc |
| Contributor docs khi được yêu cầu | Glossary, architecture, patterns, practices và change/test walkthrough theo [contributor-docs.md](contributor-docs.md); cùng navigation với usage/reference |

Với yêu cầu rộng, Overview, Concepts và Getting Started là cửa vào bộ docs; task ledger quyết định các guides/reference cần hoàn thiện trên các public capability families, không chỉ đường sử dụng cốt lõi. Repo nhỏ có thể gộp trang; repo lớn tách theo capability và viết nhiều batch giữ nguyên phạm vi. Áp dụng chapter contract và acceptance trong [documentation-contract.md](documentation-contract.md). Yêu cầu chỉ một trang hoặc danh sách tasks cụ thể không tự mở rộng sang toàn project.

Trang Overview dẫn người đọc tới một kết quả đầu tiên trước khi yêu cầu hiểu internals. Guides tổ chức theo tác vụ, reference theo contract/capability, contributor map theo cấu trúc source. Không sinh một trang cho mỗi class hoặc mỗi folder nếu người dùng không cần tra cứu ở mức đó.

Trong reference, bảng configuration nên có key chính xác, type/units, default, điều kiện áp dụng, ý nghĩa và source anchor. Chỉ gọi là default khi đã kiểm effective behavior: giá trị initializer có thể bị constructor, environment, builder hoặc auto-configuration ghi đè. Phân biệt dependency cần thiết, điều kiện tạo component và cách override. Ghi optional/required dựa trên validation/contract, không đoán từ tên biến.

Upgrade/migration notes cần hai baselines hoặc deprecations/changelog có evidence. Khi chỉ có một checkout, có thể ghi deprecations quan sát được nhưng không dựng lịch sử version, lịch release, support policy hoặc compatibility matrix từ trí nhớ.

## Ví dụ đủ để bắt đầu

Chọn đường setup nhỏ nhất thể hiện đúng public API và phù hợp constraint người dùng. Dùng quy trình bootstrap trong [documentation-contract.md](documentation-contract.md) để người chưa cache artifacts có đường bắt đầu; version trong repo không chứng minh artifact đã có trên registry. Thiếu docs module hoặc dependencies là constraint cần kiểm/ghi rõ, không tự sửa build/source để che vấn đề.

Getting Started và guides chứa imports, dependency/config và entry point cần thiết; không đưa fragment rồi gọi là app chạy được. Giải thích mỗi bước tạo state/output gì và vì sao cần. Commands ghi working directory và prerequisites; thông tin nhạy cảm dùng placeholders hoặc environment variables. Nếu chọn một external provider để minh họa, ghi lựa chọn và yêu cầu dịch vụ, không suy thành khuyến nghị cho production hoặc tự tạo tài khoản/tốn phí.

Expected result cần phân biệt với output thực đã quan sát. Với output không xác định như model generation, kiểm shape/behavior hợp lý thay vì hứa đúng một chuỗi chữ. Mock/local stub có thể kiểm wiring hoặc contract; phải ghi rõ nó không chứng minh external integration. Thiếu runtime, dependencies hoặc credentials không ngăn viết các phần source-reviewed; ghi cụ thể điều chưa chạy.

Visual phục vụ câu hỏi của từng trang: capability map cho Overview, data flow có payload cho Concepts, trace khi lifecycle/callback khó hiểu. Reference đơn giản có thể chỉ cần bảng; không ép glossary/diagram/full lab vào mọi property. Nếu dùng format khác HTML, giữ liên kết, captions, code và evidence; kiểm bằng toolchain format đó khi có, không tự thêm Antora/build pipeline chỉ vì nhắc đến tài liệu Spring.

## Cập nhật và bàn giao

Kiểm đường đọc Overview → Getting Started → guide → reference và các links tới source/coverage. Đọc tài liệu như người chưa có chat: có hiểu project giúp gì, khởi động được theo các prerequisites đã nêu, biết chọn API và tự tra cứu lỗi không? Kiểm code trích từ output cuối, điều kiện config và giới hạn đã được thể hiện tại nơi sử dụng.

Lưu page IDs/paths, capability coverage, anchors, exclusions, baseline và validation evidence trong records; phần public chỉ giữ thông tin project hữu ích. Khi source đổi, đối chiếu anchors, dependencies và callers/config liên quan, cập nhật các trang bị ảnh hưởng và giữ lịch sử checks theo baseline. Không ghi đè catalogue `index.html` hoặc recipe hiện có khi thêm onboarding; docs entry riêng được link từ learning index. Nếu cả hai workflow cùng hoạt động, dùng chung records và links ổn định mà không đòi cài skill còn lại.
