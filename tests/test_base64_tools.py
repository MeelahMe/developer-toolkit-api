from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_encode_base64():
    """
    Test encoding a plain text string into Base64.
    """
    response = client.post("/tools/base64/encode", json={"content": "hello world"})
    assert response.status_code == 200
    assert response.json()["encoded"] == "aGVsbG8gd29ybGQ="

def test_decode_base64():
    """
    Test decoding a Base64 string back into plain text.
    """
    response = client.post("/tools/base64/decode", json={"encoded": "aGVsbG8gd29ybGQ="})
    assert response.status_code == 200
    assert response.json()["decoded"] == "hello world"
