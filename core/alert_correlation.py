from typing import List, Dict
from datetime import datetime, timedelta
from collections import defaultdict
import networkx as nx

class AlertCorrelator:
    def __init__(self):
        self.correlation_window = timedelta(hours=1)
        self.graph = nx.DiGraph()

    async def correlate_alerts(self, alerts: List[Dict]) -> List[Dict]:
        alert_groups = self._group_by_time(alerts)
        correlated = []

        for timeframe, group in alert_groups.items():
            chain = self._build_attack_chain(group)
            related = self._find_related_events(chain)
            correlated.append({
                'timeframe': timeframe,
                'attack_chain': chain,
                'related_events': related,
                'risk_score': self._calculate_risk_score(chain)
            })
        return correlated

    def _build_attack_chain(self, alerts: List[Dict]) -> nx.DiGraph:
        chain = nx.DiGraph()
        for alert in alerts:
            self._add_alert_to_chain(chain, alert)
        return chain