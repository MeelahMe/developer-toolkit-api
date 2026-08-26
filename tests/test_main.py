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
