from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_password_default():
    response = client.get("/tools/password/generate")
    assert response.status_code == 200
    data = response.json()
    assert "password" in data
    assert len(data["password"]) == 12  # Default length

def test_generate_password_custom_length():
    response = client.get("/tools/password/generate?length=20")
    assert response.status_code == 200
    assert len(response.json()["password"]) == 20

def test_generate_password_without_symbols():
    response = client.get("/tools/password/generate?include_symbols=false")
    assert response.status_code == 200
    password = response.json()["password"]
    assert all(char.isalnum() or char in string.ascii_letters + string.digits for char in password)

def test_generate_password_with_all_sets_false():
    response = client.get(
        "/tools/password/generate?include_symbols=false&include_numbers=false&include_uppercase=false&include_lowercase=false"
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "At least one character set must be selected."

