# Learning experience and full ownership contract

## Two outcomes together

Build the enterprise product the user intends: capability, quality, security, reliability, delivery, operations, and cost must have corresponding requirements and evidence. At the same time, the user must be able to explain mechanisms, change code, diagnose failures, operate and recover the system, and evaluate architecture decisions for the next step. Small demos are steps toward that product; do not silently reduce the target to a prototype.

The blueprint maintains the whole product and its quality and ownership outcomes. A tutorial teaches through a runnable capability. Pairing feeds code, QA, and what the user has learned back into the roadmap. Agent tests do not demonstrate user understanding. The user can discuss or challenge an explanation instead of taking a quiz. Settle future decisions only when dependencies and learning readiness make them due.

## From the current tutorial to the next decision

After a meaningful checkpoint, use source, QA, and actual discussion to connect: **observed behavior → a mechanism the user can reason about or is still struggling with → the decision now due → the next learning/build step**. Record briefly in the active tutorial: product/quality evidence, user learning evidence or a specific gap, settled/open decisions, and the next action. Sync only affected outcomes and dependencies to the blueprint; do not create another report, grading scale, or parallel checklist. Discussion, predicting and checking state, diagnosis, modification, and operation can all provide learning evidence. Record only what was observed; do not ask the user to prove again what they already know.

If a decision is technically due but the user says they do not understand a prerequisite, or their reasoning reveals a mistaken mechanism, keep the decision and dependent implementation pending. Use an explanation or trace at the checkpoint, or a small learning experiment runnable on a safe baseline, to observe the missing mechanism. Include setup, actions, expected state/failure, and cleanup. Return to the same decision with the new evidence, using one question and one HTML artifact. Do not choose the architecture for the user, lower acceptance criteria, or expose a capability without required controls. If evidence of understanding is absent, record it as unknown and continue discussion or independent work; do not infer incompetence or create a quiz gate. Make substantial catalogue changes only after discussion and independent review under the existing design contract.

Example: the user does not understand why a retry creates two jobs. Trace a committed request whose response is lost → the client retries → a second transaction may create a second job. Transactions and identifying the same business action solve different problems. Observe retries safely in a local environment before choosing an idempotency lifecycle or store. If an invariant forbids duplicates, failing behavior still fails acceptance; a learning experiment does not authorize releasing the bug. Identity and isolation for a shared service are still required before shared exposure, but do not bundle those questions into the retry decision.

Match cognitive load to the current step. Put essential context, code, visuals, and QA in the main content; put alternatives that are not yet due and deeper material in expandable sections. If one tutorial requires several unfamiliar mechanisms to settle independent decisions, split it by prerequisites and small demos. Do not solve this by removing explanations or authoring a whole phase in advance.

## Project root and artifact layout

Determine the project root once from the workspace where the user starts the workflow, or from an explicitly designated root. Prefer an explicitly requested documentation path. Git roots, build files, and submodules help locate source; they do not automatically redefine the project root. Preserve that root across skills and changes of working directory for builds.

For example, a workflow starts at `/workspace/product`, with source at `/workspace/product/app`:

```text
/workspace/product/
├── docs/learn/
│   ├── index.html
│   ├── learn.css
│   ├── tutorials/NN-topic.html
│   ├── decisions/NN-one-question.html
│   └── explainers/topic.html
└── app/                          source/build root
```

Record the project, learning, and source roots in the blueprint's baseline section; guide and pair read them there. No separate state file is needed. Create directories only when they have a corresponding artifact. Calculate source links from the actual HTML file location.

The default learning root is `<project-root>/docs/learn`. Existing documentation in a source subdirectory does not justify making that subdirectory the new root. Read it as context and identify any layout mismatch. Do not automatically move, delete, or copy all documentation, or change the canonical root. If the user asks to edit a specific file elsewhere, edit that file; migrate only when assigned. For new artifacts, use the chosen learning root without recreating all old documents merely to fill out the directory tree.

## Asking and settling decisions

### Identify the question that is due

Read the context and reuse existing decisions and specific delegated choices. Routine choices within the assigned scope need no additional approval. Ask **one question per turn**, with only **one pending question across the workflow**. Defer other uncertainties with triggers. Do not combine independent questions as subquestions, multiple form fields, or a list at handoff.

### Prepare one decision HTML artifact

Give each question its own `decisions/NN-topic.html` file about one subject. Provide enough substance for the user to reason:

