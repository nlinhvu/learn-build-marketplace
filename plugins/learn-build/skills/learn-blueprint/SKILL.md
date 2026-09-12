---
name: learn-blueprint
description: Plan an enterprise product's architecture and adaptive tutorial roadmap for an engineer learning while building, or revisit the blueprint after implementation, QA, or new constraints. Use for product planning; local issues in an active tutorial belong to learn-pair.
---

# Learn Blueprint

Plan the user's intended enterprise product and an adaptive path to owning it without an AI coding agent.

## Recover and discuss

Read [learning-contract.md](references/learning-contract.md) for the shared priorities and decision process, and [project-memory.md](references/project-memory.md) for context recovery and continuous retention. Read project instructions, requirements, existing records, relevant source/configuration, and diffs. Establish or recover the roots, baseline, accepted target, and ownership gaps.

Start with product scope and boundaries, then the decision now due. For large products, catalogue capabilities and dependencies before current-tutorial detail; for a bounded revision, address affected choices. Clarify terms with concrete actor scenarios and compare plausible options with a recommendation. Follow the shared one-question process. Capture stories, explanations, non-ADR choices, rejected alternatives, and architectural ADRs as discussion proceeds.

## Build and adapt the blueprint

Use [blueprint.md](references/blueprint.md) for catalogue design, [quality.md](references/quality.md) for enterprise requirements, and [html.md](references/html.md) for rich visual explanation. Maintain `<learning-root>/index.html` with:

1. Goals, actors, scope, constraints, assumptions, glossary, and boundaries.
2. Current/target architecture, runtime/data flow, and delivery through CI/CD, environments, operations, and recovery.
3. Quality requirements, controls, timing, owners, and evidence.
4. Tutorial outcomes, independent ownership abilities, and technical/learning prerequisites.
5. Current snapshot and record index, including active work, pending decisions, and revisit triggers.

Keep the whole enterprise target visible. Detail implementation only for the tutorial now due; avoid whole-phase coding plans or future guides. Date estimates and distinguish baseline tutorials from conditional branches. Check current official sources for technology/version selections, prices, and standards.

Use implementation, QA, and learning evidence to adapt the sequence. Discuss material architecture, quality, budget, or roadmap changes before dependent work. At product milestones, assess both delivery and independent ownership under the shared contract.

## Review and handoff

Use [review.md](references/review.md) for new designs or substantial changes, with independent review when available. Resolve findings, validate HTML, and synchronize affected records and snapshot. Hand off the artifact, one pending decision if any, and next action. Use learn-guide for the next tutorial and learn-pair during implementation when available; they resume from the records.
