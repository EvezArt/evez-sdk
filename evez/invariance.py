"""Invariance Battery wrapper (port 9115).

Endpoints
---------
POST /audit  — run full invariance audit, test all declared invariants
GET  /health — service health check
"""
from __future__ import annotations

from typing import Any, Dict

from .base import ServiceBase


class Invariance(ServiceBase):
    """Client for the EVEZ Invariance Battery."""

    def __init__(self, host: str = "localhost", port: int = 9115, **kwargs) -> None:
        super().__init__(host=host, port=port, **kwargs)

    def audit(self) -> Dict[str, Any]:
        """Run full invariance audit — test all declared invariants."""
        return self._post("/audit")

    def status(self) -> Dict[str, Any]:
        """Get invariance service status (alias for health)."""
        return self.health()
