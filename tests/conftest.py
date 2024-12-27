import pytest
from fastapi.testclient import TestClient
from api.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_threats():
    return [
        {"type": "malware", "value": "test.com", "confidence": 80},
        {"type": "phishing", "value": "evil.com", "confidence": 90}
    ]