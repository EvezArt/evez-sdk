"""Invariance Battery wrapper (port 9115)."""
from .base import ServiceBase

class Invariance(ServiceBase):
    def __init__(self, host="localhost", port=9115):
        self.base_url = f"http://{host}:{port}"

    def audit(self) -> dict:
        """Run full invariance audit — test all declared invariants."""
        return self._post("/audit")

    def status(self) -> dict:
        return self._get("/health")
