import pytest

@pytest.mark.api
def test_get_users_robots(authed_api):
    resp = authed_api.get("/users/robots")
    assert resp.status_code == 200, (
        f"URL: {resp.url}\n"
        f"Status: {resp.status_code}\n"
        f"Body: {resp.text[:500]}\n"
    )
    assert "application/json" in resp.headers.get("Content-Type", "")
