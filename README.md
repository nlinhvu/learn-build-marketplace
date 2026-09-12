# Learn Build

Build an enterprise product you understand and own, one runnable tutorial at a time.

The highest priority is both the enterprise product you intend and your ability to develop, change, diagnose, release, operate, and recover it without an AI coding agent. Rich visual HTML and durable discussion records support those outcomes. Delegated implementation remains welcome; agent completion and your independent ownership are tracked separately.

This marketplace contains **two language editions: `learn-build` (English) and `learn-build-vn` (Vietnamese), each with the same three skills**. They connect product direction, architecture decisions, implementation, and hands-on verification without asking you to decide an entire future phase before you have learned from the current slice.

| Skill | Purpose |
| --- | --- |
| `learn-blueprint` | Establish the product architecture and an adaptive tutorial catalogue. Keep future implementation decisions open until their prerequisites are understood. |
| `learn-guide` | Create the next incremental HTML tutorial, with local context, glossary, causal diagrams, code, trade-offs, cost, security, and a runnable QA walkthrough. |
| `learn-pair` | Discuss, implement when delegated, debug, verify real behavior, and keep the tutorial and blueprint aligned with the current code. |

The workflow is **blueprint → next tutorial → implement and verify → feed evidence back into the blueprint**. You retain architecture decisions: a consequential unresolved choice gets its own saved HTML companion, one actual question, and a wait for your answer. A recommendation is not consent.

## Install

Choose **one installation method per agent**. Some agents discover other agents' skill directories too; remove an older duplicate installation if the same skill appears twice. Start a new agent session after installation.

### Codex — native marketplace

With a current Codex CLI that supports `codex plugin`:

```sh
codex plugin marketplace add nlinhvu/learn-build-marketplace
codex plugin add learn-build@learn-build-marketplace
```

Ask Codex to use `$learn-blueprint`, `$learn-guide`, or `$learn-pair`. If your Codex version does not provide plugin commands, use the portable installer below with `--agent codex`.

### Claude Code — native marketplace

Run inside Claude Code:

```text
/plugin marketplace add nlinhvu/learn-build-marketplace
/plugin install learn-build@learn-build-marketplace
```

Invoke `/learn-build:learn-blueprint`, `/learn-build:learn-guide`, or `/learn-build:learn-pair`.

### pi — native Git package

```sh
pi install git:github.com/nlinhvu/learn-build-marketplace
```

Invoke `/skill:learn-blueprint`, `/skill:learn-guide`, or `/skill:learn-pair`. Add `-l` to the install command for project-local installation.

The native pi package selects the English edition to avoid duplicate skill names. For Vietnamese, use the portable installer with `--agent pi --language vi` instead of the native package.

### Bản tiếng Việt — learn-build-vn

Bản này giữ cùng enterprise/ownership outcomes, HTML giàu visual và toàn bộ discussion context như `learn-build`. Technical terminology và specialized words giữ tiếng Anh. Toàn bộ source/test code, comments, docstrings, identifiers và runtime strings dùng tiếng Anh; phần giải thích/hướng dẫn còn lại dùng tiếng Việt.

Trong Codex:

```sh
codex plugin marketplace upgrade learn-build-marketplace
codex plugin add learn-build-vn@learn-build-marketplace
```

Nếu chưa thêm marketplace, chạy lệnh `marketplace add` ở mục Codex trước. Gọi skill với namespace `learn-build-vn`, ví dụ `$learn-build-vn:learn-blueprint`.

Trong Claude Code:

```text
/plugin marketplace update learn-build-marketplace
/plugin install learn-build-vn@learn-build-marketplace
```

Gọi `/learn-build-vn:learn-blueprint`, `/learn-build-vn:learn-guide` hoặc `/learn-build-vn:learn-pair`. Thêm marketplace trước nếu chưa có. Quy trình auto-update ở dưới áp dụng cho cả hai plugin; manual update dùng đúng tên plugin.

Portable installation:

```sh
python3 scripts/install.py --agent codex --language vi
```

Hai bản portable dùng cùng tên `learn-blueprint`, `learn-guide`, `learn-pair`, nên mỗi destination chỉ chứa một ngôn ngữ. Khi đổi/cập nhật bản đã có, thêm `--force`; installer lưu backup bên ngoài thư mục discovery. Sau khi cài native plugin và xác nhận hoạt động trong session mới, có thể xóa hoặc chuyển ra ngoài discovery **chỉ ba thư mục skill local cũ** để tránh trùng. Không xóa toàn bộ thư mục skills hay plugin cache.

### Cursor — portable installer

Requires Git and Python 3.9 or later. On Windows, use `python` if `python3` is unavailable.

```sh
git clone https://github.com/nlinhvu/learn-build-marketplace.git
cd learn-build-marketplace
python3 scripts/install.py --agent cursor
```

This copies all three complete skills into `~/.cursor/skills`. Invoke `/learn-blueprint`, `/learn-guide`, or `/learn-pair`, or ask Agent to use the skill by name. This installs local skills; availability in a remote or cloud agent depends on that agent's synchronization settings.

### Portable installation for any supported agent

From the cloned repository:

