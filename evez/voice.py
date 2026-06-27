"""Machine Voice wrapper (port 9113).

Endpoints
---------
POST /transform — transform text through N-stage formant pipeline, returns raw WAV bytes
GET  /health    — service health check
"""
from __future__ import annotations

from typing import Any, Dict

from .base import ServiceBase


class Voice(ServiceBase):
    """Client for the EVEZ Machine Voice service."""

    def __init__(self, host: str = "localhost", port: int = 9113, **kwargs) -> None:
        super().__init__(host=host, port=port, **kwargs)

    def transform(self, text: str, stage: int = 5,
                  timeout: int = 30) -> bytes:
        """Transform text through N-stage formant pipeline. Returns raw WAV bytes.

        Args:
            text: Input text to vocalize.
            stage: Number of formant pipeline stages (1-8).
            timeout: Request timeout in seconds (default 30 for audio).

        Returns:
            Raw WAV audio bytes.
        """
        return self._request(
            "POST", "/transform",
            data={"text": text, "stage": stage},
            timeout=timeout, raw=True,
        )

    def status(self) -> Dict[str, Any]:
        """Get voice service status (alias for health)."""
        return self.health()
