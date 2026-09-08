import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'source'
        for name in installer.SKILLS:
            skill = self.source / name
            (skill / 'references').mkdir(parents=True)
            (skill / 'SKILL.md').write_text(f'---\nname: {name}\n---\n')
            (skill / 'references/contract.md').write_text('Shared contract')
        self.patch = patch.object(installer, 'SOURCE', self.source)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.dest = self.root / 'path with spaces' / 'skills'

    def install(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(self.dest, **kwargs)

    def test_installs_complete_tree_and_repeated_install_is_unchanged(self):
        self.install()
        first = (self.dest / 'learn-guide/SKILL.md').stat().st_mtime_ns
        self.install()
        self.assertEqual(first, (self.dest / 'learn-guide/SKILL.md').stat().st_mtime_ns)
        self.assertEqual('Shared contract', (self.dest / 'learn-pair/references/contract.md').read_text())
        self.assertFalse((self.dest.parent / '.learn-build-backups').exists())

    def test_file_directory_mismatch_is_not_unchanged(self):
        self.install()
        target = self.dest / 'learn-guide/SKILL.md'
        target.unlink()
        target.mkdir()
        with self.assertRaises(ValueError):
            self.install()
        self.install(force=True)
        self.assertTrue(target.is_file())
        saved = list((self.dest.parent / '.learn-build-backups').rglob('learn-guide/SKILL.md'))
        self.assertEqual(1, len(saved))
        self.assertTrue(saved[0].is_dir())

    def test_dry_run_has_no_filesystem_effect(self):
        self.install(dry_run=True)
        self.assertFalse(self.dest.parent.exists())

    def test_conflict_preflight_prevents_partial_install(self):
        conflict = self.dest / 'learn-pair'
        conflict.mkdir(parents=True)
        (conflict / 'SKILL.md').write_text('User content')
        with self.assertRaises(ValueError):
            self.install()
        self.assertFalse((self.dest / 'learn-blueprint').exists())
        self.assertEqual('User content', (conflict / 'SKILL.md').read_text())

    def test_force_preserves_old_content_outside_discovery_tree(self):
        self.install()
        target = self.dest / 'learn-guide/SKILL.md'
        target.write_text('User content')
        self.install(force=True)
        saved = list((self.dest.parent / '.learn-build-backups').rglob('learn-guide/SKILL.md'))
        self.assertEqual(1, len(saved))
        self.assertEqual('User content', saved[0].read_text())
        self.assertFalse(saved[0].is_relative_to(self.dest))
        self.assertEqual((self.source / 'learn-guide/SKILL.md').read_text(), target.read_text())

    def test_symlink_target_is_rejected(self):
        self.dest.mkdir(parents=True)
        try:
            (self.dest / 'learn-guide').symlink_to(self.source / 'learn-guide', target_is_directory=True)
        except OSError:
            self.skipTest('Symlinks unavailable on this platform')
        with self.assertRaises(ValueError):
            self.install(force=True)

    def test_missing_source_prevents_partial_install(self):
        (self.source / 'learn-pair/SKILL.md').unlink()
        with self.assertRaises(ValueError):
            self.install()
        self.assertFalse(self.dest.exists())

    def test_cli_project_scope(self):
        for agent, folder in installer.PROJECT_DIRS.items():
            project = self.root / agent
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--agent', agent,
                                     '--scope', 'project', '--project-root', str(project)], capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stderr)
            for name in installer.SKILLS:
                self.assertTrue((project / folder / name / 'SKILL.md').is_file())

    def test_invalid_cli_scope_is_rejected(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--dest', str(self.dest),
                                 '--scope', 'project'], capture_output=True, text=True)
        self.assertNotEqual(0, result.returncode)
        self.assertFalse(self.dest.exists())


if __name__ == '__main__':
    unittest.main()
