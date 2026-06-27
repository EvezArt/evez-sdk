"""Cross-Domain Engine wrapper (port 9114).

Endpoints
---------
POST /ooda   — run one Observe-Orient-Decide-Act cycle
GET  /health — service health check
"""
from __future__ import annotations

from typing import Any, Dict

from .base import ServiceBase


class CrossDomain(ServiceBase):
    """Client for the EVEZ Cross-Domain Engine."""

    def __init__(self, host: str = "localhost", port: int = 9114, **kwargs) -> None:
        super().__init__(host=host, port=port, **kwargs)

    def ooda(self) -> Dict[str, Any]:
        """Run one Observe-Orient-Decide-Act cycle."""
        return self._post("/ooda")

    def status(self) -> Dict[str, Any]:
        """Get cross-domain service status (alias for health)."""
        return self.health()
