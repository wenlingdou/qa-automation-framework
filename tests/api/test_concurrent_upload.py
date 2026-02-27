import concurrent.futures
import pytest
import time


def upload_once(api, robot_id, index):

    payload = {
        "timestamp": time.time(),
        "report_name": f"concurrent_test_{index}"
    }

    resp = api.post(
        f"/api/v2/users/robots/{robot_id}/weld_test_reports_upload",
        json=payload
    )

    print(f"Upload {index}: {resp.status_code}")

    return resp.status_code


@pytest.mark.load
def test_concurrent_upload(authed_api, robot_id):

    NUM_DEVICES = 20
    MAX_THREADS = 10

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:

        futures = [
            executor.submit(upload_once, authed_api, robot_id, i)
            for i in range(NUM_DEVICES)
        ]

        results = [f.result() for f in futures]

    print("Results:", results)

    assert all(status in (200, 201) for status in results)
    