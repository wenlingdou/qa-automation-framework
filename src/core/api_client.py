import requests
from src.core.config import BASE_URL

class APIClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "QA-Automation-Framework"
        })

    # ---------- Core HTTP Methods ----------

    def get(self, path: str, **kwargs):
        return self.session.get(f"{self.base_url}{path}", **kwargs)

    def post(self, path: str, json=None, **kwargs):
        return self.session.post(f"{self.base_url}{path}", json=json, **kwargs)

    def put(self, path: str, json=None, **kwargs):
        return self.session.put(f"{self.base_url}{path}", json=json, **kwargs)

    def delete(self, path: str, **kwargs):
        return self.session.delete(f"{self.base_url}{path}", **kwargs)

    # ---------- Auth Handling ----------

    def set_bearer_token(self, token: str):
        """Attach auth token after login"""
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })
