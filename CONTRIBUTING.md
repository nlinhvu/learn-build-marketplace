# Contributing

Keep changes focused on helping an engineer build, understand, and own a real product.

Preserve one-question decision gates, runnable incremental tutorials, explicit implementation authorization, self-contained explanations, and separate evidence for runtime behavior and human understanding. Do not add a mandatory whole-phase planning workflow.

The skill directories in `plugins/learn-build` and `plugins/learn-build-vn` are the distribution source of truth. Keep both editions behaviorally aligned and preserve matching resource paths. Shared reference copies must remain byte-identical within each language so each skill can be installed independently. Keep relative links inside the skill directory. Do not introduce personal paths, project-specific policy, secrets, or agent-specific tool dependencies. Vietnamese prose keeps English technical terminology; all source/test code, including comments/docstrings, stays English.

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. For behavior changes, exercise a realistic scenario and a counterexample, including a pending architecture decision. Review generated HTML and code consistency when relevant; static checks alone do not prove teaching quality or compliance.

Bump the version together in `package.json` and all four plugin manifests when releasing. Validate both language editions through native marketplaces in isolated configuration directories. The pi native package selects English to avoid duplicate skill names; portable installation selects one edition with `--language`. Report which hosts were actually exercised. Never describe self-review as independent review.
