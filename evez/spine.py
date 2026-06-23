"""Event Spine wrapper (port 9116)."""
from .base import ServiceBase

class Spine(ServiceBase):
    def __init__(self, host="localhost", port=9116):
        self.base_url = f"http://{host}:{port}"

    def verify(self) -> dict:
        """Verify entire chain integrity."""
        return self._get("/verify")

    def append(self, domain: str, action: str, data: dict = None) -> dict:
        """Append an event. Append-only — no deletes."""
        return self._post("/append", {"domain": domain, "action": action, "data": data or {}})

    def stats(self) -> dict:
        """Get spine statistics."""
        return self._get("/stats")

    def query(self, domain: str = None, limit: int = 20) -> dict:
        """Query recent events, optionally filtered by domain."""
        params = f"/query?limit={limit}"
        if domain:
            params += f"&domain={domain}"
        return self._get(params)
