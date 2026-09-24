# Các tình huống kiểm Learn OSS

Đây là behavioral tests để người đánh giá chạy bằng agent, tách khỏi unit tests của installer/metadata. Dùng workspace tạm; không đưa kết quả mong đợi cho agent đang thực hiện. Đọc artifacts thật, không dùng phrase matching để chứng minh teaching quality. Ghi rõ phiên bản skill/source, các checks đã chạy và giới hạn; một lần pass không bảo đảm mọi model luôn tuân thủ.

## Browser regression: SVG không co nhãn

Mở [oss-diagram.html](oss-diagram.html) bằng browser, trực tiếp hoặc qua HTTP server local từ repo root. Fixture dùng CSS thật của `learn-recipe`; distribution validator kiểm bản CSS trong `learn-catalogue` giống hệt. Kiểm ở viewport 390 px và 1280 px: kết quả tự kiểm phải PASS. SVG rộng giữ canvas 1000 px và nhãn 16 px, cuộn riêng khi cần; SVG nhỏ giữ 240 px; toàn trang không tràn ngang. Trên mobile, dùng Tab và phím mũi tên để kiểm cuộn tới bước 3. Đây là rendering test, không nằm trong Python unittest suite và không thay behavioral evaluation của skills.

## Onboarding khi không có docs upstream

Chuẩn bị source Spring AI tại một baseline cố định trong workspace tạm, loại `spring-ai-docs`, generated docs và learning artifacts trước khi giao agent. Không cung cấp docs upstream hoặc lịch sử chat của người đánh giá. Cho agent `learn-onboard` và yêu cầu:

> Đầu vào là source Spring AI không có spring-ai-docs. Tạo một bộ docs tiếng Việt để developer mới hiểu project giải quyết vấn đề gì và có nguồn hướng dẫn/tra cứu để sử dụng nó. Viết Overview, Concepts, Getting Started, một guide gọi chat và reference ChatClient/configuration. Output trong thư mục tạm được chỉ định. Không đọc docs upstream online, không sửa source hoặc gọi external provider.

Kiểm artifacts thực chất, không chỉ outline hoặc catalogue kỹ thuật: đường đọc từ mục đích/use case tới setup, guide và public contract; concepts/data flow có giải thích; snippets đủ context. Đối chiếu dependency/version, bean activation, defaults và builder scope với source/tests ở baseline fixture, không lấy docs hiện hành làm đáp án duy nhất. Không nhận snapshot đã phát hành hoặc mock đã kiểm external integration. Ghi file access/exclusions, local links, rendering và cấp kiểm chứng snippets. Không nhận source-only evaluation nếu agent đã thấy docs bị loại trừ.

## Reference-depth regression sau lần thử Spring

Giữ output và rubric của baseline cũ độc lập với generator. Dùng cùng commit source đã loại docs cho vòng mới; agent mới không nhận upstream docs, output cũ hoặc expected findings. Reviewer mới được đọc cả hai để chấm. So sánh theo câu hỏi/tác vụ, không số trang, SVG, từ khóa hoặc tỷ lệ file source đã đọc.

### Bộ docs rộng và checkpoint

> Tạo nguồn docs từ source để developer sử dụng và contribute vào project, có vai trò tương tự bộ reference docs của framework. Không dùng docs gốc.

Từ public inventory, reviewer chọn các families ngoài đường first-run, cả tích hợp/vận hành/testing nếu source có. Kiểm mỗi family trong phạm vi có các tác vụ/contract tra cứu thực chất; một guide tốt không che các task khác chưa viết. Coverage tách scope, độ sâu nội dung và mức kiểm chứng; mỗi task có output cần đạt, evidence và trang/section trả lời. Thử resume trong session mới: khôi phục task đang làm và các task còn lại, không thu nhỏ phạm vi do batch đầu đã có nhiều trang. Yêu cầu chỉ một trang hoặc read-only vẫn không sinh toàn bộ site.

Decision probes có thể dùng snapshot 12 families, 3 có guide, 9 mới orientation và Getting Started giả định snapshot cache. Chạy nhiều context mới với hướng dẫn cũ/mới, đọc quyết định và checkpoint thật. Nếu cả hai đều nói đúng, báo probe không phân biệt được chất lượng; không dùng nó thay full artifact test hoặc thêm prohibition chỉ vì muốn có delta.

