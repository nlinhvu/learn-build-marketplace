# Contributing

Keep changes focused on helping an engineer build, understand, and own a real product.

Preserve one-question decision gates, runnable incremental tutorials, explicit implementation authorization, self-contained explanations, and separate evidence for runtime behavior and human understanding. Do not add a mandatory whole-phase planning workflow.

The skill directories in `plugins/learn-build` and `plugins/learn-build-vn` are the distribution source of truth. Keep both editions behaviorally aligned and preserve matching resource paths. Shared reference copies must remain byte-identical within each language so each skill can be installed independently. Keep relative links inside the skill directory. Do not introduce personal paths, project-specific policy, secrets, or agent-specific tool dependencies. Vietnamese prose keeps English technical terminology; all source/test code, including comments/docstrings, stays English.

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. For behavior changes, exercise a realistic scenario and a counterexample, including a pending architecture decision. Review generated HTML and code consistency when relevant; static checks alone do not prove teaching quality or compliance.

Learn OSS lives in `plugins/learn-oss-vn` with `learn-onboard`, `learn-catalogue` and `learn-recipe`. Preserve its distinct priority: accessible learning, useful community sharing, then contribution. Onboarding generates developer documentation from source without requiring upstream docs; preserve source exclusions and distinguish usage guides/reference from implementation recipes. Keep glossary, rendered diagrams, numbered walkthroughs and code consistent; separate public documentation from personal learning records. Documentation/catalogue coverage and source evidence must stay honest. Shared references/assets remain identical within its three self-contained skills.

Version each plugin consistently across its Codex and Claude manifests. The two Learn Build editions share a version; Learn OSS versions independently. Bump `package.json` for package releases. Validate changed plugins through native marketplaces in isolated configuration directories. The pi native package selects English Learn Build; portable installation selects its edition with `--language`, or Learn OSS with `--plugin learn-oss-vn`. Report which hosts were actually exercised. Never describe self-review as independent review.

Do not commit temporary working specs, plans, evaluation outputs, or reference screenshots. Keep `docs/superpowers/` ignored; ship only skill resources, distribution code, useful tests and maintained user documentation. This does not remove the HTML context-retention requirements for projects using the skills.
