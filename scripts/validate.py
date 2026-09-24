#!/usr/bin/env python3
"""Validate distribution metadata, self-contained skill resources, and shared contracts."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('learn-blueprint', 'learn-guide', 'learn-pair')
PLUGIN_SKILLS = {
    'learn-build': NAMES,
    'learn-build-vn': NAMES,
    'learn-oss-vn': ('learn-onboard', 'learn-catalogue', 'learn-recipe'),
}
PLUGINS = tuple(PLUGIN_SKILLS)
BUILD_PLUGINS = ('learn-build', 'learn-build-vn')
SHARED_FILES = ('learning-contract.md', 'html.md', 'project-memory.md', 'visual-explanation.md', 'recipe.css')


def validate():
    package = json.loads((ROOT / 'package.json').read_text(encoding='utf-8'))
    versions = {name: validate_plugin(ROOT / 'plugins' / name) for name in PLUGINS}
    assert versions['learn-build'] == versions['learn-build-vn'], 'Learn Build editions differ in version'
    for kind in ('.agents/plugins', '.claude-plugin'):
        market = json.loads((ROOT / kind / 'marketplace.json').read_text(encoding='utf-8'))
        assert market['name'] == 'learn-build-marketplace'
        assert [entry['name'] for entry in market['plugins']] == list(PLUGINS)
        for entry in market['plugins']:
            source = entry['source']
            assert (ROOT / (source['path'] if isinstance(source, dict) else source)).resolve() == (
                ROOT / 'plugins' / entry['name']).resolve()
    assert package['pi']['skills'] == ['./plugins/learn-build/skills']
    for name in PLUGINS:
        assert f'plugins/{name}' in package['files'], f'Plugin excluded from package: {name}'
    for name in NAMES:
        roots = [ROOT / 'plugins' / plugin / 'skills' / name for plugin in BUILD_PLUGINS]
        resources = [{p.relative_to(root) for p in root.rglob('*') if p.is_file()} for root in roots]
        assert resources[0] == resources[1], f'Localized resources differ: {name}'
    print('Distribution metadata and skill resources are valid.')


def validate_plugin(plugin):
    version = None
    for kind in ('.codex-plugin', '.claude-plugin'):
        manifest = json.loads((plugin / kind / 'plugin.json').read_text(encoding='utf-8'))
        assert manifest['name'] == plugin.name
        if version is None:
            version = manifest['version']
            assert re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:[-+][0-9A-Za-z.-]+)?', version), plugin
        assert manifest['version'] == version, f'Host manifest versions differ: {plugin}'
    shared = {}
    names = PLUGIN_SKILLS[plugin.name]
    assert {p.name for p in (plugin / 'skills').iterdir() if p.is_dir()} == set(names), plugin
    for name in names:
        skill = plugin / 'skills' / name
        if plugin.name == 'learn-oss-vn':
            required = ['agents/openai.yaml', 'assets/recipe.css'] + [
                f'references/{filename}' for filename in SHARED_FILES if filename.endswith('.md')]
            reference = {'learn-onboard': 'onboarding', 'learn-catalogue': 'catalogue', 'learn-recipe': 'recipe'}[name]
            required.append(f'references/{reference}.md')
            for relative in required:
                assert (skill / relative).is_file(), f'Missing skill resource: {skill / relative}'
        content = (skill / 'SKILL.md').read_text(encoding='utf-8')
        assert content.startswith('---\n')
        frontmatter = content.split('---', 2)[1]
        assert re.search(r'^name: ' + name + r'\s*$', frontmatter, re.M)
        assert re.search(r'^description: .+', frontmatter, re.M)
        for path in skill.rglob('*'):
            assert not path.is_symlink(), path
            if not path.is_file():
                continue
            if path.name in SHARED_FILES:
                old = shared.setdefault(path.name, path.read_bytes())
                assert old == path.read_bytes(), f'Shared contract differs: {path}'
            if path.suffix in ('.md', '.yaml', '.html', '.css'):
                text = path.read_text(encoding='utf-8')
                assert '/Users/linhvu/' not in text, path
                if plugin.name == 'learn-build':
                    assert not re.search(r'Vietnamese|tiếng Việt|tiếng Anh', text, re.I), path
                if path.suffix == '.md':
                    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                        if '://' in link or link.startswith('#'):
                            continue
                        target = (path.parent / link.split('#')[0]).resolve()
                        assert target.is_relative_to(skill.resolve()), f'External skill dependency: {path}: {link}'
                        assert target.exists(), f'Broken link: {path}: {link}'
    return version


if __name__ == '__main__':
    validate()
