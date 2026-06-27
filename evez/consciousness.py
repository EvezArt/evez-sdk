"""Consciousness Engine wrapper (port 9111).

Endpoints
---------
POST /pipeline   — run one full SENSE→DESIRE→THINK→PLAN→ACT→LEARN→MODIFY→REFLECT→BECOME cycle
GET  /emergence  — get emergence score and stage
POST /dream      — run a dream cycle (Deep or Light)
GET  /health     — service health check
"""
from __future__ import annotations

from typing import Any, Dict

from .base import ServiceBase


class Consciousness(ServiceBase):
    """Client for the EVEZ Consciousness Engine."""

    def __init__(self, host: str = "localhost", port: int = 9111, **kwargs) -> None:
        super().__init__(host=host, port=port, **kwargs)

    def pipeline(self) -> Dict[str, Any]:
        """Run one full consciousness cycle (SENSE → BECOME)."""
        return self._post("/pipeline")

    def emergence(self) -> Dict[str, Any]:
        """Get emergence score and stage."""
        return self._get("/emergence")

    def dream(self, phase: str = "Deep") -> Dict[str, Any]:
        """Run a dream cycle.

        Args:
            phase: "Deep" or "Light".
        """
        return self._post("/dream", {"phase": phase})

    def status(self) -> Dict[str, Any]:
        """Get consciousness status (alias for health)."""
        return self.health()
