from fastapi.testclient import TestClient
from backend.main import app
import datetime

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200