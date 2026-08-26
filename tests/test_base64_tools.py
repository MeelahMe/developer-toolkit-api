def test_encode_base64(client, auth_headers):
    """
    Test encoding a plain text string into Base64.
    """
    response = client.post(
        "/tools/base64/encode",
        json={"content": "hello world"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["encoded"] == "aGVsbG8gd29ybGQ="


def test_decode_base64(client, auth_headers):
    """
    Test decoding a Base64 string back into plain text.
    """
    response = client.post(
        "/tools/base64/decode",
        json={"encoded": "aGVsbG8gd29ybGQ="},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["decoded"] == "hello world"
