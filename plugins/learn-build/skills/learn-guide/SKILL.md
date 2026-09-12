---
name: learn-guide
description: Create or redesign the next incremental HTML tutorial so an engineer can implement and understand it using the blueprint and current source. Active tutorial debugging, QA, and discussion belong to learn-pair; overall product direction belongs to learn-blueprint.
---

# Learn Guide

Author the next runnable tutorial so the user advances the enterprise product and can understand and work on that capability without an AI coding agent.

## Recover and select

Read [learning-contract.md](references/learning-contract.md) and [project-memory.md](references/project-memory.md) for priorities, authority, decisions, and retained context. Inspect project instructions, blueprint/records, prior tutorial, relevant source/configuration/dependencies, and diffs. Recover the baseline, accepted and rejected choices, open questions, and ownership gaps.

Choose one demonstrable capability or operational outcome that runs without future tutorial code. Identify the independent ability it develops and the prerequisites it needs. Split excessive cognitive load into smaller outcomes. An incomplete blueprint need not block clear work; establish a minimal snapshot when absent.

## Resolve and specify

Check actual paths, symbols, signatures, wiring, and package versions; verify critical external APIs against matching sources. Use a small experiment for uncertainty that could break the guide, without prebuilding the whole feature.

Follow the shared decision process for material choices; dependent implementation instructions wait with dependent code. Persist discussion as it happens. Develop the current user stories into acceptance walkthroughs before those instructions, linking stories, decisions, and checkpoints. Internal-only work can use an operational scenario. Keep future stories at known intent.

## Author and verify

Use [tutorial.md](references/tutorial.md) for followable checkpoints, manual QA, ownership practice, and code verification. Apply [html.md](references/html.md) for rich glossary, explanations, visuals, trade-offs, cost/security reasoning, and conclusions.

Write `<learning-root>/tutorials/NN-topic.html` and update the catalogue. Each checkpoint connects why → mechanism/visual/example → exact code → actions → expected result → diagnosis. Provide enough detail for independent work, with optional deeper material. Author the guide; implement only when assigned.

## Review and handoff

Use [review.md](references/review.md), with an independent reviewer when available. Resolve findings, verify the actual HTML/snippets, and synchronize records and snapshot. Report baseline/checkpoint, evidence and limits, ownership gaps, the pending decision, and next action. Keep authored, implemented, verified, and independently understood states separate. Learn-pair supports implementation and practice when available; create another guide only when due.
