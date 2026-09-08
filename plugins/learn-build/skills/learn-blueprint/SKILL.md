---
name: learn-blueprint
description: Plan an enterprise product's architecture and adaptive tutorial roadmap for an engineer learning while building, or revisit the blueprint after implementation, QA, or new constraints. Use for product planning; local issues in an active tutorial belong to learn-pair.
---

# Learn Blueprint

Maintain the whole enterprise product and learning roadmap so the user can understand, design, change, diagnose, operate/recover, and make architecture decisions for the next step.

## Start

Read [learning-contract.md](references/learning-contract.md) for ownership outcomes, project/docs roots, asking through HTML and waiting for a decision, in-place context, and documentation synchronization. This contract applies throughout the workflow.

Read project instructions, requirements, blueprint/decisions, relevant source/configuration, and diffs. Identify outcomes, users, critical journeys, constraints, and learning needs from the actual baseline. Reuse existing information and authorization.

## Build the whole picture and catalogue

Use [blueprint.md](references/blueprint.md) for an adaptive catalogue and [quality.md](references/quality.md) for quality requirements. Create or update `<learning-root>/index.html` using [html.md](references/html.md), covering:

1. Product goals, actors, scope, constraints, and assumptions.
2. Glossary, system context, current/target architecture, and boundaries.
3. Runtime/data flow and delivery flow from source through CI/CD and environments to operations/recovery.
4. Quality profile: requirements, controls, the tutorial/milestone where each is needed, evidence, and owners.
5. Tutorial catalogue: capabilities/demos, learning outcomes, and technical/learning dependencies.
6. Settled decisions, candidates/deferred questions, triggers/evidence needed, the active tutorial, and the next action.

Distinguish observed facts, selected targets, and candidates. Keep the full enterprise target visible, but detail implementation only for the tutorial now due; do not write a whole-phase coding plan or future guides. Estimate tutorial counts using assumptions and conditional branches rather than a fixed total while discovery remains open.

## Adapt direction

Settle required invariants before their dependencies using the shared decision process. Both technical and learning readiness determine the sequence. When evidence materially changes architecture, budget, quality, or the roadmap, present impacts, options, and a tagged recommendation for the user's decision before dependent work. Sync facts directly within scope.

Favor long-term choices proportionate to risk and operating capacity. Check current official sources when selecting technologies/versions, quoting prices, or citing standards. Do not add frameworks merely to fill boxes.

## Review and handoff

New designs or substantial design changes need independent review when available, following [review.md](references/review.md). Resolve findings, sync affected artifacts under the shared contract, and check HTML before handoff. Do not require the user to invoke a review skill themselves.

Hand off the artifact, one pending decision if any, and the next action. Use learn-guide for the next tutorial and learn-pair during implementation, discussion, debugging, or QA when those skills are available. Do not ask the entire deferred-question list again.
