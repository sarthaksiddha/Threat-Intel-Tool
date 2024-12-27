import yaml
from typing import Dict, List
from datetime import datetime

class PlaybookRunner:
    def __init__(self):
        self.playbooks = self._load_playbooks()
        self.action_handlers = {
            'collect_logs': self._collect_logs,
            'analyze_patterns': self._analyze_patterns,
            'network_analysis': self._network_analysis,
            'isolate_host': self._isolate_host,
            'notify_soc': self._notify_soc
        }

    def _load_playbooks(self) -> Dict:
        playbooks = {}
        for file in glob.glob('playbooks/*.yml'):
            with open(file) as f:
                playbook = yaml.safe_load(f)
                playbooks[playbook['name']] = playbook
        return playbooks

    async def run_playbook(self, name: str, context: Dict = None) -> Dict:
        if name not in self.playbooks:
            raise ValueError(f"Playbook {name} not found")
        
        playbook = self.playbooks[name]
        results = []
        
        for step in playbook['steps']:
            action = step['action']
            if action in self.action_handlers:
                result = await self.action_handlers[action](step['params'])
                results.append(result)
        
        return self._process_results(results, playbook['responses'])