from fastapi.testclient import TestClient
from app.main import app
import string

client = TestClient(app)

def test_generate_password_default():
    """
    Test generating a password using default parameters.
    Should be 12 characters long.
    """
    response = client.get("/tools/password/generate")
    assert response.status_code == 200
    assert "password" in response.json()
    assert len(response.json()["password"]) == 12

def test_generate_password_custom_length():
    """
    Test that the password generator respects custom length.
    """
    response = client.get("/tools/password/generate?length=20")
    assert response.status_code == 200
    assert len(response.json()["password"]) == 20

def test_generate_password_without_symbols():
    """
    Test password generation excluding symbols.
    """
    response = client.get("/tools/password/generate?include_symbols=false")
    assert response.status_code == 200
    password = response.json()["password"]
    # Ensure no symbol characters present
    assert all(char in string.ascii_letters + string.digits for char in password)

def test_generate_password_with_all_sets_false():
    """
    Test that the API returns 400 when no character sets are selected.
    """
    response = client.get(
        "/tools/password/generate?include_symbols=false&include_numbers=false&include_uppercase=false&include_lowercase=false"
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "At least one character set must be selected."
ert response.json()["detail"] == "At least one character set must be selected."

