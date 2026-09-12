---
name: learn-guide
description: Dùng khi cần tạo hoặc thiết kế lại một incremental tutorial HTML để engineer vừa implement vừa hiểu, dựa trên blueprint và source hiện tại. Phù hợp với tutorial đến lượt làm; debug, QA hoặc discussion khi đang implement thuộc learn-pair, định hướng toàn product thuộc learn-blueprint.
---

# Learn Guide

Viết tutorial runnable tiếp theo để user phát triển enterprise product, hiểu và tự làm việc với capability đó mà không cần AI coding agent.

## Khôi phục và chọn bước

Đọc [learning-contract.md](references/learning-contract.md), [project-memory.md](references/project-memory.md) cho ưu tiên, authority, decisions và retained context. Kiểm project instructions, blueprint/records, tutorial trước, source/config/dependencies/diffs liên quan. Khôi phục baseline, accepted/rejected choices, câu hỏi mở, ownership gaps.

Chọn một capability hoặc operational outcome demo được mà không cần future tutorial code. Xác định khả năng tự thực hiện sẽ phát triển và prerequisites cần có. Tách outcome nếu quá tải nhận thức. Blueprint chưa đầy đủ không chặn phần đủ scope; tạo snapshot tối thiểu nếu thiếu.

## Giải quyết và đặc tả

Kiểm paths, symbols, signatures, wiring, package versions thật; critical external API đối chiếu nguồn đúng version. Dùng experiment nhỏ cho uncertainty có thể phá guide, không prebuild toàn feature.

Theo decision process chung cho material choices; instructions phụ thuộc chờ cùng code. Lưu discussion ngay khi diễn ra. Phát triển user stories hiện tại thành acceptance walkthrough trước instructions đó, link story/decision/checkpoint. Internal-only work có thể dùng operational scenario. Future stories chỉ giữ intent đã biết.

## Author và kiểm

Dùng [tutorial.md](references/tutorial.md) cho checkpoints làm theo được, manual QA, ownership practice và code verification. Áp dụng [html.md](references/html.md) cho glossary, explanations, visuals, trade-offs, cost/security reasoning, conclusions phong phú bằng tiếng Việt.

Viết `<learning-root>/tutorials/NN-topic.html` và cập nhật catalogue. Mỗi checkpoint nối vì sao → mechanism/visual/example → exact code → thao tác → expected result → diagnosis. Đủ chi tiết để tự làm, phần sâu mở rộng tùy chọn. Author guide; chỉ implement khi được giao.

## Review và handoff

Dùng [review.md](references/review.md), independent reviewer khi khả dụng. Xử lý findings, kiểm HTML/snippets thật, sync records/snapshot. Báo baseline/checkpoint, evidence/limits, ownership gaps, decision pending, next action. Tách authored, implemented, verified và independently understood. Learn-pair hỗ trợ implementation/practice khi khả dụng; chỉ tạo guide tiếp khi đến lượt.