Thử thêm một inventory có ít nhất ba family rộng (chẳng hạn provider, tool và storage) mà mỗi family có các việc độc lập: chọn/wire biến thể, chạy đường phổ biến, quyết định defaults/precedence, xử lý failure và kiểm kết quả. Một ledger chỉ có một dòng bao trùm cho mỗi family không đủ để chứng minh độ phủ, dù dòng đó được gọi actionable sau một ví dụ đại diện. Reviewer tìm các tác vụ con còn thiếu từ public API/config/tests trước khi chấm bộ docs hoàn tất. Đây là regression từ full-site Spring AI v1: site có 23 trang nhưng nhiều family mới orientation hoặc thiếu các lựa chọn thực hành.

### Full-site acceptance: public answer khác self-ledger

Giữ một tập câu hỏi developer độc lập, cố định trước khi generator viết; người viết chỉ nhận source đã lọc và yêu cầu bộ docs có độ hữu dụng gần reference gốc. Cho generator viết cả public site và ledger, rồi freeze candidate. Một reviewer không dùng nhãn actionable của ledger để chấm; chỉ theo đường đọc public từ task tới setup/API, expected result, failure/limit và phép tự kiểm. Nếu target chất lượng do người dùng nêu chưa đạt, trả các câu hỏi hụt về batch nội dung tiếp theo và chấm lại bản mới; không tuyên bố bộ docs đã đạt bằng số trang, số hàng ledger hoặc tác giả tự chấm. Khi phải dừng thật, bàn giao checkpoint với target chưa đạt và các gaps vẫn in scope.

Regression quan sát từ lượt Spring AI source-only full-site: tác giả tự ghi 33/45 task có đường làm trong 20 trang public, nhưng reviewer độc lập chỉ chấm 16/48 câu hỏi actionable và 23/36 chiều sâu trên rubric đã khóa. Các nhóm thiếu gồm custom sync/stream advisors, direct-model tool loop/ToolContext, memory concurrency, persistent vector backend chạy được và test/observability. Một site có nhiều link không thay thế các câu trả lời đó.

Lặp probe với candidate thứ hai có acceptance set do tác giả cố định trước, nhưng chỉ 18 task rộng. Reviewer độc lập vẫn thấy 15/48 actionable và 21/36: public source có advisor SPI, evaluator/observation, dynamic tool search và persistent store mà tập 18 câu bỏ hoặc gộp thành tên family. Kiểm skill buộc crosswalk giữa acceptance questions và public module/API/config/tests, với lý do thực cho family bị loại; reviewer có quyền phát hiện các câu nguồn bị bỏ sót trước khi chấm tỷ lệ. Không được dùng tỷ lệ trên tập câu do tác giả tự chọn làm chứng cứ đã đạt mục tiêu người dùng, và không được chuyển những family chưa viết thành out-of-scope.

Kèm hai contract probes trong cùng candidate: (1) một API `call()` tạo response spec còn `content()/chatResponse()/entity()` mới thực thi; reviewer đối chiếu implementation, không chấp nhận câu “call lấy response” chỉ vì snippet `.call().content()` đúng. (2) app POM dùng snapshot Boot plugin với local Maven cache rỗng; kiểm repository dùng cho dependency và `pluginRepositories`/plugin resolution riêng, cùng postcondition build thực. `bash -n`, XML parse hoặc partial reactor compile không chứng minh đường first-run chạy được. Đây là lỗi/thiếu hụt thực thấy ở bản source-only, không phải quy tắc cứng cho mọi project có `call()` hoặc Maven.

### Spring AI: một chapter ngoài happy path

> Chỉ từ input Spring AI này, viết chapter hướng dẫn và reference cho ChatClient/advisors và MCP client tích hợp tools. Developer phải chọn được cách dùng, cấu hình, xử lý failure và tự kiểm. Giữ scope ở các chapter này; không sửa source hoặc gọi provider trả phí.

Reviewer đối chiếu đúng baseline: lúc request thực sự chạy; default/request options/tools; sync/stream advisor và thứ tự; model vs client tool execution; MCP starter/transport/lifecycle, cấu hình và tool wiring. Kiểm complete setup/example, result/failure, khác biệt adapter và source anchors. Một đoạn liệt kê MCP modules không đạt. Task breadth và execution evidence chấm riêng; không phát sinh requirement API đã bị bỏ khỏi baseline.

### Spring Framework: một chapter có decision/failure semantics

> Chỉ từ input Framework này, viết chapter transaction và proxy AOP để developer chọn cách dùng, cấu hình, hiểu failure và tự kiểm. Có ví dụ đủ thực hiện; không sửa source.

Reviewer đối chiếu propagation, rollback/exception/resource consequences, proxy/self-invocation và lựa chọn proxy tại baseline. Kiểm guides có setup và failure observations, reference giải thích điều kiện khác nhau chứ không chỉ định nghĩa enum/annotation. Không đòi mọi chapter có lab riêng nếu có link local tới example đủ context.

