"""RQNS Pipeline wrapper (port 9119)."""
from .base import ServiceBase

class RQNS(ServiceBase):
    def __init__(self, host="localhost", port=9119):
        self.base_url = f"http://{host}:{port}"

    def cycle(self) -> dict:
        """Run one LIF neuron + contextual bandit cycle."""
        return self._post("/cycle")

    def status(self) -> dict:
        return self._get("/health")
