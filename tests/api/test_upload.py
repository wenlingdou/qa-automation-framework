import pytest
import time


@pytest.mark.api
def test_upload_weld_report(authed_api, robot_id):

    payload = {
        "timestamp": time.time(),
        "test": "qa upload test"
    }

    resp = authed_api.post(
        f"/api/v2/users/robots/{robot_id}/weld_test_reports_upload",
        json=payload
    )

    print(resp.status_code)
    print(resp.text)

    assert resp.status_code in [200, 201]
    