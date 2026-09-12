# Blueprint and adaptive catalogue

The main page should let the user answer: who the product serves, what the system contains, where requests/data go, how code is released, what quality is required, and what to learn next. Keep deeper details in expandable sections. State needed invariants and decisions on the page itself, with source/ADR links as provenance. Use [learning-contract.md](learning-contract.md) for roots, questions, and self-contained content.

Connect catalogue outcomes to work the user can eventually perform without an AI coding agent. At product milestones, revisit both enterprise acceptance and whole-product ownership using the shared contract; retain gaps even if delegated implementation is complete.

## Catalogue

Link capability entries to the user stories already discussed and their scope status under [project-memory.md](project-memory.md). Record actor goals, rules, and edge cases during discovery, including candidate/deferred flows. The catalogue summarizes outcomes; the story records preserve their evolving intent. Do not wait for a tutorial to exist before saving a story, or invent future walkthrough detail to fill it.

Each entry includes an intended outcome/demo, a mechanism-based learning outcome, technical prerequisites, learning prerequisites, target environment, and relevant quality concerns. State what the user will be able to explain, change, debug, or operate, and which next architecture decision that knowledge prepares them for. Preserve the path to the selected enterprise target; do not end the catalogue at a local demo. Label known languages/frameworks/libraries/infrastructure as Observed, Decided, Candidate, or Deferred. Do not fill in a stack merely to complete a template. Commands, exact files/symbols, and exercises are needed only when authoring the guide now due.

One tutorial adds a demonstrable capability or operational outcome from an explicit baseline without depending on future tutorials. It may build on previous tutorial code. A checkpoint is a small step with an observable change or result; it need not independently deliver a capability. Split a tutorial if multiple new mechanisms force choices before their prerequisites are understood.

Count baseline and conditional tutorials separately. Mutually exclusive alternatives are not both commitments. Date estimates, state their assumptions, and identify unknowns that may change the total. Even with incomplete information, provide a useful catalogue for what is known.

Example: a job API progresses through create → status → recovery, while learning progresses through contracts/data ownership → lifecycle → crash windows/idempotency. Queue technology can wait for workload and recovery evidence. If data loss already violates a current requirement, fix the current scope rather than silently deferring it.

## Feedback into the blueprint

When selecting the next tutorial, use the transition in [learning-contract.md](learning-contract.md): read current behavior/evidence and learning gaps, identify which decision is actually due, and determine which prerequisite needs an experiment first. Keep the full enterprise target visible through previews of future outcomes, dependencies, and conditional branches. Detail implementation only for the tutorial now due with sufficient grounding. Do not fill unknowns with stack commitments.

After a tutorial, or when an assumption is disproved, compare actual capabilities, evidence, remaining learning gaps, and next-step dependencies. Add, remove, split, merge, or reorder tutorials as needed. Update only affected content; do not regenerate the whole program each cycle.

Without a new decision, record the candidate and impact while marking the existing target as needing review. Once the user chooses, update the target and catalogue, and record the choice with its authority and supersession links under project-memory.md. Preserve earlier rationale and rejected alternatives in the records. Do not lower requirements to match incorrect implementation. Keep one link to the active tutorial, with detailed progress and evidence there, avoiding competing checklists.
