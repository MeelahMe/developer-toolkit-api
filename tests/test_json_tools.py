from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prettify_valid_json():
    """
    Test that valid compact JSON is successfully prettified.
    """
    response = client.post("/tools/json/prettify", json={"content": '{"key":"value"}'})
    assert response.status_code == 200
    assert response.json()["prettified"].startswith("{\n")

def test_prettify_invalid_json():
    """
    Test that invalid JSON input returns a 400 error with appropriate detail.
    """
    response = client.post("/tools/json/prettify", json={"content": "{name: Jameelah"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid JSON string."