1. The question, affected outcome, baseline, why it must be decided now, and the dependent work waiting on it.
2. An in-place glossary: each new term's meaning, ownership, example from the product/source, and place in the flow.
3. A visual of the mechanism and each option: paths, boundaries, or changing state, with captions/legends and worked input/output.
4. Advantages and disadvantages compared on the same dimensions, including failure, security, operations, reversibility, and revisit triggers. Label recommendations accurately with long-term, cost, short-term, or least code change tags.
5. Engineering and learning effort, runtime/resource/operating costs, and migration costs. State assumptions; monetary prices require current sources. If there is no monetary cost yet, say so rather than omitting cost.
6. Room to choose, write another option, combine options with reasons, challenge the premise, or request further explanation. Do not force A/B/C answers.

Separate facts, inferences, and estimates. Check API/types, option semantics, and diagnostics against the actual version. For concurrency and streaming, compare demand, buffer bounds, thread ownership, cancellation, and error/terminal propagation at the same boundary when relevant. Adapter line counts, one happy-path spike, or the absence of warnings do not establish total cost, risk, or reversibility. State what remains unmeasured and the conditions behind the recommendation.

### Present the artifact, ask in conversation, then wait

Format and validate using [html.md](html.md), open an available preview/browser, and put a clickable artifact link next to the question. If the UI cannot open, link the created file and state the limitation. Do not replace HTML with a CLI table or claim to have inspected rendering. Use an interaction tool that supports freeform answers; if only fixed options are available, ask in plain text. Do not create a fake form or Submit button.

After presenting the artifact, ask **one actual question in the conversation**, then yield and wait for the user. A question inside the HTML does not replace this step. If the question was asked in an earlier turn, keep it pending without repeating it. Do not author questions in batches; the next question depends on the answer just received.

When the user answers, explain or adjust the page if they are still uncertain, and record the settled choice and rationale in that same file. A recommendation, pending label, compile spike, generic instruction to continue, silence, or default selection is neither a choice nor evidence of understanding. Keep decision HTML for tutorial reuse, while retaining essential content within the tutorial itself.

### Work allowed while a decision is open

If a decision changes a public contract, concurrency/lifecycle, trust boundary, or checkpoint implementation, **both dependent code and dependent implementation instructions remain pending**. Do not write or publish a full tutorial around a default option and ask for the answer at the end.

Continue explanations, comparison snippets, small spikes, or independent checkpoints to gather evidence; these do not become the selected target. If the user explicitly requests a draft under a specific assumption, produce that draft with its assumptions and limits. Do not treat it as an implementation decision.

## Each page stands on its own

Where an invariant, decision, or prerequisite is used, state **its actual content + why it applies + its consequences for the current code/QA**. For example: “Each run emits only one terminal event; both the error and completion branches pass through the terminal guard to prevent two results.” An `INV-3` identifier or blueprint link supplies additional provenance, not a substitute for this explanation.

The glossary needed for the code, and the context and visualization needed for its mechanism, must appear in the current tutorial/decision. Repeat essential material from earlier pages with appropriate wording, without copying entire chapters. Links to full source, decisions, and explainers support deeper study or verification. When an invariant or decision changes, check its restatements in affected tutorials for consistency; intentional duplication must be synchronized.

Each new mechanism needs a causal explanation of its algorithm or boundary, plus a worked example: concrete input → transformations/intermediate states → output. Identify the symbols implementing each step and relevant branches/failures. Use sequence diagrams for interactions, state diagrams for lifecycles, graphs for ownership/dependencies, and trace tables for algorithms. Provide enough visualization to follow the causal flow; decorative boxes or component names alone are insufficient. Interactive stepping helps with multiple transitions or races, but does not replace explanatory text or justify invented chart values.

## Current documentation, not editing history

After implementation, pairing, or reviewer findings, rewrite explanations, snippets, diagrams, commands, and QA so they describe the same current baseline/target. Remove incorrect claims and accounts of what an older draft got wrong, what the reviewer fixed, “the documentation previously showed…”, “correction…”, or document revision comparisons. Do not retain incorrect reasoning and negate it below. Reviewers return findings to the author; they do not insert review dialogue into the lesson.

Preserve valid rationale for the current design, actual limits and evidence, unmet acceptance criteria, and pending status. Distinguish current source from code the tutorial intends to create; do not claim planned code is implemented. Checkpoints may use diffs to apply changes from an identified baseline to a target, without narrating edits to the document itself. If migration between runtime versions is the user's task, explain it using two clear baselines; that is not editorial history.

When the user asks more about a mechanism, sync the essential explanation into the original checkpoint and keep a deeper explainer if useful. A later reading should not depend on asking the same follow-up. End the tutorial by stating the specific knowledge used and the next decision it prepares for. Do not open several questions or mark the user as having understood.
