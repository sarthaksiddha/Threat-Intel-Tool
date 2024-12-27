import pytest
from core.feed_collector import ThreatFeedCollector

@pytest.fixture
def collector():
    return ThreatFeedCollector()

def test_collect_feeds(collector):
    indicators = await collector.collect_feeds()
    assert isinstance(indicators, list)
    assert len(indicators) > 0
    assert all(isinstance(i, dict) for i in indicators)

def test_parse_indicators(collector):
    mock_data = [{
        'type': 'malware',
        'indicator': 'test.com',
        'confidence': 80,
        'tags': ['malicious']
    }]
    parsed = collector._parse_indicators(mock_data, 'test')
    assert parsed[0]['source'] == 'test'
    assert parsed[0]['type'] == 'malware'