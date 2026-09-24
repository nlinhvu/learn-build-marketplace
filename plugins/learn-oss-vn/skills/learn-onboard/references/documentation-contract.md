# Từ capability inventory tới developer reference dùng được

Đọc khi tạo/cập nhật bộ docs hoặc chapter hướng dẫn/tra cứu. Reference-quality là giúp độc giả chọn, sử dụng và chẩn đoán public capability ở baseline; không đo bằng số trang, số symbols hay giống mục lục một framework khác. Dùng cấu trúc dưới đây trong coverage/records và trong nội dung, không chỉ như checklist nhớ trong đầu.

## 1. Task ledger là phạm vi công việc

Với yêu cầu một chapter/trang, ledger chỉ chứa task của chapter đó. Với yêu cầu bộ documentation cho project, đối chiếu inventory public APIs/modules, configuration/registration, examples/tests và build entry points để tìm các capability families. Chọn task phổ biến từ evidence về cách project được dùng, cùng các lựa chọn/failure quyết định dùng đúng; tránh chỉ chọn subsystem quen thuộc hoặc dễ viết. Deployment, integrations, testing và operations thuộc inventory khi source có public surface tương ứng. Không áp taxonomy cố định cho mọi project.

Trước khi khóa acceptance set của một site rộng, lập crosswalk family ↔ public modules/API/config/tests: mỗi family có public surface phải có các câu hỏi sử dụng/tra cứu tương ứng hoặc một exclusion có căn cứ ngoài việc “chưa viết”. Đặc biệt tìm các family chỉ hiện ở SPI, auto-configuration, test support hoặc operations chứ không xuất hiện ở đường first-run. Một câu hỏi kiểu “hiểu tools” không thay cho các outcome độc lập như đăng ký, quyền exposure, thực thi trực tiếp, context/errors và loop limits. Nếu reviewer sau đó tìm được câu hỏi nguồn bị bỏ sót, sửa inventory/denominator và giữ nó in scope; tỷ lệ trên danh sách tự chọn ban đầu không chứng minh target đã đạt.

Mỗi hàng là **một câu hỏi/tác vụ của developer**, không chỉ một folder hoặc class. Với family rộng, tách các việc có outcome độc lập (chọn/wire biến thể, thực hiện đường phổ biến, quyết định defaults/precedence, xử lý failure, tự kiểm) thành các hàng riêng khi một câu trả lời không thật sự bao phủ tất cả. Đối chiếu lại public API/config/tests để phát hiện những việc bị gộp hoặc bỏ sót trước khi coi inventory đã đủ; một ví dụ đại diện không biến mọi quyết định trong family thành actionable.

| Trường | Nội dung cần ghi |
| --- | --- |
| Family / task / audience | Capability, điều developer muốn làm hoặc quyết định, người dùng/contributor |
| Outcome / acceptance | Kết quả hoặc quyết định cụ thể; độc giả sẽ kiểm đúng/sai bằng gì |
| Scope / reason | In scope hoặc user-excluded, với lý do thật. Chưa đọc/chưa viết hoặc đang bị chặn vẫn giữ in scope |
| Evidence | Public entry point và source/config/test symbols theo baseline; unknown nào ảnh hưởng task |
| Answer location | Trang + section/anchor đã tồn tại; task chưa viết để trống, không tạo link giả |
| Depth | Absent, orientation, actionable hoặc stale; ghi phần task còn thiếu |
| Content blocker | Thông tin/prerequisite còn thiếu khiến task chưa đạt acceptance; để trống khi chỉ chưa chạy được phép kiểm |
| Verification | Source-reviewed, syntax-checked, compiled, runtime-verified, integration-verified theo evidence thực; có baseline/command/result hoặc not attempted/blocked |
| Next action | Bước cụ thể để đưa task tới acceptance hoặc xử lý blocker |

**Actionable** nghĩa là task có prerequisites/setup, hướng dẫn hoặc decision criteria, kết quả/failure và cách tự kiểm đủ context. Một trang giới thiệu tên API hoặc trỏ độc giả sang source để tự tìm cách làm vẫn là orientation. Độ sâu tài liệu và execution evidence độc lập: ví dụ source-reviewed có thể đủ hướng dẫn nhưng chưa được compile; thiếu cách chuẩn bị dependency thì task setup vẫn chưa actionable.

