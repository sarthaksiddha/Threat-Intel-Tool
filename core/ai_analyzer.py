from transformers import pipeline
import numpy as np
from typing import Dict, List

class ThreatAnalyzer:
    def __init__(self):
        self.classifier = pipeline("text-classification")
        self.similarity_model = pipeline("sentence-similarity")
        
    def analyze_threat(self, indicator: Dict) -> Dict:
        """Analyze threat indicators using AI models"""
        analysis = {
            'severity': self._calculate_severity(indicator),
            'related_threats': self._find_related_threats(indicator),
            'recommendations': self._generate_recommendations(indicator)
        }
        return {**indicator, **analysis}
    
    def _calculate_severity(self, indicator: Dict) -> float:
        """Calculate threat severity score using ML"""
        features = self._extract_features(indicator)
        severity_score = self.classifier(features)[0]['score']
        return float(severity_score)