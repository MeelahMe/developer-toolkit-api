from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_convert_timestamp_to_date():
    """
    Test converting a UNIX timestamp to an ISO 8601 UTC date string.
    """
    response = client.post("/tools/time/convert", json={"timestamp": 1609459200})
    assert response.status_code == 200
    assert response.json()["date_string"].startswith("2021-01-01")

def test_convert_date_to_timestamp():
    """
    Test converting an ISO 8601 date string to a UNIX timestamp.
    """
    response = client.post("/tools/time/convert", json={"date_string": "2021-01-01T00:00:00"})
    assert response.status_code == 200
    assert response.json()["timestamp"] == 1609459200