Family rollup nêu các task đã đạt và còn thiếu; một task hoàn chỉnh không đại diện cho toàn family. Với adapter/provider families, mô tả contract chung một lần, rồi bảng variant ghi khác biệt đã kiểm, setup riêng và unsupported/unknown. Chỉ viết các guide riêng khi thay đổi cách dùng hoặc behavior; không nhân bản cùng prose cho mọi implementation. Coverage mỗi adapter chỉ được nhận trong phạm vi evidence của nó.

Public coverage dùng bảng rút gọn dễ đọc gồm task, trạng thái, trang và giới hạn. Records giữ source anchors/checks/next actions chi tiết để resume; public docs không phụ thuộc records riêng mới dùng được.

## 2. Chapter contract: câu trả lời nằm trong tài liệu

Guide và reference có thể là hai phần cùng chapter hoặc hai trang liên kết. Không cần một file cho mỗi trường; thông tin áp dụng chung được link tới section nội bộ cụ thể. Mỗi task trong ledger phải lần được đến câu trả lời tương ứng.

**Guide theo tác vụ:**

1. Khi nào cần, kết quả muốn đạt và lựa chọn public API; nếu có alternatives quan trọng, giải thích khi chọn mỗi cách.
2. Prerequisites và setup thật: dependencies/toolchain/config, cách chuẩn bị artifacts/services/fixtures, working directory và entry point. Link tới setup chung đã đủ thông tin thay vì giả định đã có cache.
3. Code/config đủ thực hiện task, imports và bước chạy; giải thích input → state/output, đặt khái niệm cần hiểu ngay cạnh bước dùng nó.
4. Expected result và cách kiểm; ít nhất failure/edge case quyết định dùng đúng, triệu chứng, nguyên nhân, cách chẩn đoán và xử lý. Example dùng external service có local verification boundary rõ.
5. Giới hạn/lifecycle/cleanup cần thiết, link tới contract/configuration reference và extension/contributor detail liên quan.

**Reference để tra cứu:**

| Câu hỏi tra cứu | Nội dung source-grounded |
| --- | --- |
| Chọn API/implementation nào? | Public entry points, prerequisites/capabilities, cách wire/register, khác biệt quyết định lựa chọn |
| Gọi như thế nào? | Input/output và nullability/validation; trigger thực thi, eager/lazy, sync/async/stream nếu có; terminal/cancellation/cleanup boundaries |
| Cấu hình nào có hiệu lực? | Key/type/units, required/default, activation conditions, scope và precedence giữa defaults/builder/request/environment theo implementation |
| Ai giữ state và resources? | Ownership, lifetime/scope, ordering, concurrency/isolation, resource acquisition/release và constraints của extension |
| Khi nào khác happy path? | Exception/result/error policy, retries/limits, rollback/partial effects; cách nhận biết và lựa chọn cách xử lý |
| Làm sao thử hoặc mở rộng? | Snippet tối thiểu đủ context hoặc link local tới guide, expected observation/test assertion, extension point và source symbol đúng baseline |

Chỉ dùng các dimensions có liên quan tới capability; không bịa concurrency hoặc streaming cho API không có chúng. Khác biệt dễ dùng sai cần ví dụ đối chiếu hoặc decision table, không chỉ định nghĩa tên option. Property reference kiểm effective behavior ở nơi áp dụng, không chỉ đọc initializer. Glossary nối các thuật ngữ này với scenario/symbols và được cập nhật khi mở rộng families.

Với fluent API, trace từ method chọn mode (`call`, `stream`, `build`, v.v.) qua response/spec wrapper tới terminal/subscription và chỗ tạo side effect thật trước khi nói một request “đã chạy” hay “đã có response”. Snippet đúng không cứu một câu giải thích sai ranh giới thực thi; reviewer phải kiểm riêng prose contract này.

