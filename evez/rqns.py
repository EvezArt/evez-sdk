"""RQNS Pipeline wrapper (port 9119).

Endpoints
---------
POST /cycle  — run one LIF neuron + contextual bandit cycle
GET  /health — service health check
"""
from __future__ import annotations

from typing import Any, Dict

from .base import ServiceBase


class RQNS(ServiceBase):
    """Client for the EVEZ RQNS Pipeline."""

    def __init__(self, host: str = "localhost", port: int = 9119, **kwargs) -> None:
        super().__init__(host=host, port=port, **kwargs)

    def cycle(self) -> Dict[str, Any]:
        """Run one LIF neuron + contextual bandit cycle."""
        return self._post("/cycle")

    def status(self) -> Dict[str, Any]:
        """Get RQNS service status (alias for health)."""
        return self.health()