```sh
python3 scripts/install.py --agent codex
python3 scripts/install.py --agent claude
python3 scripts/install.py --agent pi
```

Run only the command for the agent you want. Default destinations are `~/.codex/skills` (or `$CODEX_HOME/skills`), `~/.claude/skills`, and `~/.pi/agent/skills` respectively.

For one project:

```sh
python3 scripts/install.py --agent cursor --scope project --project-root /path/to/project
```

Project destinations are `.agents/skills`, `.claude/skills`, `.cursor/skills`, and `.pi/skills`. For another agent supporting the `SKILL.md` format, select its documented directory:

```sh
python3 scripts/install.py --dest /path/to/agent/skills --dry-run
python3 scripts/install.py --dest /path/to/agent/skills
```

The installer preserves each skill's references, templates, and assets. Identical installations are skipped. Differing existing skills are never overwritten unless you pass `--force`; previous versions are saved under `.learn-build-backups` beside the skills directory, outside the discovery tree. Keep those backups until you have verified the update.

To update a portable installation, run `git pull --ff-only`, review changes, then repeat your installation command with `--force`. Portable copies do not update automatically. To uninstall, remove only the three installed `learn-*` directories from the chosen destination.

### Native plugin updates

Releases bump the version in both plugin manifests and `package.json`. Users following the repository's default branch can receive new versions when their host refreshes the marketplace; installations pinned to a tag or commit remain pinned.

In Claude Code, enable automatic updates once through `/plugin` → **Marketplaces** → **learn-build-marketplace** → **Enable auto-update**. Third-party marketplaces default to auto-update off. Apply downloaded updates with `/reload-plugins` or restart. See the [official auto-update guidance](https://code.claude.com/docs/en/discover-plugins#configure-auto-updates). To update manually:

```sh
claude plugin marketplace update learn-build-marketplace
claude plugin update learn-build@learn-build-marketplace
```

For Codex CLI versions supporting these plugin commands, refresh the Git marketplace and install the current version, then start a new session:

```sh
codex plugin marketplace upgrade learn-build-marketplace
codex plugin add learn-build@learn-build-marketplace
```

Automatic refresh depends on the host and user settings; a release cannot enable it for other users. Use the host's plugin/package manager to uninstall native installations.

## First session

Start in the workspace that should own the learning documents:

```text
Use learn-blueprint to help me build a multi-tenant support product.
I want to implement it myself and understand the architecture.
```

After the blueprint and current decisions are settled:

```text
Use learn-guide to create the next runnable tutorial from the blueprint and current source.
```

While implementing:

```text
Use learn-pair to explain this request flow and guide me through the real QA walkthrough.
```

Documents default to `<invocation-workspace>/docs/learn`, even when application source lives in a nested directory. An explicit document root takes precedence. Existing learning documents are not silently moved.

Discussion context is saved as you work, including unfinished questions, explanations, user corrections, non-architectural choices, and rejected alternatives. All new records are HTML: `discussions/` holds topic records, `adrs/` holds architectural decisions, and `user-stories/` holds actor goals and acceptance walkthroughs. Existing equivalent records keep their paths. `index.html` provides the current snapshot and links; a new session reads it and the relevant records, checks the actual source, and resumes the pending work. Tutorials stay current while historical reasoning remains available in clearly labeled record sections.

Tutorials explain their own relevant constraints and decisions rather than requiring you to follow opaque section IDs. Updates describe the current implementation rather than narrating why an earlier draft was wrong. Security, tenancy, reliability, deployment, operations, recovery, and cost are introduced before the relevant product exposure; a prototype is not labeled production-ready.

Agent execution, independent review, runtime QA, and evidence that you understand the product are distinct. The skills do not claim that tests prove your understanding. Browser rendering and independent subagents depend on the host's tools and permissions; when unavailable, the agent must report the limitation and must not claim an independent review or visual verification occurred.

## Package layout

```text
.agents/plugins/marketplace.json       Codex marketplace
.claude-plugin/marketplace.json        Claude Code marketplace
package.json                          pi package discovery
plugins/learn-build/                  English edition
  .codex-plugin/plugin.json
  .claude-plugin/plugin.json
  skills/
    learn-blueprint/
    learn-guide/
    learn-pair/
plugins/learn-build-vn/               Vietnamese edition, same structure
scripts/install.py                    Portable, dependency-free installer
```

Each language edition provides the same workflow across agents. Each skill includes its own supporting references so it also works when installed separately. There are no runtime dependencies, hooks, MCP servers, or credentials required by this package. Product implementation may require tools appropriate to your project.

## Compatibility and verification

Native marketplace installation is checked with Codex and Claude Code. The portable installer is exercised using temporary directories, including updates, conflicts, backups, and project scope. pi's package resource paths and Cursor's installed skill layout are checked structurally; that does not constitute a live interactive session in either agent. Host model behavior can vary, so instruction compliance is not guaranteed merely by installing a skill.

Installation formats follow the official documentation for [Codex plugins](https://learn.chatgpt.com/docs/plugins), [Claude Code marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), [Cursor skills](https://cursor.com/docs/skills), and [pi packages](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/packages.md).

## Development

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under [Apache-2.0](LICENSE).
