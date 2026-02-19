import pytest

@pytest.mark.api
def test_get_robot_detail(authed_api, robot_id):
    resp = authed_api.get(f"/users/robots/{robot_id}")

    assert resp.status_code==200, (
        f"URL: {resp.url}\n"
        f"Status: {resp.status_code}\n"
        f"Body: {resp.text[:500]}\n"
    )

    body = resp.json()
    assert isinstance(body, dict)
