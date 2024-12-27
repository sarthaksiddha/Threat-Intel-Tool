import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from typing import List, Dict

class ThreatPredictor:
    def __init__(self):
        self.model = GradientBoostingRegressor()
        self.scaler = StandardScaler()
        self.feature_columns = [
            'severity', 'frequency', 'source_reputation',
            'target_criticality', 'campaign_duration'
        ]

    async def predict_threats(self, historical_data: List[Dict]) -> Dict:
        df = pd.DataFrame(historical_data)
        X = self.scaler.fit_transform(df[self.feature_columns])
        
        predictions = {
            'next_24h': self._predict_window(X, window=24),
            'next_week': self._predict_window(X, window=168),
            'emerging_threats': self._identify_emerging_threats(X, df)
        }
        return predictions

    def _predict_window(self, X, window: int):
        return self.model.predict(X)

    def _identify_emerging_threats(self, X, df):
        trend_analysis = self._analyze_trends(df)
        return [threat for threat in trend_analysis if threat['growth_rate'] > 1.5]