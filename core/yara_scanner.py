import yara
import os
from typing import List, Dict

class YaraScanner:
    def __init__(self, rules_dir: str = 'rules/yara_rules'):
        self.rules = self._compile_rules(rules_dir)

    def _compile_rules(self, rules_dir: str):
        rules_files = []
        for root, _, files in os.walk(rules_dir):
            for file in files:
                if file.endswith('.yar'):
                    rules_files.append(os.path.join(root, file))
        return yara.compile(filepaths={
            f'rule_{i}': path for i, path in enumerate(rules_files)
        })

    async def scan_file(self, file_path: str) -> List[Dict]:
        matches = self.rules.match(file_path)
        return [{
            'rule': match.rule,
            'strings': match.strings,
            'tags': match.tags,
            'meta': match.meta
        } for match in matches]