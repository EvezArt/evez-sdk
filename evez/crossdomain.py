"""Cross-Domain Engine wrapper (port 9114)."""
from .base import ServiceBase

class CrossDomain(ServiceBase):
    def __init__(self, host="localhost", port=9114):
        self.base_url = f"http://{host}:{port}"

    def ooda(self) -> dict:
        """Run one Observe-Orient-Decide-Act cycle."""
        return self._post("/ooda")

    def status(self) -> dict:
        return self._get("/health")
