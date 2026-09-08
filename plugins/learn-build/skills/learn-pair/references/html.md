# HTML engineers can read and follow

Save discussion visuals and trade-offs in the documentation. Preserve the learning root established in [learning-contract.md](learning-contract.md). Reuse existing HTML/CSS there; copy [learn.css](../assets/learn.css) as a starting point if the project has no style.

## Content organization

Use semantic HTML with `lang="en"`, UTF-8, a viewport, a short title, nav/main/section elements, a heading hierarchy, and stable IDs. Start with the outcome and next action. Show immediately needed material first, with an in-place glossary and expandable deep dives/alternatives. Give code exact paths/symbols, escape &, <, and >, and preserve whitespace with independently scrollable pre/code blocks. Source links must resolve in the artifact's actual context.

Choose visuals to fit the question: sequence diagrams for interactions, state diagrams for lifecycles, dependency graphs for ordering, worked traces for algorithms, graphs for boundaries/dependencies, and tables for trade-offs. Render diagrams using inline SVG/HTML or an available renderer; unrendered Mermaid source does not count as a diagram. Include captions/legends and distinguish current/target and observed/expected. Quantitative charts need evidence or explicit assumption labels. Every new mechanism or architecture needs a visual sufficient to follow its causal flow and a worked input → intermediate states/steps → output example tied to real symbols. Use interactive stepping or branch comparison when useful; do not force every chart type into one page.

The optional CSS provides wrap, top, eyebrow, lede, toc, grid/two, card/selected, note/pending, table-scroll, flow, diagram/lane/node/arrow, small, and tag classes. It is a starting point, not a fixed section count. Inline interaction JavaScript must work with the documented way of opening the artifact; avoid mandatory CDNs and requests outside the assigned scope.

## Copyable, verifiable code

Code in HTML must preserve its language syntax after HTML entity decoding. Do not add an extra layer of Java/JSON/shell escaping in pre/code. When editing logic or literals, extract code from the final HTML to verify it. Do not validate a different temporary source and claim the artifact itself passed. For fragments, verify them within their documented scope/anchor; compiling a fragment does not mean the whole tutorial was built.

## Before handoff

1. Use an available formatter/HTML5 validator. Fix structure, escaping, accessibility semantics, duplicate IDs, local links, and fragments. A custom parser or `xmllint` does not replace HTML5 validation; if those are all that were used, describe the actual checks. Do not disable a rule to hide a content problem.
2. Open the page in a browser at desktop and mobile sizes, expand details and interactions, and inspect screenshots directly. Check text, code, tables, diagrams, contrast, focus/keyboard behavior, and overflow. Wide tables need their own scroll area and a scroll cue when needed; the page must not overflow horizontally.
3. Compare visuals with source, decisions, and text. Follow a concrete input through the diagram and code to output, including relevant branches/failures. A polished graph with incorrect branches/flow or only component names does not teach the mechanism.
4. Report the actual validation scope. If a browser or tool is unavailable, perform available checks and state that rendering is unverified; do not claim visual QA passed. After an edit, recheck only affected content and related links.

Keep enough evidence, version, and environment context to identify the document's baseline, without annotating every sentence. Do not edit unrelated artifacts. Read the page independently to verify its context: essential glossary, invariants/decisions, and explanations must be present in place. Links add provenance and depth. Remove editorial history; do not preserve incorrect reasoning followed by a correction.
