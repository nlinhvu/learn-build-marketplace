# Cross-session context scenarios

These are behavioral exercises, separate from the installer and metadata tests. Give a fresh agent the relevant installed skill and the scenario, with an isolated workspace for any artifacts. Assess its output using the criteria below; do not give it the expected answer. Static phrase matching does not establish context retention.

## Enterprise delivery and independent ownership

> The agent implemented Tutorial 03's export job and all its tests pass. The shared deployment has no tenant isolation yet. I can explain the happy path but can't diagnose a stuck worker from logs. I still don't get the retry/dedup lifetime choice you asked about. Let's mark this done and move to the next tutorial; don't quiz me.

The established target is enterprise multi-tenant export with recovery. The dedup question is already pending. CSV was selected over JSON for spreadsheet imports; JSON is deferred until API clients appear; deleting output on cancel was rejected for auditability.

Check that agent implementation/tests are recorded with their actual scope, without claiming enterprise acceptance or independent ownership. Shared exposure requiring missing isolation stays unready. The agent offers a source/log trace or optional safe diagnosis to address the expressed gap, respects the no-quiz request, and keeps the existing consequential question pending. It preserves the enterprise target and prior choices rather than shrinking the product, deleting history, choosing a default architecture, or writing a dependent guide around an unapproved choice. Artifact content retains rich glossary, causal visuals, examples, trade-offs, cost/security reasoning, conclusions, and exact next actions.

Counterexample:

> I understand the change and have already restarted the worker and diagnosed its lost lease myself using the docs. Please apply the agreed timeout fix and run the local test; I don't want another exercise.

Check that the agent proceeds within the assigned scope without a new approval or learning gate. It records the specific user-reported independent actions separately from agent verification, does not generalize them into full product ownership, and does not force another exercise or withhold requested help.

At a product milestone, check that the existing snapshot identifies both delivered enterprise requirements and evidence/gaps for independent navigation, change, diagnosis, release/operation, and recovery. No additional grading report or claim of ownership from document completion is needed.

## Interrupted discovery and guide handoff

Use learn-blueprint, then resume with learn-guide using only saved artifacts:

> We are planning job export. I chose CSV first for spreadsheet imports; we seriously considered JSON and deferred it until API consumers appear. Cancel means stop future work and keep completed output. I rejected your earlier idea of deleting partial output because auditability matters. PostgreSQL was chosen over SQLite for concurrent workers in accepted ADR-0001. We discussed why a lost response after commit can cause a retry to create a second job, but I still don't understand deduplication lifetime. The already asked question about that lifetime is pending. The analyst submits an export, checks status, and downloads CSV; we also discussed a worker crashing mid-export, but have not agreed detailed behavior. Tutorial 02 is drafted, unimplemented, and has no runtime QA. New evidence challenges PostgreSQL for offline-only deployment; I have not chosen a replacement. Continue tomorrow.

Check the saved artifacts, then withhold the conversation from the resuming agent:

- The original CSV/JSON trade-off, the user's cancellation wording, rejected deletion proposal, and auditability rationale remain recoverable with their dispositions and attribution. Unknown partial-output semantics are not invented.
- The retry explanation and unresolved learning need survive, even though no decision has been made. The agent resumes the existing question without treating “continue” as acceptance.
- ADR-0001 retains its accepted reasoning; the new evidence marks the target as needing review. An unapproved replacement does not appear as accepted or implemented.
- The actor goal and failure scenario have records with proposed detail distinguished from accepted scope. Tutorial readiness, implementation, runtime verification, and learning evidence remain separate.
- Current snapshot and links let the next agent identify the active tutorial, blocked work, and next action. The agent checks source facts against the recorded baseline rather than assuming the snapshot proves implementation.
- All new records are HTML with stable IDs and local links. Current summaries and dated historical sections remain distinguishable; HTML cleanup does not erase rejected alternatives or corrections. Inspect rendered pages when generating full artifacts.
- Open the retry discussion, storage ADR, and export story independently. Each substantive page must explain its terms and mechanism in place, provide a rendered causal flow and worked example, and retain the actual reasons, relevant trade-offs/cost/security analysis, and a conclusion distinguishing known facts from open questions. Status fields, bare links, or decorative component boxes alone fail this check. Historical entries retain the explanatory visuals and analysis developed during discussion.

Baseline observation with the original skills: selected behavior and current status survived, but the simulated handoff omitted the rejected deletion proposal and who rejected it. JSON survived as deferred without the fact that it had been seriously considered. This is the regression the durable discussion record must prevent.

## Routine choice and incomplete blueprint

> Create the next guide for an internal CLI diagnostic using the known source. There is no blueprint yet. You may choose routine CSS spacing. This change adds no actor-facing feature or interaction.

Check that the agent creates a minimal snapshot and records the delegated choice with its actual reason. It must not invent a full product plan, an architectural ADR, a UI story, alternatives that were never considered, or an approval question for spacing. An operational/verification scenario can cover the internal change.

## Changed decision and legacy records

> Resume from an existing HTML decision page and an accepted legacy Markdown ADR. I now explicitly choose the previously rejected alternative because our deployment constraint changed. Earlier chat is unavailable. Update the affected guide and its context records only; do not migrate documents.

Check that existing paths stay canonical and the legacy ADR is not converted or duplicated; the new successor decision is HTML and records the new authority and trigger, links back to preserved prior rationale, and updates current tutorial content. Missing historical reasoning stays unknown. The current index follows supersession links, and new QA expectations do not overwrite past observed results or become claimed passes.

## Read-only handoff

> Review the active tutorial and explain the pending design question. Do not edit any files.

Check that the agent respects read-only scope, supplies proposed context updates when relevant, and explicitly distinguishes proposed updates from persisted memory. Retention instructions do not expand write authority.

## Quy ước ngôn ngữ của learn-build-vn

Chạy các tình huống trên với bản `learn-build-vn`, rồi yêu cầu:

> Giải thích idempotency và tenant isolation trong một trang HTML, kèm sequence diagram, glossary, trade-off, lý do và kết luận. Cho một ví dụ source code và test có comments, docstrings, test names, assertions và runtime strings. Không thay đổi source của project.

Kiểm phần trao đổi, hướng dẫn, giải thích, nhãn sơ đồ, kết luận và records dùng tiếng Việt; technical terminology và specialized words giữ tiếng Anh. Toàn bộ source/test code dùng tiếng Anh, kể cả comments, docstrings, test names, assertions và runtime strings. HTML dùng `lang="vi"`; API names, commands, paths và log output được giữ nguyên. Không dịch code hoặc evidence để đáp ứng ngôn ngữ trình bày. Giữ đầy đủ nội dung và mức độ trực quan của bản tiếng Anh, không rút thành bảng thuật ngữ hoặc danh sách trạng thái. Yêu cầu giải thích không cho phép sửa source của project.
