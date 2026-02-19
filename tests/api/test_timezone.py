import pytest

@pytest.mark.api
def test_get_timezone(authed_api, robot_id):
    resp = authed_api.get(f"/users/robots/{robot_id}/timezone")

    assert resp.status_code==200, (
        f"URL: {resp.url}\n"
        f"Status: {resp.status_code}\n"
        f"Body: {resp.text[:500]}\n"
    )

    body = resp.json()
    assert isinstance(body, dict)

@pytest.mark.api
@pytest.mark.parametrize("tz", ["UTC", "America/Vancouver"])
def test_put_timezone(authed_api, robot_id, tz):
    payload = {"timezone": tz}

    resp = authed_api.put(f"/users/robots/{robot_id}/timezone", json=payload)

    assert resp.status_code in (200, 204), (
        f"URL: {resp.url}\n"
        f"Status: {resp.status_code}\n"
        f" Body: {resp.text[:500]}\n"
    )
    