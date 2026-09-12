# Durable project context

Preserve the substance of every discussion so the user and a new agent can recover intent, reasoning, status, and next actions without the previous chat. All new records are rich HTML under [html.md](html.md); use [learning-contract.md](learning-contract.md) for ownership, roots, authority, and decisions.

## Record ownership

Use the established learning root. Create records only when content exists; reuse equivalent records and their paths. Read legacy formats as evidence without converting or duplicating them unless assigned.

| Artifact | Owns |
|---|---|
| `index.html` | Product snapshot, adaptive catalogue, active checkpoint, and record index |
| `discussions/NNNN-topic.html` | Topic history, including non-ADR decisions, explanations, and open questions |
| `adrs/NNNN-slug.html` | Enduring architectural choices, rejected alternatives, and supersession |
| `user-stories/US-NNNN-slug.html` | Actor goals, rules, acceptance, walkthroughs, and observed results |
| `decisions/NN-topic.html` | One question's rich teaching/comparison page and disposition |
| `tutorials/NN-topic.html` | Current lesson, code checkpoints, progress, QA, and ownership evidence |
| `explainers/topic.html` | Optional deeper explanation supporting essential in-place content |

The skill conducting an exchange updates its records. Blueprint captures product/story intent, guide elaborates the current capability, and pair records actual implementation, QA, and learning. Sync summaries and links without duplicating full histories or competing progress checklists.

Use stable identifiers and anchors. Allocate the next unused number per record kind; never reuse or renumber IDs. Link related records in both directions. Promoting a decision to an ADR leaves its discussion intact and points to the ADR as the decision's canonical record.

## Capture during discussion

After every substantive exchange, save new information before the next question or dependent work. Also save before yielding on an open question, switching skills, or ending a session. Update the existing topic, not a report per message; unfinished designs and non-decisions still need records.

Retain every distinct requirement, constraint, glossary definition, user statement/correction, story/edge case, option and trade-off, selection/rejection/deferral and reason, objection, explanation/worked trace, assumption, experiment/evidence and limit, learning need, and open question. Consolidate repeated wording without losing meaning. Quote user wording when it defines a contract. Do not fabricate transcripts, approvals, alternatives, missing history, or learning evidence; exclude secrets and unnecessary personal data.

Preserve the rich content developed during discussion, including glossary, rendered visuals, cost/security reasoning, and conclusions. Extend affected sections and reuse valid visuals rather than recreating the whole page on each exchange. The following fields organize content; html.md defines its explanatory depth.

## Topic records

Each topic page contains:

- Stable ID, title, scope/related links, and status: exploring, awaiting-answer, settled, deferred, or superseded.
- Current position separating observed facts, accepted choices, candidates, and unresolved issues.
- Dated entries with stable anchors: source/attribution; discussion substance and visual explanation; actual options, trade-offs and disposition; conclusion/rationale; authority or its absence; learning evidence and assistance needed; affected work and revisit triggers.
- Resume section: one pending question, whether already asked, missing answer, allowed independent work, next action, and other deferred questions with triggers.

A topic can be an explanation without any decision. A local choice retains its reasoning even without an ADR. Future topics retain only detail actually discussed.

When a position changes, append an entry preserving the old position, its original rationale, new evidence/answer, and successor link; update the current summary. Clearly label rejected or disproved historical ideas. Correct current teaching sections without erasing user corrections or rejected proposals from the record.

## Architectural decisions

Create an ADR as a choice lands when it affects architecture, shared contracts, data/trust boundaries, or substantial migration cost with enduring rationale. This includes foundational blueprint choices. The threshold determines where reasoning lives, not whether it survives; routine choices remain in topic records.

Each ADR contains ID/title, date/scope, related links, context/drivers, actual alternatives with visual explanation and comparable cost/security/risk analysis, decision/conclusion and rationale, authority/acceptance evidence, consequences/limits, revisit triggers, and supporting sources/versions. Status is proposed, accepted, rejected, deprecated, or superseded with a successor link.

Accepted decision and reasoning remain historical. A changed choice gets a successor ADR with reciprocal supersession links; status, link, and typo updates are allowed. Challenging evidence opens discussion and marks the target as needing review, without silently replacing acceptance. Missing legacy authority or rationale stays unknown.

## User stories and walkthroughs

Capture every discussed actor goal, rule, and failure/edge case immediately, even during blueprint discovery or before approval. One coherent goal may span tutorials. API consumers and operators are actors; internal changes with no actor flow can use an operational/verification scenario.

Each story contains:

- Stable ID/title; actor, goal/value, trigger, preconditions, intended success/postconditions, rules, edge cases, and unresolved detail.
- Links to discussions/ADRs, catalogue outcome, and tutorial checkpoints.
- Separate scope status (candidate/accepted/deferred/superseded), delivery status (unimplemented/in-progress/implemented), and verification (not-run/partial/passed/failed with baseline/environment/evidence).
- A walkthrough when due: setup/reset and safe data; ordered actor actions → system interactions/state → expected observable results; rendered flow through relevant boundaries and a worked example; negative/failure/recovery cases; cleanup/rollback; actual results and limits; conclusion/next action.
- Dated requirement changes with rationale, authority, prior behavior, and successor links.

Blueprint records known intent without inventing future click-level detail. Guide develops acceptance and walkthroughs for the current capability before dependent implementation instructions, resolving material open behavior through the decision process. Keep essential QA in the tutorial as well. Pair adds observed results with who/when/baseline/environment; intended behavior never becomes a claimed pass. Preserve past evidence when expectations change.

## Snapshot and resume

The compact snapshot in `index.html` records roots, inspected source baseline/revision/date, product scope and current versus target state, active tutorial/checkpoint, readiness/implementation/QA status, known ownership evidence/gaps, the one pending question, next action, and deferred triggers. Index topic/ADR/story IDs with status and links, including superseded records. A guide without a blueprint starts this minimal entry point from known facts.

At resume:

1. Read project instructions and snapshot; preserve roots.
2. Read the active tutorial and linked discussions/stories/ADRs plus applicable project-wide constraints. Follow supersession links and use the index to find relevant history.
3. Check source/configuration/diffs and evidence against the recorded baseline. Source establishes implemented facts; user decisions establish intended behavior. Record mismatches without silently redefining either.
4. Continue the next action, reusing settled choices and keeping an already asked question pending. Reopen only with new evidence, a revisit trigger, or user direction.

Index legacy context as touched; do not invent unavailable reasoning. If writes are prohibited, provide precise proposed updates and state that they are unpersisted.

Before handoff, verify coverage of substantive exchanges, links, and consistent statuses. A reader must recover what was wanted, chosen and rejected, why, what remains uncertain, what was built/tested, what the user can do independently, and what comes next.
