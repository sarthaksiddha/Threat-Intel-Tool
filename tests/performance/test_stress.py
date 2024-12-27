import pytest
from concurrent.futures import ThreadPoolExecutor
from core.ml_predictor import ThreatPredictor
from core.threat_hunter import ThreatHunter

@pytest.mark.asyncio
async def test_concurrent_predictions():
    predictor = ThreatPredictor()
    max_workers = 10
    num_requests = 100
    
    async with ThreadPoolExecutor(max_workers=max_workers) as executor:
        tasks = [predictor.predict_threats(sample_data) for _ in range(num_requests)]
        results = await asyncio.gather(*tasks)
        
        assert len(results) == num_requests
        assert all(r is not None for r in results)

@pytest.mark.asyncio
async def test_system_under_load():
    predictor = ThreatPredictor()
    hunter = ThreatHunter()
    
    async def process_threat():
        pred = await predictor.predict_threats(sample_data)
        hunt = await hunter.run_hunt('lateral_movement')
        return pred, hunt
    
    num_concurrent = 50
    tasks = [process_threat() for _ in range(num_concurrent)]
    results = await asyncio.gather(*tasks)
    
    assert len(results) == num_concurrent