import pytest

@pytest.mark.api
def test_get_robot_list_authorized(authed_api):
    resp = authed_api.get("/robot")

    assert resp.status_code == 200, (
        f"URL: {resp.url}\n"
        f"Status: {resp.status_code}\n"
        f"Content-Type: {resp.headers.get('Content-Type')}\n"
        f"Body: {resp.text[:500]}\n"
    )

