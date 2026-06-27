"""DAW Agent wrapper (port 9112).

Endpoints
---------
POST /synthesize — synthesize audio from parameters, returns raw WAV bytes
GET  /status    — service health/status
GET  /health     — service health check
"""
from __future__ import annotations

from typing import Any, Dict

from .base import ServiceBase


class DAW(ServiceBase):
    """Client for the EVEZ DAW Agent."""

    def __init__(self, host: str = "localhost", port: int = 9112, **kwargs) -> None:
        super().__init__(host=host, port=port, **kwargs)

    def synthesize(self, bpm: int = 170, genre: str = "breakcore",
                   duration: int = 8, timeout: int = 30) -> bytes:
        """Synthesize audio. Returns raw WAV bytes.

        Args:
            bpm: Beats per minute.
            genre: Genre string (e.g. "breakcore", "ambient").
            duration: Duration in seconds.
            timeout: Request timeout in seconds (default 30 for audio).

        Returns:
            Raw WAV audio bytes.
        """
        return self._request(
            "POST", "/synthesize",
            data={"bpm": bpm, "genre": genre, "duration": duration},
            timeout=timeout, raw=True,
        )

    def status(self) -> Dict[str, Any]:
        """Get DAW agent status."""
        return self._get("/status")
