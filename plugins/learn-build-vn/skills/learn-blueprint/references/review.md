# Review độc lập blueprint

## Review artifact cụ thể

Giao reviewer độc lập khả dụng requirements, constraints/decisions đã chốt, artifact và source/config/dependency paths, evidence liên quan. Review read-only: trả findings có location, severity, basis, proposed fix, phạm vi chưa kiểm. Author xử lý findings.

- Product fit: observed state, accepted target, boundaries, assumptions và actor goals khớp requirements/source.
- Catalogue: giữ enterprise destination, technical/ownership prerequisites; conditional estimates có cơ sở, future tutorials không bị chốt sớm.
- Quality: controls đến trước dependencies/exposure, technology/standard choices có nguồn, operational evidence và gaps còn lại rõ.

## Kiểm outcomes chung

Đọc [learning-contract.md](learning-contract.md), [html.md](html.md), [project-memory.md](project-memory.md); đối chiếu với artifact:

- Công việc có tiến tới enterprise product dự định và khả năng user tự change/diagnose/operate không cần agent hướng dẫn? Tách product evidence, user actions/assistance và khả năng chưa biết.
- User reasoning được từ glossary tại chỗ, causal visuals, examples, trade-offs, cost/security analysis, conclusions và hướng dẫn thực tế? Nội dung thường bằng tiếng Việt; technical terms và toàn bộ source/test code bằng tiếng Anh.
- Consequential decisions có authority thật và theo quy trình một câu hỏi? Prerequisite chưa hiểu được explanation/experiment; routine delegated choice không thêm approval/quiz gate.
- Người đọc mới resume được từ records, khôi phục corrections, rejected alternatives, non-ADR reasoning, stories, pending work, supersession mà không cần chat? Legacy context thiếu vẫn ghi unknown.
- Required controls cùng manual failure/recovery QA thật đến trước exposure tương ứng? Test-runner output không thay walkthrough.

## Xử lý và handoff

Author sửa findings, sync nội dung hiện hành và giữ reasoning lịch sử, kiểm phần bị ảnh hưởng. Review lại khi design thay đổi đáng kể hoặc resolution chưa rõ. Giữ dependent checkpoints unready nếu issue chưa xử lý có thể làm chúng sai.

Validate HTML theo html.md. Báo independent review, execution, rendering, user ownership là các scope riêng. Không có reviewer thì self-check và ghi rõ independent review chưa thực hiện.
