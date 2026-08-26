def test_convert_timestamp_to_date(client, auth_headers):
    """
    Test converting a UNIX timestamp to an ISO 8601 UTC date string.
    """
    response = client.post(
        "/tools/time/convert",
        json={"timestamp": 1609459200},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["date_string"].startswith("2021-01-01")


def test_convert_date_to_timestamp(client, auth_headers):
    """
    Test converting an ISO 8601 date string to a UNIX timestamp.
    """
    response = client.post(
        "/tools/time/convert",
        json={"date_string": "2021-01-01T00:00:00"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["timestamp"] == 1609459200
