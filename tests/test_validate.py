import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ('plugins', '.agents', '.claude-plugin'):
            shutil.copytree(ROOT / directory, self.root / directory)
        shutil.copy2(ROOT / 'package.json', self.root / 'package.json')
        override = patch.object(validator, 'ROOT', self.root)
        override.start()
        self.addCleanup(override.stop)

    def validate(self):
        with contextlib.redirect_stdout(io.StringIO()):
            validator.validate()

    def test_both_editions_are_valid(self):
        self.validate()

    def test_missing_localized_asset_is_rejected(self):
        (self.root / 'plugins/learn-build-vn/skills/learn-guide/assets/learn.css').unlink()
        with self.assertRaises(AssertionError):
            self.validate()

    def test_stale_localized_version_is_rejected(self):
        manifest = self.root / 'plugins/learn-build-vn/.claude-plugin/plugin.json'
        data = json.loads(manifest.read_text(encoding='utf-8'))
        data['version'] = '0.0.1'
        manifest.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaises(AssertionError):
            self.validate()

    def test_localized_contract_drift_is_rejected(self):
        contract = self.root / 'plugins/learn-build-vn/skills/learn-guide/references/learning-contract.md'
        contract.write_text(contract.read_text(encoding='utf-8') + '\nUnexpected divergence\n',
                            encoding='utf-8')
        with self.assertRaises(AssertionError):
            self.validate()

    def test_oss_version_can_change_independently_of_build_and_package(self):
        for kind in ('.codex-plugin', '.claude-plugin'):
            manifest = self.root / 'plugins/learn-oss-vn' / kind / 'plugin.json'
            data = json.loads(manifest.read_text(encoding='utf-8'))
            data['version'] = '1.2.3'
            manifest.write_text(json.dumps(data), encoding='utf-8')
        self.validate()

    def test_missing_oss_marketplace_entry_is_rejected(self):
        manifest = self.root / '.agents/plugins/marketplace.json'
        data = json.loads(manifest.read_text(encoding='utf-8'))
        data['plugins'] = [entry for entry in data['plugins'] if entry['name'] != 'learn-oss-vn']
        manifest.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaises(AssertionError):
            self.validate()

    def test_oss_host_version_mismatch_is_rejected(self):
        manifest = self.root / 'plugins/learn-oss-vn/.claude-plugin/plugin.json'
        data = json.loads(manifest.read_text(encoding='utf-8'))
        data['version'] = '9.0.0'
        manifest.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaises(AssertionError):
            self.validate()

    def test_oss_missing_visual_reference_is_rejected(self):
        (self.root / 'plugins/learn-oss-vn/skills/learn-recipe/references/visual-explanation.md').unlink()
        with self.assertRaises(AssertionError):
            self.validate()

    def test_oss_shared_contract_drift_is_rejected(self):
        path = self.root / 'plugins/learn-oss-vn/skills/learn-recipe/references/learning-contract.md'
        path.write_text(path.read_text(encoding='utf-8') + '\nUnexpected divergence\n', encoding='utf-8')
        with self.assertRaises(AssertionError):
            self.validate()

    def test_oss_broken_local_link_is_rejected(self):
        path = self.root / 'plugins/learn-oss-vn/skills/learn-recipe/references/recipe.md'
        path.write_text(path.read_text(encoding='utf-8') + '\n[Missing](missing.md)\n', encoding='utf-8')
        with self.assertRaises(AssertionError):
            self.validate()


if __name__ == '__main__':
    unittest.main()
