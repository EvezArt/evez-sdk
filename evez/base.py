"""Shared HTTP helpers for the EVEZ SDK."""
from __future__ import annotations

import json
import logging
import time
from typing import Any, Dict, Optional
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

logger = logging.getLogger("evez")

DEFAULT_TIMEOUT = 5
DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_BACKOFF = 0.5  # seconds


class EvezError(RuntimeError):
    """Base exception for EVEZ SDK errors."""


class ServiceUnavailableError(EvezError):
    """Raised when a backend service is unreachable."""


class ServiceBase:
    """Base class for EVEZ service wrappers.

    Provides ``_get`` / ``_post`` helpers with automatic retry on transient
    failures (connection errors, HTTP 5xx).
    """

    base_url: str = ""
    _max_retries: int = DEFAULT_MAX_RETRIES
    _retry_backoff: float = DEFAULT_RETRY_BACKOFF

    def __init__(self, host: str = "localhost", port: int = 0,
                 timeout: int = DEFAULT_TIMEOUT,
                 max_retries: int = DEFAULT_MAX_RETRIES,
                 retry_backoff: float = DEFAULT_RETRY_BACKOFF) -> None:
        if port:
            self.base_url = f"http://{host}:{port}"
        else:
            self.base_url = host  # allow full URL override
        self._timeout = timeout
        self._max_retries = max_retries
        self._retry_backoff = retry_backoff

    def _request(self, method: str, path: str, data: Optional[Dict[str, Any]] = None,
                 timeout: Optional[int] = None, raw: bool = False) -> Any:
        """Perform an HTTP request with retry logic.

        Args:
            method: "GET" or "POST".
            path: URL path (appended to ``self.base_url``).
            data: JSON body for POST requests.
            timeout: Per-request timeout in seconds.
            raw: If True, return raw bytes instead of parsed JSON.

        Returns:
            Parsed JSON dict (or raw bytes when ``raw=True``).

        Raises:
            ServiceUnavailableError: After all retries are exhausted.
        """
        timeout = timeout or self._timeout
        url = f"{self.base_url}{path}"
        last_exc: Optional[Exception] = None

        for attempt in range(self._max_retries):
            try:
                if method.upper() == "GET":
                    resp = urlopen(url, timeout=timeout)
                else:
                    body = json.dumps(data or {}).encode()
                    req = Request(url, data=body,
                                  headers={"Content-Type": "application/json"})
                    resp = urlopen(req, timeout=timeout)

                if raw:
                    return resp.read()
                return json.loads(resp.read())

            except (URLError, HTTPError, OSError) as exc:
                last_exc = exc
                if attempt < self._max_retries - 1:
                    sleep = self._retry_backoff * (2 ** attempt)
                    logger.debug("retry %d/%d for %s %s in %.1fs: %s",
                                 attempt + 1, self._max_retries, method, path, sleep, exc)
                    time.sleep(sleep)

        raise ServiceUnavailableError(
            f"{method} {path} failed after {self._max_retries} retries: {last_exc}"
        ) from last_exc

    def _get(self, path: str, timeout: Optional[int] = None) -> Dict[str, Any]:
        return self._request("GET", path, timeout=timeout)

    def _post(self, path: str, data: Optional[Dict[str, Any]] = None,
              timeout: Optional[int] = None) -> Dict[str, Any]:
        return self._request("POST", path, data=data, timeout=timeout)

    def _get_raw(self, path: str, data: Optional[Dict[str, Any]] = None,
                 timeout: Optional[int] = None) -> bytes:
        return self._request("POST", path, data=data, timeout=timeout, raw=True)

    def health(self) -> Dict[str, Any]:
        """Check service health."""
        return self._get("/health")
