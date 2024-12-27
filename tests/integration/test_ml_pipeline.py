import pytest
from core.ml_predictor import ThreatPredictor
from core.threat_hunter import ThreatHunter

@pytest.fixture
async def setup_pipeline():
    predictor = ThreatPredictor()
    hunter = ThreatHunter()
    return predictor, hunter

@pytest.mark.asyncio
async def test_prediction_hunting_pipeline(setup_pipeline):
    predictor, hunter = setup_pipeline
    
    # Test prediction flow
    predictions = await predictor.predict_threats(sample_data)
    assert predictions is not None
    
    # Use predictions in hunting
    for threat in predictions['emerging_threats']:
        hunt_results = await hunter.run_hunt('lateral_movement')
        assert hunt_results is not None
        assert 'findings' in hunt_results