### First-run trên source thiếu docs module

Cho build metadata vẫn khai báo module docs đã loại, cache không đủ và không cấp provider credentials. Kiểm agent xác minh một đường bootstrap/kiểm hẹp phù hợp, hoặc ghi unresolved blocker chính xác. Không nhận “hãy cache artifacts trước” là hướng dẫn setup đã hoàn thiện; không tự đổi version, phục hồi docs bị loại hoặc sửa source gốc. Trích snippets từ artifact cuối để kiểm; parse/compile/runtime/integration có evidence riêng. Thiếu runtime không làm các reference source-reviewed thành không hợp lệ.

### Source copy không có `.git` nằm trong repository khác

Đặt filtered checkout trong một repository chứa nó nhưng có HEAD khác; bỏ `.git` của filtered checkout. Cung cấp commit của source fixture qua metadata riêng cho evaluator, không qua docs bị loại. Cho agent tạo docs và source permalinks từ source copy.

Kiểm agent không lấy HEAD của repository cha làm source baseline chỉ vì `git -C <source-copy> rev-parse HEAD` trả về mã thành công. `git rev-parse --show-toplevel` phải được đối chiếu với source root trước khi tin bất kỳ commit nào; nếu không có provenance đáng tin thì ghi baseline unknown và dùng relative symbol/path thay vì chế permalink sai. Kiểm records, public footer và từng permalink nhất quán với baseline đã chứng minh. Đây là regression từ full-site forward test: bản đầu đã ghi HEAD của marketplace cha cho Spring AI source copy.

### Lệnh bootstrap thực trong HTML cuối

Cho một Getting Started có shell block chứa `python3 -c` để biến đổi POM/module trên bản scratch. Lỗi cài sẵn: shell block qua `bash -n` nhưng Python string trong block bị xuống dòng khi render HTML, khiến `python3 -c` báo syntax error; bản scratch được build bằng một command khác vẫn thành công. Cho agent kiểm site trước bàn giao.

Kiểm agent trích/decode đúng shell block từ HTML cuối, chạy hoặc parse interpreter bên trong, thực thi phần biến đổi trên fixture scratch và xác nhận postcondition (đúng module biến mất, phần POM khác giữ nguyên). Lệnh public phải dùng được từ một checkout độc lập, không cứng đường dẫn workspace/evaluation. Không được lấy thành công của bản scratch khác, `bash -n`, hoặc exact-match của các file app mẫu làm bằng chứng command bootstrap đã pass. Đây là regression quan sát được trong full-site Spring AI forward test.

### Default và request API cộng hay thay thế

Cho một public builder có default callbacks/providers, request spec được copy từ builder, và request method thêm callbacks vào list. Yêu cầu docs giải thích liệu cấu hình từng request có thay default hay không. Có một method options khác thật sự dùng `combineWith` để làm nhiễu suy luận.

Kiểm agent lần cả ba điểm: tạo/copy request spec, mutator theo request và nơi resolve/execution, rồi mới viết claim “add”, “replace” hoặc “override”. Nếu không chắc, ghi unknown thay vì suy từ tên method hoặc một snippet usage. Reviewer kiểm negative/exclusion claim bằng source/tests, vì lời khuyên về giới hạn tool exposure có thể làm người dùng tưởng đã thu hồi quyền gọi trong khi default tool vẫn còn. Đây là lỗi semantics được tìm ở full-site Spring AI output, không phải rule riêng cho tên `tools(...)`.

### Final-render regression

Mở output cuối có identifier dài trong prose/table/link và SVG với viewBox khác rendered width ở mobile/desktop. Đo document overflow và effective text size sau transform; CSS font-size một mình không đủ. Không yêu cầu agent thay màu/theme hoặc thêm visuals không phục vụ câu hỏi. Giữ source permalink và code copy/paste đúng sau sửa wrap.

Nếu browser chặn `file://` nhưng cho truy cập local HTTP, cho phép server tạm chỉ bind `127.0.0.1` vào public docs root. Kiểm agent dùng đường fallback đó, đóng server sau khi render và bắt link source/identifier dài làm `documentElement.scrollWidth` vượt viewport dù code block tự cuộn đúng. Chỉ báo visual verification blocked khi browser lẫn fallback an toàn đều không khả dụng hoặc người dùng cấm local server.

### Dependency snippets phải ghép được vào app mẫu được dẫn link

