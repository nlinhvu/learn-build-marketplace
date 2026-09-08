# Contributing

Keep changes focused on helping an engineer build, understand, and own a real product.

Preserve one-question decision gates, runnable incremental tutorials, explicit implementation authorization, self-contained explanations, and separate evidence for runtime behavior and human understanding. Do not add a mandatory whole-phase planning workflow.

The three skill directories are the distribution source of truth. Shared reference copies must remain byte-identical so each skill can be installed independently. Keep relative links inside the skill directory. Do not introduce personal paths, project-specific policy, secrets, or agent-specific tool dependencies.

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. For behavior changes, exercise a realistic scenario and a counterexample, including a pending architecture decision. Review generated HTML and code consistency when relevant; static checks alone do not prove teaching quality or compliance.

Bump the version together in `package.json` and both plugin manifests when releasing. Validate both native marketplace installations in isolated configuration directories. Report which hosts were actually exercised. Never describe self-review as independent review.
