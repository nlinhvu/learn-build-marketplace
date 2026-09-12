# Rich HTML for independent understanding

Rich visual explanation is the defining quality of all output HTML: blueprints, tutorials, decisions, discussions, ADRs, user stories, and explainers. It must help the user understand and work on the real product independently, serving the highest priority in [learning-contract.md](learning-contract.md).

## Content the reader can reason from

For every substantive topic, provide:

- **Detailed in-place glossary:** plain meaning, responsibility/ownership, concrete product example, and place in the flow.
- **Context and causal explanation:** the problem, why it matters, how the mechanism works, applicable constraints, and consequences for the code or operation.
- **Rendered visuals and worked examples:** diagrams, graphs, and flows with labeled boundaries, arrows/states, captions and legends. Trace concrete input → intermediate states → output, including relevant failures and actual source symbols.
- **Comparable alternatives:** benefits and drawbacks on the same dimensions, including engineering/learning effort, runtime/resource/operating and migration costs, security/trust/data implications, reliability, and reversibility where relevant. State assumptions and unknowns; use current sources for monetary prices. Explain when there is no monetary cost yet or a dimension does not apply.
- **Reasoned conclusion:** what evidence supports, why options were selected/rejected/deferred, consequences, limits, and the next action or unresolved question. Do not invent a decision to finish the page.

State the actual invariant, decision, or prerequisite and its implications where used. Links support provenance and deeper study; readers must not need another chat to understand essential content. Keep necessary code, explanation, visuals, and QA in place. Use expandable sections for deeper analysis, alternatives, and history; organize depth without removing it.

Choose visuals by the relationship: sequence diagrams for interactions, state diagrams for lifecycles, dependency/ownership graphs for boundaries and ordering, trace tables for algorithms, and comparison tables for trade-offs. Interactive stepping or scenario comparison helps with races and multiple transitions. Render with inline SVG/HTML or an available renderer; unrendered Mermaid source does not count. Decorative component boxes do not explain causality. Quantitative graphs require evidence or labeled assumptions; no chart quota or invented values.

## Durable records are rich HTML too

Use [project-memory.md](project-memory.md) for record fields and lifecycle. Put current position and resume links first; retain dated historical entries with stable IDs and explicit rejected/disproved/superseded labels. Preserve their glossary, worked traces, visuals, cost/security analysis, and conclusions. A brief metadata update need not repeat the whole explanation. Record outlines define retained content, not permission to output only a status ledger.

Current teaching sections explain the current baseline/target without editorial revision chatter. Historical sections preserve prior reasoning and corrections with links to the current position, so obsolete claims cannot be mistaken for current guidance.

## Structure and code

Reuse project HTML/CSS; [learn.css](../assets/learn.css) is a starting point when needed. Use semantic HTML with the document's language, UTF-8, viewport, title, navigation, main/section elements, heading hierarchy, and stable IDs. Start with outcome and next action. Use captions, accessible controls, and independently scrollable wide code/tables with scroll cues. Avoid page-wide horizontal overflow.

Give code exact paths/symbols and complete scoped edits. Escape HTML characters while preserving decoded language syntax and whitespace in pre/code; do not add extra Java/JSON/shell escaping. Verify code extracted from the final HTML, within its documented baseline or fragment context. Another scratch implementation does not validate the delivered snippets, and compilation does not prove runtime behavior.

Resolve local links/fragments from the actual file location. Interaction must work with the documented opening method; avoid mandatory CDNs or external requests outside scope.

## Verify before handoff

1. Use an available formatter/HTML5 validator. Check structure, escaping, accessibility semantics, duplicate IDs, links, and fragments. A custom parser or xmllint is a limited check, not HTML5 validation.
2. Open in a browser at desktop/mobile widths and inspect screenshots. Exercise details, interaction, keyboard/focus, code/table scrolling, contrast, and overflow.
3. Read each substantive page independently against the content bar above. Follow a real input through its visuals and code to success/failure; confirm glossary, reasoning, trade-offs, cost/security, and conclusions agree with source and decisions.
4. Report the actual scope and missing evidence. If tools are unavailable, perform available checks and mark rendering or execution unverified. Recheck affected content and links after edits.

Checks cover record pages and tutorials equally. A visually polished artifact does not by itself establish product correctness or user ownership.
