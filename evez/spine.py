"""Event Spine wrapper (port 9116).

Endpoints
---------
GET  /verify  — verify entire chain integrity
POST /append  — append an event (append-only, no deletes)
GET  /stats   — get spine statistics
GET  /query   — query recent events, optionally filtered by domain
GET  /health  — service health check
"""
from __future__ import annotations

from typing import Any, Dict, Optional

from .base import ServiceBase


class Spine(ServiceBase):
    """Client for the EVEZ Event Spine."""

    def __init__(self, host: str = "localhost", port: int = 9116, **kwargs) -> None:
        super().__init__(host=host, port=port, **kwargs)

    def verify(self) -> Dict[str, Any]:
        """Verify entire chain integrity."""
        return self._get("/verify")

    def append(self, domain: str, action: str,
               data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Append an event. Append-only — no deletes.

        Args:
            domain: Domain label (e.g. "consciousness", "audio").
            action: Action identifier.
            data: Optional payload dictionary.
        """
        return self._post("/append", {"domain": domain, "action": action,
                                      "data": data or {}})

    def stats(self) -> Dict[str, Any]:
        """Get spine statistics."""
        return self._get("/stats")

    def query(self, domain: Optional[str] = None,
              limit: int = 20) -> Dict[str, Any]:
        """Query recent events, optionally filtered by domain.

        Args:
            domain: Filter by domain (None for all).
            limit: Maximum number of events to return.
        """
        path = f"/query?limit={limit}"
        if domain:
            path += f"&domain={domain}"
        return self._get(path)
