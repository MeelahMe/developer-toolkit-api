from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prettify_valid_json():
    response = client.post(
        "/tools/json/prettify",
        json={"content": "{\"name\":\"Jameelah\"}"}
    )
    assert response.status_code == 200
    assert "prettified" in response.json()
    assert "Jameelah" in response.json()["prettified"]

def test_prettify_invalid_json():
    response = client.post(
        "/tools/json/prettify",
        json={"content": "{name: Jameelah"}  # Invalid JSON
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid JSON input."

