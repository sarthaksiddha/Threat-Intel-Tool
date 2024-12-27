import aiohttp
from typing import Dict, List
from datetime import datetime

class ReputationManager:
    def __init__(self, config: Dict):
        self.reputation_sources = {
            'virustotal': self._check_virustotal,
            'abuseipdb': self._check_abuseipdb,
            'threatfox': self._check_threatfox
        }

    async def get_reputation(self, ioc: str, ioc_type: str) -> Dict:
        results = {}
        for source, checker in self.reputation_sources.items():
            try:
                results[source] = await checker(ioc, ioc_type)
            except Exception as e:
                results[source] = {'error': str(e)}
        
        return self._calculate_composite_score(results)

    async def _check_virustotal(self, ioc: str, ioc_type: str) -> Dict:
        async with aiohttp.ClientSession() as session:
            response = await session.get(
                f'https://www.virustotal.com/vtapi/v2/url/report',
                params={'apikey': self.vt_key, 'resource': ioc}
            )
            return await response.json()