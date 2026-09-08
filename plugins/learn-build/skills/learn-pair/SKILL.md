---
name: learn-pair
description: Pair with an engineer implementing a tutorial personally or through an agent, including discussion, code explanation, debugging, QA walkthroughs, design changes, and resume/checkpoint review. Use for learning while building, without forcing ordinary coding tasks into a tutorial workflow.
---

# Learn Pair

Help the user build an enterprise product and retain full ownership through reasoning, debugging, modification, operations/recovery, and architecture decisions grounded in actual evidence.

## Start and preserve scope

Read [learning-contract.md](references/learning-contract.md) for project/docs roots, learning before decisions become due, asking and waiting in conversation, and keeping documentation current. This contract applies throughout the workflow.

Read project instructions, the active tutorial/checkpoint, relevant blueprint/decisions, source/configuration/diffs, and evidence. Preserve the assigned collaboration mode and authorization. When the user writes code, the agent provides reasoning/QA and edits documentation within scope; edit source only when assigned. Do not ask again about routine choices or information that can be read or inferred.

A follow-up or resume request is the time to reread source and diffs; the skill does not observe changes outside the session. Use [pairing.md](references/pairing.md) for debugging, tool-based QA, discussion, and resuming.

## Pairing loop

| Signal | Action |
|---|---|
| User asks or challenges | Explain through source, mechanisms, and visuals; experiment when useful without forcing a quiz or decision |
| Error or QA differs from expectations | Reproduce, distinguish hypotheses from root causes, and check before fixing |
| New diff/evidence | Compare requirements, boundaries, quality, and learning prerequisites, even when the happy path passes |
| QA walkthrough | Proactively use tools within scope; compare expected/actual behavior with source and the quality profile |
| Checkpoint finished or session resumed | Read the actual state, sync documentation, and identify the next action |

After a meaningful observation, determine whether to continue, make a local fix, or discuss the design. Material changes to public contracts, data ownership, trust boundaries, quality, budget, technologies with high migration cost, or the learning roadmap require the user's decision and independent review when available before dependent work. Keep improvements that are not yet due as candidates. Ask under the shared contract; an explanation can end without generating a decision.

## Synchronize and close the session

Synchronization is an output of pairing: directly update affected tutorial/blueprint snippets, setup/commands, diagrams, explanations, and QA/status when facts are sufficient and documentation edits are authorized. For read-only tasks or prohibited documentation changes, return a patch or findings. Do not stop at a list of things that need syncing.

Under the shared contract, preserve acceptance criteria when code is wrong, keep candidates separate from targets, and describe current code/targets instead of editing history. Add essential mechanism explanations to the checkpoint when the user asks follow-up questions. Apply learn-blueprint/learn-guide for redesign when available, without requiring the user to coordinate handoffs among skills.

At session end, record briefly in the tutorial: checkpoint/baseline, evidence and limits, a learning gap or pending decision, and the next action. Do not create a report for each message. Record who ran QA, the command/actions, actual results, and enough environment context to identify scope. Completing the agent's assigned work does not mean the tutorial is complete or the user understands it. Apply [html.md](references/html.md) when editing HTML.
