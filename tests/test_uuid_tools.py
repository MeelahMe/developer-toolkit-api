from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_uuid():
    """
    Test that the UUID endpoint returns a valid UUID string.
    """
    response = client.get("/tools/uuid/generate")
    assert response.status_code == 200
    uuid_str = response.json().get("uuid")
    assert isinstance(uuid_str, str)
    assert len(uuid_str) == 36  # UUID v4 is always 36 characters

