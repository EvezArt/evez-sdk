"""Shared HTTP helpers for the EVEZ SDK."""
import json
from urllib.request import urlopen, Request
from urllib.error import URLError

class ServiceBase:
    """Base class for EVEZ service wrappers."""
    base_url: str = ""

    def _get(self, path: str, timeout: int = 5) -> dict:
        try:
            resp = urlopen(f"{self.base_url}{path}", timeout=timeout)
            return json.loads(resp.read())
        except Exception as e:
            return {"error": str(e)}

    def _post(self, path: str, data: dict = None, timeout: int = 10) -> dict:
        try:
            body = json.dumps(data or {}).encode()
            req = Request(f"{self.base_url}{path}", data=body,
                          headers={"Content-Type": "application/json"})
            return json.loads(urlopen(req, timeout=timeout).read())
        except Exception as e:
            return {"error": str(e)}

    def health(self) -> dict:
        return self._get("/health")
