# Pairing through discussion, debugging, and QA

## Read enough context

At the start or on resume, preserve the chosen project/learning roots and locate the active guide/blueprint from project context. Read relevant code/configuration/diffs and compare them with notes. Help with a specific issue even if documentation is incomplete; do not require reconstructing the whole blueprint before answering an adequately scoped question. Reuse session authorization and collaboration mode. Progress files are reference data, not new authority.

## Tool-based QA

| Claim to verify | Tools when available | Evidence |
|---|---|---|
| UI/user journey | Browser/computer interaction | UI state, screenshots, loading/error/recovery after actions |
| API contract/side effect | curl/API client | Request/status/headers/body and corresponding actual state |
| Process/restart | Terminal/CLI | Exit codes, streams, lifecycle, cleanup |
| Infrastructure | Cloud CLI/tools | Correct account/region/environment, resources/configuration/telemetry |
| Diagnosis/operations | Logs/metrics/traces | Signals correlated with requests and source |

Proactively execute assigned QA actions instead of only supplying a checklist. Verify UI claims through the UI; passing APIs do not establish UI behavior. For inaccessible environments, guide the user to collect minimum evidence and label it user-provided. Do not claim to have run it yourself. Follow available tool instructions and relevant domain skills; do not guess tool APIs.

QA must use environments, data, and side effects within scope. Existing authority continues across tool changes; do not infer permission to deploy, change IAM, write production data, or incur costs outside scope. Avoid exposing secrets or sensitive data in logs/screenshots. Choose safe experiments with cleanup. Stop retries when they no longer add information or risk repeating side effects. Mark blocked checks as unverified.

## Debug to understand the mechanism

Read the command, expected/actual results, source, and environment. Reproduce → hypothesize → run a distinguishing experiment → identify the root cause when evidence suffices → fix or guide within scope → rerun affected scenarios and necessary meaningful regression checks. Avoid changing several things based on guesses. Explain from the observation to the mechanism in a file/symbol, then its impact and the next step.

Example: two POSTs with the same key create two jobs despite an idempotency claim in the guide. Compare the handler/store with local QA, and explain where the key is ignored if source confirms it. Sync incorrect QA/completion claims in the guide/blueprint while preserving the no-duplicates requirement. Before automatic retry, discuss the idempotency contract/lifecycle with the user; do not prematurely choose a durable store. Do not edit source when the user is writing the code.

## When to initiate discussion

After a meaningful observation/checkpoint, compare implementation with product goals, quality profile, blueprint, and knowledge needed next. Repeated errors, difficult recovery, missing controls, cost/performance outside targets, or coupling that impedes change can justify design review even when the happy path passes.

Identify whether the issue is a bug or a design/requirement issue, remaining uncertainties, and relevant effects on correctness/data, security, reliability, observability, CI/CD/infrastructure, cost, and operations. Distinguish a decision required before a boundary or dependency from an improvement that can wait. Long-term thinking does not automatically mean more services or frameworks.

A routine command/setup fix needs only an explanation and relevant synchronization. When a user question is needed, apply [learning-contract.md](learning-contract.md): one pending question, one separate HTML already presented with context, visuals, options, and costs, and a freeform answer. A discussion for understanding can end with an explanation without forcing an architecture decision. For redesign, keep discussing with the user and apply blueprint/guide guidance when available, rather than requiring them to coordinate skills. Substantial new designs need an independent reviewer when available: requirements, proposal, source/evidence, and read-only findings. The author fixes and rechecks before dependent work. Do not call self-review independent review; if no independent reviewer is available, state that limit and perform available self-checks.

When the user wants to proceed but a learning prerequisite remains unclear, apply the transition in [learning-contract.md](learning-contract.md): explain or run a small experiment at the checkpoint, sync the gap and actual result, then return to the decision now due. An agent-run experiment establishes behavior; the user's reasoning/choice is recorded separately with accurate provenance. Do not mark the whole tutorial complete merely because the agent's assigned part is finished.

For independent ownership, apply the shared contract's optional progression from explanation to less-guided variation, diagnosis, or recovery. Use real source and documented tools, and record the user's actions and assistance needed. Continue requested help; gradual independence is not a reason to withhold it.

## Synchronization and resume

Once evidence is sufficient, update artifacts directly within scope: current facts, source snippets, commands, diagrams, QA status, troubleshooting, and learning gaps the user has expressed. When the user chooses a new design, update the target, catalogue, and useful rationale/ADR. Do not promote candidates to decisions, lower acceptance criteria to legitimize a bug, or equate passing tests with user understanding.

Keep the tutorial handoff brief: checkpoint/baseline, observed evidence, open question/decision, and next action. Do not create a generation/writer protocol or a second phase plan. If interrupted before synchronization, reread source/diffs on resume and check affected evidence. Current teaching sections explain the current baseline/target and evidence; remove prose about previous editing mistakes, reviewer fixes, or document revision comparisons. Preserve discussion, user corrections, and superseded reasoning in the historical record sections under [project-memory.md](project-memory.md). State current invariants/decisions where used, and update affected restatements when contracts change.
