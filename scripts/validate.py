#!/usr/bin/env python3
"""Validate distribution metadata, self-contained skill resources, and shared contracts."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('learn-blueprint', 'learn-guide', 'learn-pair')


def validate():
    plugin = ROOT / 'plugins/learn-build'
    package = json.loads((ROOT / 'package.json').read_text(encoding='utf-8'))
    for kind in ('.codex-plugin', '.claude-plugin'):
        manifest = json.loads((plugin / kind / 'plugin.json').read_text(encoding='utf-8'))
        assert manifest['name'] == 'learn-build'
        assert manifest['version'] == package['version']
    for kind in ('.agents/plugins', '.claude-plugin'):
        market = json.loads((ROOT / kind / 'marketplace.json').read_text(encoding='utf-8'))
        assert market['name'] == 'learn-build-marketplace'
        assert len(market['plugins']) == 1
        entry = market['plugins'][0]
        assert entry['name'] == 'learn-build'
        source = entry['source']
        assert (ROOT / (source['path'] if isinstance(source, dict) else source)).resolve() == plugin.resolve()
    assert package['pi']['skills'] == ['./plugins/learn-build/skills']
    shared = {}
    for name in NAMES:
        skill = plugin / 'skills' / name
        content = (skill / 'SKILL.md').read_text(encoding='utf-8')
        assert content.startswith('---\n')
        frontmatter = content.split('---', 2)[1]
        assert re.search(r'^name: ' + name + r'\s*$', frontmatter, re.M)
        assert re.search(r'^description: .+', frontmatter, re.M)
        for path in skill.rglob('*'):
            assert not path.is_symlink(), path
            if not path.is_file():
                continue
            if path.name in ('learning-contract.md', 'html.md', 'project-memory.md'):
                old = shared.setdefault(path.name, path.read_bytes())
                assert old == path.read_bytes(), f'Shared contract differs: {path}'
            if path.suffix in ('.md', '.yaml', '.html', '.css'):
                text = path.read_text(encoding='utf-8')
                assert '/Users/linhvu/' not in text, path
                assert not re.search(r'Vietnamese|tiếng Việt|tiếng Anh', text, re.I), path
                if path.suffix == '.md':
                    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                        if '://' in link or link.startswith('#'):
                            continue
                        target = (path.parent / link.split('#')[0]).resolve()
                        assert target.is_relative_to(skill.resolve()), f'External skill dependency: {path}: {link}'
                        assert target.exists(), f'Broken link: {path}: {link}'
    print('Distribution metadata and skill resources are valid.')


if __name__ == '__main__':
    validate()
