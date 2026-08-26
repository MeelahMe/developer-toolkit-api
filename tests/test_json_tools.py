def test_prettify_valid_json(client, auth_headers):
    """
    Test that valid compact JSON is successfully prettified.
    """
    response = client.post(
        "/tools/json/prettify",
        json={"content": '{"key":"value"}'},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["prettified"].startswith("{\n")


def test_prettify_invalid_json(client, auth_headers):
    """
    Test that invalid JSON input returns a 400 error with appropriate detail.
    """
    response = client.post(
        "/tools/json/prettify",
        json={"content": "{name: Jameelah"},
        headers=auth_headers,
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid JSON string."