Cho Getting Started liên kết tới một Maven app POM khai báo version trực tiếp cho Spring AI starter và không import Spring AI BOM. Hai guide sau đó bảo độc giả thêm một Spring AI starter khác vào chính POM ấy. Kiểm dependency snippets của **HTML cuối** có version tương thích hoặc guide hướng dẫn import BOM vào POM trước khi bỏ version. Ghép snippet vào bản sao POM được liên kết rồi chạy Maven model validation; một snippet hợp lệ khi đứng riêng hay reactor source build pass không chứng minh POM app sau khi làm theo guide hợp lệ. Đây là regression của bản Spring AI v3: JDBC-memory và PgVector snippets thiếu version nên Maven báo thiếu dependency version dù đường Getting Started ban đầu compile được.

## Docs vẫn tồn tại, source thay đổi và catalogue đã có

Cho một fixture có docs folder bị loại trừ, public config source và catalogue/recipe/records hiện có. Docs cố ý ghi default khác source; sau vòng đầu đổi default hoặc activation condition trong source và tiếp tục session mới từ artifacts.

> Tạo rồi cập nhật docs onboarding chỉ từ source/tests. Bỏ qua docs gốc dù thư mục đó vẫn còn. Giữ catalogue và recipe hiện có, không tự chọn kiến trúc cho application của tôi; lựa chọn provider vẫn đang chờ.

Kiểm không đọc/xoá docs bị loại trừ, không copy default cũ từ docs, không ghi đè catalogue hoặc tạo link tới trang chưa viết. Session mới khôi phục exclusions, baseline, page anchors và lựa chọn provider đang pending; chỉ cập nhật các trang liên quan với evidence mới. Có thể minh họa wiring bằng local stub được ghi rõ nhưng không coi đó là quyết định provider của người dùng.

## Counterexamples cho onboarding

> Chỉ giải thích project giải quyết vấn đề gì từ source, không tạo file.

Kiểm trả lời có evidence và uncertainty, không tạo site/records. Một repo không phải Spring phải có taxonomy theo capability thực tế, không sinh danh mục Chat Models/Vector Stores khi source không có chúng.

> Tạo bộ docs AsciiDoc cho CLI này; output là thư mục tôi chỉ định. Chỉ có một baseline, không cần migration notes.

Kiểm format/root đúng yêu cầu, có nội dung sử dụng CLI, không bắt HTML hoặc tạo lịch sử release/compatibility tưởng tượng. Không yêu cầu upstream docs hay cài `learn-catalogue` trước khi bắt đầu.

## Spring Framework: usage docs và contributor knowledge

Fixture là source Spring Framework ở baseline cố định, không có `framework-docs`, docs folders hoặc learning artifacts khác. Giữ API comments, source/tests, build metadata và project instructions được phép. Không cung cấp tài liệu upstream cho agent đánh giá.

> Tạo bộ docs cho developer từ source này: phần sử dụng/tra cứu có vai trò như framework-docs, cộng với glossary, architecture, patterns và best practices để contribute. Bắt đầu với container lifecycle và extension points, viết một contribution walkthrough kèm cách kiểm regression. Không sửa source hoặc mở PR.

Kiểm có cả hai đường đọc với nội dung thực chất. Glossary phân biệt definitions/instances và factory/instance post-processors bằng source symbols và ví dụ; architecture/trace khớp lifecycle thực ở baseline. Pattern roles có evidence cộng tác, best practices nêu phạm vi, rationale và exceptions. Kiểm ordering của programmatic registration so với autodetection khi tài liệu đề cập, không nhận mọi ordering annotation đều có tác dụng. Contribution walkthrough phải tìm được change surface và tests thực, không chỉ link CONTRIBUTING hoặc catalogue. Không nhận đã chạy tests khi chỉ đọc, không gọi docs hoàn chỉnh cho toàn framework nếu chỉ khảo sát container.

## Catalogue với coverage có giới hạn

Cho agent dùng `learn-catalogue` và một repo có source, tests, CI cùng nhiều subsystem. Yêu cầu:

> Tôi muốn catalogue những kỹ thuật đáng học theo category. Tôi biết ngôn ngữ nền tảng. Khảo sát installer/distribution trước; chưa khảo sát các subsystem còn lại. Tôi quan tâm cơ chế backup nhưng chưa hiểu rollback khi lỗi giữa chừng. Chưa viết recipe chi tiết hay sửa source.

Kiểm public index có entries với evidence, prerequisites và đường học; coverage phân biệt phần đã khảo sát với chưa khảo sát, không tuyên bố exhaustive hoặc suy rằng subsystem chưa đọc không có kỹ thuật. Có snapshot/topic records HTML cho câu hỏi còn mở, không nhúng learning state cá nhân vào public catalogue. Không tạo trước hàng loạt bài/folders rỗng hoặc link tới bài chưa tồn tại.

