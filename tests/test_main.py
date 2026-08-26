def test_metrics_endpoint(client):
    """
    Test that the /metrics endpoint returns Prometheus-formatted metrics
    without requiring authentication.
    """
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text


def test_root_endpoint(client):
    """
    Test that the root endpoint is accessible without authentication.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the Developer Toolkit API!"


def test_usage_requires_api_key(client):
    """
    Test that /usage rejects requests without a valid API key.
    """
    response = client.get("/usage")
    assert response.status_code == 401


def test_usage_returns_logged_requests(client, auth_headers):
    """
    Test that /usage returns request history when authenticated.
    """
    # Generate at least one logged request first
    client.get("/", headers=auth_headers)
    response = client.get("/usage", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
