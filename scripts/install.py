#!/usr/bin/env python3
"""Install complete Learn Build skills without requiring an agent-specific plugin loader."""
import argparse
import filecmp
import os
from pathlib import Path
import shutil
import tempfile
from datetime import datetime, timezone

SKILLS = ('learn-blueprint', 'learn-guide', 'learn-pair')
SOURCE = Path(__file__).resolve().parents[1] / 'plugins' / 'learn-build' / 'skills'
SOURCES = {'en': SOURCE, 'vi': SOURCE.parent.parent / 'learn-build-vn' / 'skills'}
USER_DIRS = {'codex': '.codex/skills', 'claude': '.claude/skills', 'cursor': '.cursor/skills', 'pi': '.pi/agent/skills'}
PROJECT_DIRS = {**USER_DIRS, 'codex': '.agents/skills', 'pi': '.pi/skills'}


def identical(left, right):
    if not right.is_dir() or right.is_symlink():
        return False
    comparison = filecmp.dircmp(left, right)
    if comparison.left_only or comparison.right_only or comparison.funny_files or comparison.common_funny:
        return False
    if any(not filecmp.cmp(left / name, right / name, shallow=False) for name in comparison.common_files):
        return False
    return all(identical(left / name, right / name) for name in comparison.common_dirs)


def install(destination, force=False, dry_run=False, source_root=None):
    destination = Path(destination).expanduser().absolute()
    source_root = Path(source_root) if source_root is not None else SOURCE
    changed = []
    for name in SKILLS:
        source, target = source_root / name, destination / name
        if not (source / 'SKILL.md').is_file():
            raise ValueError(f'Missing source skill: {source}')
        if target.is_symlink():
            raise ValueError(f'Refusing to replace a symbolic link: {target}')
        if identical(source, target):
            print(f'Unchanged: {target}')
            continue
        if target.exists() and not force:
            raise ValueError(f'Existing skill differs: {target}. Use --force to back it up and replace it.')
        changed.append((source, target))
    if dry_run:
        for _, target in changed:
            print(f'Would install: {target}')
        return
    if not changed:
        return
    destination.mkdir(parents=True, exist_ok=True)
    backup = destination.parent / '.learn-build-backups' / destination.name / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    for source, target in changed:
        stage = Path(tempfile.mkdtemp(prefix='.learn-build-stage-', dir=destination))
        saved = None
        try:
            shutil.copytree(source, stage / target.name)
            if target.exists():
                backup.mkdir(parents=True, exist_ok=True)
                saved = backup / target.name
                target.rename(saved)
            try:
                (stage / target.name).rename(target)
            except OSError:
                if saved is not None:
                    saved.rename(target)
                raise
            print(f'Installed: {target}')
            if saved is not None:
                print(f'Previous version: {saved}')
        finally:
            shutil.rmtree(stage)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument('--agent', choices=USER_DIRS)
    target.add_argument('--dest', type=Path, help='Custom skills directory for another compatible agent')
    parser.add_argument('--scope', choices=('user', 'project'), default='user')
    parser.add_argument('--project-root', type=Path)
    parser.add_argument('--language', choices=SOURCES, default='en',
                        help='Skill language: en (learn-build, default) or vi (learn-build-vn)')
    parser.add_argument('--force', action='store_true', help='Back up differing existing skills before replacement')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if args.dest and (args.scope != 'user' or args.project_root):
        parser.error('--dest cannot be combined with --scope project or --project-root')
    if args.project_root and args.scope != 'project':
        parser.error('--project-root requires --scope project')
    if args.dest:
        destination = args.dest
    elif args.scope == 'project':
        destination = (args.project_root or Path.cwd()) / PROJECT_DIRS[args.agent]
    elif args.agent == 'codex' and os.environ.get('CODEX_HOME'):
        destination = Path(os.environ['CODEX_HOME']) / 'skills'
    else:
        destination = Path.home() / USER_DIRS[args.agent]
    try:
        install(destination, args.force, args.dry_run, source_root=SOURCES[args.language])
    except (ValueError, OSError) as error:
        parser.exit(1, f'{error}\n')


if __name__ == '__main__':
    main()