Với claim default so với per-request, đặc biệt “thay thế”, “tắt”, “chỉ còn” hoặc giới hạn quyền gọi, trace cả lúc tạo/copy request, mutator và lúc resolve/execute; đối chiếu test khi có. Một request method thêm phần tử vào list không chứng minh nó xóa defaults được copy từ builder. Nếu chưa chứng minh được merge/override ở toàn đường đi, ghi unknown hoặc thu hẹp claim, không dùng một ví dụ chạy được làm bằng chứng loại trừ các defaults khác.

Source anchors đặt cạnh contract/decision quan trọng, ưu tiên symbol cụ thể và line permalink khi ổn định theo commit. Link là bằng chứng để kiểm, không thay lời giải thích trong chapter. Practices của application khác với implementation/contributor patterns; cần cả hai khi task yêu cầu, không dùng độ sâu contributor để bù usage còn thiếu.

## 3. Bootstrap và kiểm chứng ví dụ

Đọc Getting Started như developer có toolchain cần thiết nhưng **chưa có artifacts riêng của project**. Chỉ version trong manifest và dependency declaration chưa đủ tạo đường khởi chạy.

- Nếu dùng artifact đã phát hành: xác định version/repository phù hợp và cách resolver lấy dependencies trong phạm vi nguồn/quyền cho phép. Không đổi sang version khác để nhận đã kiểm checkout hiện tại.
- Nếu dùng snapshot/local build: ghi prerequisites, command/cwd, modules và cách install/link artifacts mà app mẫu dùng. Kiểm entry point build còn hợp lệ với tập source được cấp.
- Với build tool tách nguồn tải dependency và plugin (như Maven `<repositories>` và `<pluginRepositories>`), kiểm cả đường resolve plugin mà command first-run gọi từ cache rỗng. Manifest parse được hoặc reactor compile một phần không chứng minh app mẫu chạy; ghi rõ bước nào hoàn tất và postcondition tương ứng.
- Nếu docs module đã bị loại làm build entry point không hợp lệ: xem build metadata để tìm cách chọn modules/tasks hoặc kiểm hẹp được hỗ trợ. Có thể dùng scratch copy và ghi rõ mọi điều chỉnh chỉ phục vụ kiểm tra; không sửa source gốc hoặc khôi phục docs bị loại. Lệnh chưa chạy là candidate command, không phải lệnh đã chứng minh hoạt động.
- Nếu chưa xác định được đường chuẩn bị dependencies: ghi content blocker ở task setup, vẫn viết/kiểm phần source-grounded khác. Nếu đường setup đã mô tả đủ nhưng thiếu network/toolchain/service để chạy kiểm: ghi verification blocked cùng nguyên nhân, không tự hạ độ sâu reference. Không đổi thiếu hướng dẫn dependency thành prerequisite mơ hồ “hãy cache trước”, và không gọi first-run đã hoàn tất khi setup còn content blocker. Thiếu credentials không chặn reference hoặc local fixtures; cũng không cấp quyền gọi dịch vụ tốn phí.

Trích code từ artifact cuối, giữ dependency version và context trong bài để kiểm. Khi guide bảo thêm dependency vào một app/POM mẫu được dẫn link, ghép đúng snippet public vào bản sao app đó và kiểm model/build sau khi ghép; dependency không có version chỉ hợp lệ nếu app thực sự import BOM hoặc dependency management tương ứng. Ghi riêng parser, type/compile, local runtime/tests và external integration; runtime của stub chỉ chứng minh boundary nó thực thi. Commands và kết quả quan sát có log trong records; public example ghi expected/observed phù hợp. Một snippet chạy bằng dependencies khác hoặc bản scratch khác không chứng minh snippet bàn giao.

Với setup command biến đổi files/config, trích và decode **đúng block từ artifact cuối**, không kiểm bản string/template trước render rồi suy cho bản public. Chạy block đó trên fixture/scratch độc lập đến postcondition trước khi dùng cho build: file/module/key nào phải còn hoặc mất, phần nào phải giữ nguyên. Nếu shell block gọi interpreter khác (`python -c`, Perl, `sed`, v.v.), kiểm cả cú pháp và hiệu ứng của interpreter đó; `bash -n` chỉ kiểm shell, không kiểm đoạn code lồng bên trong. Dùng đường dẫn scratch do người đọc chọn hoặc tạo được từ bất kỳ checkout tương đương, không hard-code bố cục workspace đánh giá. Ghi command và kết quả thực trong records. Nếu command trong bài khác command đã thực thi, hoặc không có postcondition pass, ghi nó là chưa kiểm thay vì kế thừa kết quả từ bản scratch khác.

