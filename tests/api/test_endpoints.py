import pytest
from fastapi.testclient import TestClient
from api.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer test-token"}

def test_get_threats(client, auth_headers):
    response = client.get("/threats", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert all(isinstance(t, dict) for t in data)

def test_analyze_threat(client, auth_headers):
    threat_id = "test-threat-id"
    response = client.get(f"/analyze/{threat_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert "severity" in data
    assert "analysis" in data

def test_invalid_threat(client, auth_headers):
    response = client.get("/analyze/invalid-id", headers=auth_headers)
    assert response.status_code == 404

def test_unauthorized_access(client):
    response = client.get("/threats")
    assert response.status_code == 401