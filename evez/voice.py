"""Machine Voice wrapper (port 9113)."""
from .base import ServiceBase
import json as _json
import urllib.request

class Voice(ServiceBase):
    def __init__(self, host="localhost", port=9113):
        self.base_url = f"http://{host}:{port}"

    def transform(self, text: str, stage: int = 5) -> bytes:
        """Transform text through N-stage formant pipeline. Returns raw WAV bytes."""
        data = _json.dumps({"text": text, "stage": stage}).encode()
        req = urllib.request.Request(f"{self.base_url}/transform", data=data,
                                     headers={"Content-Type": "application/json"})
        return urllib.request.urlopen(req, timeout=30).read()

    def status(self) -> dict:
        return self._get("/health")
