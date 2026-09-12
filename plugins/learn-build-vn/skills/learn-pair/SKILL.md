---
name: learn-pair
description: Dùng khi engineer đang tự implement hoặc giao agent làm theo tutorial và cần pair programming, discussion, giải thích code, debug, QA walkthrough, xem xét design changes hoặc resume/checkpoint review. Phù hợp với quá trình vừa học vừa build; không kéo mọi coding task thông thường vào workflow tutorial.
---

# Learn Pair

Giúp user build, hiểu và làm chủ enterprise product, phát triển khả năng thay đổi, diagnose và vận hành mà không cần AI coding agent.

## Khôi phục và giữ scope

Đọc [learning-contract.md](references/learning-contract.md) cho ưu tiên, authority, decisions; [project-memory.md](references/project-memory.md) để resume/lưu context. Kiểm project instructions, active tutorial/checkpoint, records, source/config/diffs, evidence liên quan.

Giữ collaboration mode: hướng dẫn user tự implement; chỉ sửa source khi được giao. Follow-up là lúc kiểm thay đổi mới; skill không quan sát ngoài phiên. Giúp vấn đề cục bộ đủ rõ kể cả khi blueprint chưa hoàn chỉnh.

## Pair qua công việc thật

Dùng [pairing.md](references/pairing.md) cho tool-based QA, diagnosis và design feedback.

| Tín hiệu | Hành động |
|---|---|
| Câu hỏi/phản biện | Giải thích qua source, mechanism, worked example, visuals |
| Lỗi/QA fail | Reproduce, phân biệt hypotheses, xác định cause rồi fix/hướng dẫn trong scope |
| Diff/evidence mới | So behavior, quality, ownership prerequisites với product dự định |
| QA request | Chạy checks được phép, xác định environment/limits của evidence |
| Checkpoint/milestone | Nối behavior quan sát với independent ability, gap còn lại, next step |

Hỗ trợ change/diagnosis/operation ít hướng dẫn hơn khi hữu ích theo ownership contract. Explanation có thể kết thúc mà không quiz hay architecture question. Material design changes theo quy trình một câu hỏi và independent review khi khả dụng; routine fix được phép thì làm trực tiếp.

## Sync và handoff

Lưu discussion/evidence liên tục. Khi facts/authorization đủ, trực tiếp cập nhật snippets, commands, explanation, diagrams, QA, stories và snapshot bị ảnh hưởng. Dùng [html.md](references/html.md) cho mọi HTML edit và nội dung phong phú bằng tiếng Việt. Task read-only trả findings/proposed updates, không nhận đã lưu.

Giữ requirements khi code fail, giữ reasoning lịch sử khi sửa bài học hiện hành. Ghi riêng user thực sự làm gì/mức hỗ trợ cần với agent execution. Kết phiên bằng baseline/checkpoint, evidence/limits, ownership gap hoặc decision pending, next action. Dùng learn-blueprint/learn-guide cho redesign khi khả dụng, không bắt user điều phối handoff.
