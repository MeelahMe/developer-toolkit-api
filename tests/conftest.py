import os
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.main import app

load_dotenv()


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture
def auth_headers():
    api_key = os.getenv("API_KEY")
    return {"X-API-Key": api_key}
