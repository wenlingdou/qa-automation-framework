import pytest

@pytest.mark.api
def test_signin_invalid_credentials(api):
    payload = {
        "email": "fake@novarctech.com",
        "password": "wrongpassword"
    }

    resp = api.post("/auth/signin", json=payload)

    # real API behavior check
    assert resp.status_code in (400, 401)

    assert "application/json" in resp.headers.get("Content-Type", "")

    body = resp.json()
   
    assert "message" in body or "error" in body
    

    