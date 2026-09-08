# Contract for the current tutorial

## Opening

State the added capability, demo, learning outcomes, baseline/source inspected, prerequisites, environment, and current limits. Provide necessary setup/start/stop commands, safe data, and initial state for a repeatable walkthrough. Check new versions/tools for project compatibility; do not upgrade merely to use the latest release.

## Followable checkpoints

Each checkpoint answers, in place:

1. What problem it solves and why this step comes here.
2. Context/glossary and the actual invariant/decision. For a new mechanism or architecture, include a rendered visual and a worked input → intermediate steps/states → output example tied to real symbols, including relevant branches/failures. Explain why the algorithm or boundary behaves this way.
3. Exact paths, symbols, and code to add, replace, or remove. Use complete snippets for the edit scope or diffs with clear anchors. Do not hide required logic behind ellipses. Link full source for comparison while keeping essential code and explanation in the checkpoint.
4. Commands/actions, expected UI/API/CLI/state/log results, and how to recognize failure. Distinguish expected from observed, and identify the baseline/environment for executed evidence.
5. Troubleshooting from symptoms to likely causes, diagnostic steps, and remedies. Code may differ from the guide after implementation.

A checkpoint need not deliver an independent capability, but must include an appropriate observation or verification step. The complete tutorial must be demonstrable without code from future tutorials.

Example: add status lookup to a job API that already creates jobs. Explain lifecycle → add lookup using the store's actual API → wire a GET handler → QA known/unknown IDs. Retry and durable storage remain previews if not yet due; do not force a queue choice before status lookup.

## Decisions and quality at the point of use

Present settled decisions fully where used, with rationale, context/evidence, trade-offs, cost/security, reversibility, and revisit triggers. When the user must decide, follow [learning-contract.md](learning-contract.md): one question, its own HTML presented before asking, freeform answers, and waiting for the response. Use long-term, cost, short-term, or least code change tags accurately. Do not force multiple alternatives for a routine choice.

Attach quality to actual changes: security/trust/secret boundaries, correctness/data, timeout/retry/recovery, telemetry, cost drivers/bounds, build/CI/CD/IaC, and release/rollback when relevant. State which controls are needed now, which gaps remain unmet, and the environment checked. “Enterprise” means requirements with evidence, not a quota of patterns or diagrams.

## Manual QA and learning

A walkthrough includes the actor, setup/reset, ordered real actions, expected/actual results, a suitable negative/failure path, evidence, and cleanup/rollback. Use the real UI for UI claims, curl/CLI for APIs/processes, and authorized cloud tools for infrastructure. The agent can run QA or guide the user when access/tools are missing.

After removing test-runner commands, manual QA must still be a walkthrough observing actual behavior. Assertions and unit tests are supplementary checks.

Keep product behavior, quality evidence, and user understanding separate. Predicting state after a crash, diagnosing through logs, or changing a small contract can reveal what needs explaining. Do not turn this into a compulsory exam.

## Verify the artifact and error paths before handoff

For new or changed code/snippets, verify risky runnable portions using code extracted from the final HTML itself in an isolated scratch/baseline environment when tools are available. Compilation checks syntax/APIs; run the needed scenarios to check behavior. For wire formats such as JSONL, pass multiple events through the corresponding parser to catch delimiter/escaping errors. Do not require prebuilding the entire product or calling paid services outside scope. State precisely what could not be executed, and do not mark dependent checkpoints ready while uncertainty could break them.

Trace both success and failure through actual layers: does a callback emitting an error event consume the exception, or does it still escape to the caller? What terminal behavior, transcript/state, and exit code actually occur? A fake provider returning an error as data does not prove a real provider's thrown exception is handled. Choose a small reproduction for that semantically different error path and retain acceptance criteria when it fails. Manual walkthroughs must state network/account prerequisites accurately. A model prompt does not guarantee a tool call or particular invalid input; give conditional expectations and a controlled local trigger where needed to observe failure. Do not call a path offline if it still invokes a service.

## Synchronization and handoff

When implementation differs from the guide, sync snippets, commands, diagrams, QA, and explanations with facts and requirements. If code fails acceptance, the tutorial remains unmet; do not change expectations to hide the bug. Material design changes return to discussion; update targets and next tutorials only after decisions are settled. Write future guides only when their inputs are ready.

When syncing, remove editorial history and replace incorrect claims with correct explanations for the current baseline/target. Supplementary explainers do not replace in-place prerequisites. At the end, identify the knowledge the learner can use to decide the next step, rather than merely citing a decision identifier on another page.

Hand off using the transition in [learning-contract.md](learning-contract.md): connect a concrete behavior/trace to the mechanism to reason about and the decision it prepares for. For work not yet practiced, state the planned activity and missing evidence; do not write the user's answer for them.
