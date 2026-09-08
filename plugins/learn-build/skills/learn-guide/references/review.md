# Independent tutorial review

## Assign independent review

When an artifact is concrete enough and an independent reviewer is available, give that reviewer a separate context containing requirements, settled constraints/decisions, artifact and source/configuration/dependency paths, and relevant evidence. The reviewer works read-only and returns evidence-backed findings with location, severity, basis, proposed fix, and unverified scope. Do not combine reviewing with editing the artifact.

## Check content for this role

- Runnable scope: baseline, prerequisites, exact paths/symbols/code, setup/wiring, and observations are sufficient for the user to implement. A symbol that the tutorial plans to create is not wrong merely because it is absent from current source.
- API and artifact: critical APIs match the actual package/source version or have a compile spike. Verify exact snippets after HTML decoding; another spike or source file is not evidence for the current artifact.
- Behavior: trace success and exceptions/error-as-data across boundaries to terminal behavior, state, and exit codes. A fake error event does not prove a thrown exception is handled. Actual QA accurately identifies fake/live dependencies and environment scope.
- Feasibility: a source declaration does not establish dependency resolution; compilation does not establish runtime behavior. Material uncertainty needs an experiment before dependent work, or an explicit unready checkpoint. Do not require prebuilding the whole feature.

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
