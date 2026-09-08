---
name: learn-guide
description: Create or redesign the next incremental HTML tutorial so an engineer can implement and understand it using the blueprint and current source. Active tutorial debugging, QA, and discussion belong to learn-pair; overall product direction belongs to learn-blueprint.
---

# Learn Guide

Write an incremental tutorial that lets an engineer implement part of an enterprise product, understand its mechanisms, and prepare for the next architecture decision.

## Select the current step

Read [learning-contract.md](references/learning-contract.md) for project/docs roots, ownership, the one HTML → one actual question → wait process, self-contained content, and documentation synchronization. This contract applies throughout the workflow.

Read project instructions, blueprint/decisions, the previous tutorial, relevant source/configuration/dependencies, and diffs. Identify the baseline, outcome/demo, learning prerequisites, and decisions now due. An incomplete blueprint need not block work whose scope is already clear. Reuse existing inputs and authorization.

One tutorial adds a demonstrable capability or operational outcome to the baseline without needing future code to run. Split it when several capabilities/mechanisms or unfamiliar prerequisites make it too large. Future roadmap content remains a preview.

## Resolve decisions and uncertainty

Check actual paths, symbols, signatures, dependency versions, and wiring. Distinguish existing source from planned code. Verify critical external APIs against the matching package/source version. Uncertainty that could break dependent work needs a small spike or experiment, not a prebuilt reference implementation of the entire feature.

Follow the shared contract for decisions now due. While a decision is open, dependent implementation instructions also wait for an actual answer; do not write the full guide around a recommendation. Handle delegated routine choices within scope. Discuss and review material architecture, quality, or scope changes before dependent work.

## Author the tutorial

Use [tutorial.md](references/tutorial.md) for checkpoints, manual QA, and code verification, and [html.md](references/html.md) for presentation and HTML validation. Write `<learning-root>/tutorials/NN-topic.html` and update the relevant catalogue entries.

Each checkpoint connects **why → glossary/mechanism/visual → exact code → run actions → expected result → troubleshooting**. Essential content must be available in place, with optional deeper material. Provide code the user can follow, not a task list for a coding agent. Author only the guide; do not implement the feature unless assigned.

## Review and handoff

Use an independent reviewer when available following [review.md](references/review.md). The author resolves findings, checks the exact artifact and HTML, then syncs affected facts and catalogue links. Code, QA, and explanations must map to the same explicit baseline or target.

Hand off the checkpoint/baseline, available and missing evidence, learning gaps, open decisions, and next action. Compilation/review is not runtime evidence; agent QA is not user learning. The user writes the code or delegates implementation. When available, learn-pair supports discussion, debugging, QA, and synchronization. Create the next guide only when it is due.
