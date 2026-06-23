"""DAW Agent wrapper (port 9112)."""
from .base import ServiceBase

class DAW(ServiceBase):
    def __init__(self, host="localhost", port=9112):
        self.base_url = f"http://{host}:{port}"

    def synthesize(self, bpm: int = 170, genre: str = "breakcore", duration: int = 8) -> bytes:
        """Synthesize audio. Returns raw WAV bytes."""
        import urllib.request
        data = json.dumps({"bpm": bpm, "genre": genre, "duration": duration}).encode()
        req = urllib.request.Request(f"{self.base_url}/synthesize", data=data,
                                     headers={"Content-Type": "application/json"})
        return urllib.request.urlopen(req, timeout=30).read()

    def status(self) -> dict:
        return self._get("/status")

import json
