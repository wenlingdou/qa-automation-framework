import pytest

@pytest.mark.api
@pytest.mark.parametrize("path", [
    "/users/robots/operation_hours",
    "/users/robots/performance/weld_hours",
    "/users/robots/performance/weld_inches",
])
def test_metrics_endpoints_return_json(authed_api, path):
    resp =authed_api.get(path)

    assert resp.status_code==200, (
        f"URL: {resp.url}\n"
        f"Status: {resp.status_code}\n"
        f"Body: {resp.text[:500]}\n"
    )
    assert "application/json" in resp.headers.get("Content-Type", "")
    _ = resp.json()
    