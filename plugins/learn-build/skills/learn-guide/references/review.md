# Independent tutorial review

## Review the concrete artifact

Give an available independent reviewer requirements, settled constraints/decisions, artifact and source/configuration/dependency paths, and relevant evidence. Review is read-only: return findings with location, severity, basis, proposed fix, and unverified scope. The author resolves them.

- Runnable scope: baseline, prerequisites, exact paths/symbols/code, setup/wiring, and expected observations let the user implement independently. Planned symbols may legitimately be absent from current source.
- Artifact/API accuracy: verify snippets extracted from final HTML against actual package versions. Another spike is not evidence for this artifact.
- Behavior: trace success and thrown exceptions/error-as-data through real boundaries to terminal state and exit codes. A fake error event does not establish exception handling.
- Feasibility: dependency declaration is not resolution; compilation is not runtime evidence. Test material uncertainty with a small experiment or leave the checkpoint unready, without prebuilding the whole feature.

## Check the shared outcomes

Read [learning-contract.md](learning-contract.md), [html.md](html.md), and [project-memory.md](project-memory.md). Check their requirements against the artifact:

- Does the work advance the intended enterprise product and the user's ability to change, diagnose, or operate it without agent guidance? Product evidence, user actions/assistance, and unknown abilities stay distinct.
- Can the user reason from in-place glossary, causal visuals, examples, trade-offs, cost/security analysis, conclusions, and practical instructions?
- Are consequential decisions supported by actual authority, with the one-question process respected? Misunderstood prerequisites get explanation/experiments; routine delegated choices get no new approval or quiz gate.
- Can a new reader resume from saved records, recovering corrections, rejected alternatives, non-ADR reasoning, stories, pending work, and supersession without chat? Missing legacy context stays unknown.
- Do required controls and real manual failure/recovery QA precede relevant exposure? Test-runner output alone does not replace a walkthrough.

## Resolve and hand off

The author fixes findings, synchronizes current content while preserving historical reasoning, and checks affected work. Seek another review for material design changes or uncertain resolution. Keep dependent checkpoints unready when unresolved issues could break them.

Validate HTML under html.md. Report independent review, execution, rendering, and user ownership as separate scopes. If no reviewer is available, perform self-checks and explicitly state that independent review was not performed.
