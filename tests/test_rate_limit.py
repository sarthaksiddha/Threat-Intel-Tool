import pytest
from fastapi.testclient import TestClient
from api.main import app

def test_rate_limit(client):
    # Make 61 requests (exceed limit)
    for _ in range(61):
        response = client.get("/threats")
    
    assert response.status_code == 429
    assert response.json()["detail"] == "Too many requests"