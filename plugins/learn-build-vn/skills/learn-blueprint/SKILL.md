---
name: learn-blueprint
description: Dùng khi engineer bắt đầu product muốn vừa học vừa build, cần toàn cảnh architecture và lộ trình tutorials, hoặc cần xem lại blueprint sau implementation, QA hay constraint mới. Phù hợp với product planning; một lỗi cục bộ trong tutorial đang làm thuộc learn-pair.
---

# Learn Blueprint

Lập kế hoạch enterprise product user muốn và lộ trình thích nghi để làm chủ mà không cần AI coding agent.

## Khôi phục và trao đổi

Đọc [learning-contract.md](references/learning-contract.md) cho ưu tiên chung/quy trình decision; [project-memory.md](references/project-memory.md) cho khôi phục và lưu context liên tục. Đọc project instructions, requirements, records hiện có, source/config và diffs liên quan. Xác định/khôi phục roots, baseline, accepted target, ownership gaps.

Bắt đầu từ product scope/boundaries rồi decision đến hạn. Product lớn cần catalogue capability/dependency trước chi tiết tutorial hiện tại; revision nhỏ tập trung affected choices. Làm rõ thuật ngữ bằng actor scenario cụ thể, so sánh options có recommendation. Theo quy trình một câu hỏi chung. Lưu stories, explanations, non-ADR choices, rejected alternatives và architectural ADRs trong lúc trao đổi.

## Dựng và điều chỉnh blueprint

Dùng [blueprint.md](references/blueprint.md) cho catalogue, [quality.md](references/quality.md) cho enterprise requirements, [html.md](references/html.md) cho giải thích giàu visual bằng tiếng Việt. Duy trì `<learning-root>/index.html` gồm:

1. Goals, actors, scope, constraints, assumptions, glossary, boundaries.
2. Current/target architecture, runtime/data flow, delivery qua CI/CD/environments tới operations/recovery.
3. Quality requirements, controls, timing, owners, evidence.
4. Tutorial outcomes, khả năng ownership độc lập, technical/learning prerequisites.
5. Current snapshot/record index, active work, pending decisions và revisit triggers.

Giữ toàn cảnh enterprise target. Chỉ chi tiết implementation cho tutorial đến lượt; không viết whole-phase coding plan hoặc future guides. Estimate có ngày, tách baseline tutorials với conditional branches. Kiểm official sources hiện hành cho technology/version, giá và standards.

Dùng evidence implementation/QA/learning để điều chỉnh thứ tự. Discuss thay đổi architecture, quality, budget hoặc roadmap đáng kể trước phần phụ thuộc. Tại product milestone, đánh giá cả delivery và independent ownership theo contract chung.

## Review và handoff

Dùng [review.md](references/review.md) cho design mới hoặc thay đổi đáng kể, independent review khi khả dụng. Xử lý findings, validate HTML, sync records/snapshot bị ảnh hưởng. Handoff artifact, một decision pending nếu có và next action. Khi khả dụng, dùng learn-guide cho tutorial tiếp, learn-pair trong implementation; chúng resume từ records.
