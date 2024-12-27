from typing import List, Dict
import requests
import pandas as pd
from datetime import datetime

class ThreatFeedCollector:
    def __init__(self):
        self.feeds = {
            'alienvault': 'https://otx.alienvault.com/api/v1/pulses/subscribed',
            'misp': 'https://your-misp-instance/events',
            'virustotal': 'https://www.virustotal.com/vtapi/v2/'
        }
        self.indicators = []

    async def collect_feeds(self) -> List[Dict]:
        """Collect threats from configured feeds"""
        for feed_name, feed_url in self.feeds.items():
            try:
                response = await self._fetch_feed(feed_url)
                self.indicators.extend(self._parse_indicators(response, feed_name))
            except Exception as e:
                print(f"Error collecting from {feed_name}: {e}")
        
        return self.indicators

    def _parse_indicators(self, data: Dict, source: str) -> List[Dict]:
        """Parse and normalize threat indicators"""
        parsed = []
        for item in data:
            indicator = {
                'type': item.get('type'),
                'value': item.get('indicator'),
                'source': source,
                'timestamp': datetime.now(),
                'confidence': item.get('confidence', 0),
                'tags': item.get('tags', [])
            }
            parsed.append(indicator)
        return parsed