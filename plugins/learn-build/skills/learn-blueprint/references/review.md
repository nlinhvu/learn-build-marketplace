# Independent blueprint review

## Assign independent review

When an artifact is concrete enough and an independent reviewer is available, give that reviewer a separate context containing requirements, settled constraints/decisions, artifact and source/configuration/dependency paths, and relevant evidence. The reviewer works read-only and returns evidence-backed findings with location, severity, basis, proposed fix, and unverified scope. Do not combine reviewing with editing the artifact.

## Check content for this role

- Product fit: current/target/candidate states, boundaries, and assumptions agree with requirements and source.
- Catalogue: the enterprise target, technical/learning prerequisites, and conditional estimates remain intact; future tutorials do not require premature detail or commitments.
- Quality: controls have deadlines before dependencies/exposure. Stack/standard choices and recommendations have a basis without false precision.

## Check the learning experience and decision authority

Read [learning-contract.md](learning-contract.md), then verify:

- The project/docs root remains correct with nested source. In-place context is not replaced by an identifier or link. A page read independently explains invariants/decisions, why they apply, and consequences for code/QA.
- A single input can be traced through visuals, real symbols, and output/failure. Essential content appears at the checkpoint; separate explainers add depth. Learning outcomes prepare the user to design, change, debug, operate, and make the next decision.
- Each question has one decision HTML, freeform response support, and an actual question in the conversation. Settled targets have evidence of choice or delegated authority. A pending banner neither replaces the question nor permits the full dependent guide. An explicitly requested assumption-based draft stays within that request.
- Decisions now due with misunderstood prerequisites have an explanation/small experiment, and dependent work stays pending. Delegated routine choices do not acquire extra approvals or compulsory quizzes.
- Trade-offs use actual version-specific APIs/diagnostics and semantics. Estimates account for lifecycle, errors, buffering, and migration costs.
- Required controls and manual failure/recovery walkthroughs precede exposure where relevant. Removing test-runner commands still leaves QA that observes actual behavior. Agent checks and simulations are not human learning evidence.

## Resolve findings and conclude

The author resolves findings under the synchronization contract, preserving acceptance criteria, evidence limits, and current explanations without inserting review history into learning content. Recheck affected work. Seek another review when a material design changes or resolution remains uncertain. Unresolved assumptions, code problems, or failure-path issues leave dependent checkpoints unready.

If no independent reviewer is available, perform the checks possible and explicitly state that independent review was not performed. Design verdicts, execution evidence, rendered QA, and user learning are separate scopes; claim only what was actually checked. Validate HTML using [html.md](html.md) before handoff.
