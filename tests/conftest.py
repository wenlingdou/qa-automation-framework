import pytest
from src.core.api_client import APIClient
from src.core.config import USER_EMAIL, USER_PASSWORD

@pytest.fixture(scope="session")
def api():
    return APIClient()

@pytest.fixture(scope="session")
def token(api):
    resp = api.post("/auth/signin", json={"email": USER_EMAIL, "password": USER_PASSWORD})
    resp.raise_for_status()
    body = resp.json()
    return body.get("token") or body.get("access_token")

@pytest.fixture(scope="session")
def authed_api(api, token):
    api.set_bearer_token(token)
    return api

# def authed_api(token):
#     client = APIClient()
#     client.set_bearer_token(token)
#     return client

@pytest.fixture(scope="session")
def robot_id(authed_api):
    resp = authed_api.get("/users/robots")
    resp.raise_for_status()

    robots = resp.json()
    assert robots, "No robot returned from /users/robots"

    first = robots[0]
    rid = first.get("id") or first.get("robot_id") or first.get("robotId")
    assert rid, f"Cannot find robot id in: {first}"
    return str(rid)



