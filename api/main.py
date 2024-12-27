from fastapi import FastAPI, HTTPException
from core.feed_collector import ThreatFeedCollector
from core.ai_analyzer import ThreatAnalyzer
from database.models import ThreatIndicator

app = FastAPI()
collector = ThreatFeedCollector()
analyzer = ThreatAnalyzer()

@app.get("/threats")
async def get_threats():
    """Get all threat indicators"""
    threats = await collector.collect_feeds()
    return {"threats": threats}

@app.get("/analyze/{threat_id}")
async def analyze_threat(threat_id: str):
    """Analyze specific threat with AI"""
    threat = await ThreatIndicator.get(threat_id)
    if not threat:
        raise HTTPException(404)
    analysis = analyzer.analyze_threat(threat)
    return analysis