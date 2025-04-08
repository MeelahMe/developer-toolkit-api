from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_convert_timestamp_to_date():
    response = client.post("/tools/time/convert", json={"timestamp": 1609459200})  # Jan 1, 2021
    assert response.status_code == 200
    assert "date_string" in response.json()
    assert response.json()["date_string"].startswith("2021-01-01")

def test_convert_date_to_timestamp():
    response = client.post("/tools/time/convert", json={"date_string": "2021-01-01T00:00:00"})
    assert response.status_code == 200
    assert response.json()["timestamp"] == 1609459200

