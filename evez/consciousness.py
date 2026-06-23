"""Consciousness Engine wrapper (port 9111)."""
from .base import ServiceBase

class Consciousness(ServiceBase):
    def __init__(self, host="localhost", port=9111):
        self.base_url = f"http://{host}:{port}"

    def pipeline(self) -> dict:
        """Run one full SENSE→DESIRE→THINK→PLAN→ACT→LEARN→MODIFY→REFLECT→BECOME cycle."""
        return self._post("/pipeline")

    def emergence(self) -> dict:
        """Get emergence score and stage."""
        return self._get("/emergence")

    def dream(self, phase="Deep") -> dict:
        """Run a dream cycle (Deep or Light)."""
        return self._post("/dream", {"phase": phase})

    def status(self) -> dict:
        """Get consciousness status."""
        return self._get("/health")
