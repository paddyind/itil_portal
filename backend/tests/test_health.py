import pytest
from django.conf import settings
from django.test import Client

@pytest.fixture
def client():
    return Client()

def test_health_check(client):
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