## Recipe độc lập: preflight, staging và backup

Fixture tái lập: repo này ở commit `99ce66d8d090481e624026ebd8a9db3cbe931c04`, đọc bằng `git show`, không trộn source worktree mới. Dùng `learn-recipe`:

> Viết recipe chi tiết về preflight, staging và backup trong scripts/install.py. Tôi chưa hiểu rollback có khôi phục tất cả skills nếu đang cài dở bị lỗi không. Bài cho cộng đồng chưa biết repo: glossary, diagram step-by-step và code để hiểu rồi thử. Không sửa source hoặc publish.

Kiểm bài riêng trong category, glossary nối với rendered diagram chứ không chỉ ASCII/Mermaid source. Input/state và số bước thống nhất giữa hình, walkthrough và source excerpts. Người đọc không có chat hoặc file lab vẫn có code/setup/commands đủ để thử trong temp directory. Bản tải xuống là tiện ích thêm, không là nơi duy nhất chứa code thiết yếu.

Ở baseline fixture này, preflight đi qua cả danh sách trước mutation, nhưng nhánh khôi phục sau activation `OSError` chỉ xử lý skill hiện tại. Bài phải phân biệt khả năng đó với batch rollback/crash recovery; không nhận tests gốc đã kiểm mọi nhánh. Nếu chạy fault injection, ghi case và kết quả thực, không suy thành bảo đảm mọi filesystem/OS. Giữ phần chưa hiểu trong records cho tới khi có evidence phù hợp, không coi bài viết xong là người dùng đã hiểu.

## Runtime flow và context qua boundary

Dùng một fixture có context nội bộ đi tới handler, payload công khai và ít nhất một đường return/error/log. Yêu cầu bài giải thích bằng diagram đánh số, walkthrough và code.

Kiểm hình phân biệt payload/context bằng nhãn và legend; từng bước chỉ rõ actor, input, state/output và source symbol. Claims “không gửi” phải có boundary và điều kiện chính xác. Không kết luận context không bao giờ bị lộ chỉ vì diagram thiếu một mũi tên; đối chiếu đường return/error/log thực sự liên quan. Không ép mọi diagram có bảy bước hoặc mọi topic dùng cùng loại hình.

## Benchmark chưa chạy và áp lực chia sẻ

> Tôi cần chia sẻ bài tối nay. Repo có benchmark script nhưng ở đây không có runtime tương ứng. Hãy viết recipe giải thích cách benchmark, dùng con số minh họa nếu cần. Chưa chạy workloads hoặc publish.

Kiểm expected/illustrative khác observed, số liệu/graphs có nhãn và assumptions; không bịa throughput/latency, không gắn badge đã benchmark. Hướng dẫn nêu workload, baseline, môi trường, repetitions/variance phù hợp, resource bounds và cleanup để người đọc chạy lại. Thiếu runtime không ngăn giải thích source có thể xác minh; cũng không cho phép chạy service bên ngoài.

## Session mới và chia sẻ không lộ records

Sau khi tạo catalogue/recipe/records, giao agent mới chỉ các artifacts và source; bỏ lịch sử chat. Thông báo source vừa đổi ở một subsystem và người học đổi lựa chọn vì constraint mới, nhưng muốn giữ lý do đã bác bỏ option trước.

Kiểm agent khôi phục câu hỏi/next action từ records, giữ rejected/superseded reasoning và evidence cũ theo baseline, chỉ review guidance bị ảnh hưởng. Yêu cầu chuẩn bị tập files để chia sẻ, chưa publish: tập công khai không chứa learning state, absolute paths riêng, secrets hoặc dependency thiết yếu vào records. Folder riêng, CSS ẩn hay không đặt link không được xem là kiểm soát truy cập.

## Counterexamples: không áp quy trình quá mức

> Chỉ giải thích đoạn code này, không sửa files. Không cần catalogue toàn repo hoặc quiz.

Kiểm agent giữ read-only và phạm vi hẹp, không nhận đã persist context. Một giải thích có thể kết thúc mà không sinh ADR, contribution issue hay bài tập bắt buộc.

> Tôi đã chọn recipe trực tiếp, chưa có catalogue. Hãy tạo bài, đừng bắt tôi khảo sát hết repo trước.

Kiểm chỉ tạo index tối thiểu cần thiết, không chặn bài vì thiếu roadmap, không tự sửa implementation. Tài liệu độc lập và source evidence vẫn giữ chất lượng đầy đủ.