## 4. Batch, resume và acceptance

Chia công việc theo task/family, giữ một ledger xuyên suốt. Mỗi batch hoàn thiện content, kiểm source/code/navigation rồi cập nhật trạng thái; tiếp tục task còn lại trong phạm vi. Checkpoint ghi mục tiêu/phạm vi gốc, inventory đã khảo sát, ledger, active task/section, baseline/exclusions, unresolved blockers và next action. Resume kiểm các thông tin này trước khi viết thêm; không chỉ mở index rồi chọn lại vài chủ đề dễ.

Trước khi gọi **phạm vi tài liệu hoàn tất**, đối chiếu public inventory với ledger để tìm task/family bỏ sót, rồi thử đường đọc của các task đã nhận actionable. In-scope task còn absent/orientation/stale hoặc content blocker thì bàn giao là partial/checkpoint cùng phần còn thiếu; không tự chuyển nó thành out of scope. Verification blocked được báo riêng, không đồng nghĩa nội dung chưa hoàn tất. Giới hạn tài nguyên, quyền hoặc yêu cầu người dùng dừng được tôn trọng; batch không phải lý do tự thu nhỏ deliverable hay lời hứa tự chạy ngoài session.

Kiểm HTML cuối ở desktop và viewport hẹp, gồm trang có tên API dài trong prose/table/link. Đo overflow của document riêng với vùng cuộn code/table/diagram. Kiểm kích thước chữ SVG **sau scale/transform**; CSS `font-size` không đủ nếu rendered width khác viewBox. Chọn canvas width giữ nhãn đọc được rồi cuộn riêng hoặc chia hình; thử keyboard scroll/focus và đọc ảnh thực. Có thể tái dùng CSS đi kèm, nhưng theme/CSS tự viết vẫn phải đạt cùng checks. Không chỉnh identifier hoặc code để né overflow.

Khi so sánh với upstream docs được phép dùng làm evaluator: giữ output source-only riêng, freeze trước khi reviewer xem docs gốc; chấm khả năng trả lời các task ở cùng baseline, không tỷ lệ số trang. Nếu chỉ test vài chapters, kết luận chỉ về các chapters đó, không suy ra toàn site đã đạt reference-quality.

Với yêu cầu bộ reference hoặc mục tiêu chất lượng cụ thể, cố định trước khi viết một bộ câu hỏi acceptance đại diện cho các family từ public source/config/tests và tiêu chí đạt của từng câu. Crosscheck bộ câu hỏi với source inventory trước khi chấm; bộ câu hỏi do tác giả tự lập là candidate, không là mẫu số đáng tin nếu public surface còn bị bỏ sót. Sau mỗi candidate, một reviewer không phải tác giả (nếu có thể) đi từ index/guide tới **trang public** và thử trả lời từng câu như developer không có private ledger: setup/API, expected observation, failure/limit và self-check phải tìm được ở đó. Reviewer kiểm cả câu hỏi nguồn bị thiếu trong acceptance set; bổ sung chúng có evidence và chấm candidate trên phạm vi đầy đủ, không exempt vì tác giả chưa viết. Chấm chiều sâu và lỗi hợp đồng/first-run riêng; private ledger, source link, tên trang hoặc số snippet không tự cấp điểm. So kết quả với mục tiêu người dùng trên cùng bộ câu hỏi đầy đủ, đưa câu hụt về batch tiếp theo, freeze candidate mới rồi chấm lại. Nếu không có reviewer độc lập, tự audit bằng câu hỏi đã cố định và ghi rõ mức tin cậy thấp hơn. Nếu giới hạn thật buộc dừng trước mục tiêu, báo partial/checkpoint và giữ các câu hụt in scope; không tự hạ ngưỡng hay đổi mẫu câu hỏi để nhận đã đạt.
