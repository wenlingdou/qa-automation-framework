import pytest

@pytest.mark.api
def test_robot_detail_invalid_id_returns_400_or_404(authed_api):
    resp = authed_api.get("/users/robots/THIS_ID_SHOULD_NOT_EXIST_123")
    assert resp.status_code in (400,404), f"{resp.status_code} {resp.text[:200]}"

@pytest.mark.api
def test_unauthoized_without_token(api):
    # api = raw APIClient without bearer token
    resp = api.get("/users/robots")
    assert resp.status_code in (401,403), f"{resp.status_code} {resp.text[:200]}"  


    