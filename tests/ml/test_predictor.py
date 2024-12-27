import pytest
import numpy as np
from core.ml_predictor import ThreatPredictor

@pytest.fixture
def predictor():
    return ThreatPredictor()

@pytest.fixture
def sample_data():
    return [
        {
            'severity': 0.8,
            'frequency': 10,
            'source_reputation': 0.6,
            'target_criticality': 0.9,
            'campaign_duration': 48
        }
    ] * 100

def test_prediction_shape(predictor, sample_data):
    predictions = await predictor.predict_threats(sample_data)
    assert 'next_24h' in predictions
    assert 'next_week' in predictions
    assert len(predictions['next_24h']) == len(sample_data)

def test_emerging_threats(predictor, sample_data):
    predictions = await predictor.predict_threats(sample_data)
    assert isinstance(predictions['emerging_threats'], list)
    for threat in predictions['emerging_threats']:
        assert threat['growth_rate'] > 1.5

def test_model_persistence(predictor, sample_data):
    predictor.save_model('model.pkl')
    new_predictor = ThreatPredictor.load_model('model.pkl')
    
    pred1 = await predictor.predict_threats(sample_data)
    pred2 = await new_predictor.predict_threats(sample_data)
    
    np.testing.assert_array_almost_equal(pred1['next_24h'], pred2['next_24h'])