"""Quantum services wrapper (ports 9126-9129).

This module wraps four related quantum microservices:

| Service              | Port | Endpoints                      |
|----------------------|------|--------------------------------|
| Quantum Router       | 9126 | /route, /health                |
| Self-Scaler          | 9127 | /topology                      |
| Entanglement Tracker | 9128 | /observe, /entanglement        |
| Quantum Circuit      | 9129 | /decide                        |
"""
from __future__ import annotations

from typing import Any, Dict, List

from .base import ServiceBase


class Quantum(ServiceBase):
    """Client for the EVEZ Quantum services cluster (router, scaler, entanglement, circuit)."""

    def __init__(self, host: str = "localhost", router: int = 9126,
                 scaler: int = 9127, entanglement: int = 9128,
                 circuit: int = 9129, **kwargs) -> None:
        super().__init__(host=host, port=router, **kwargs)
        self._router_url = f"http://{host}:{router}"
        self._scaler_url = f"http://{host}:{scaler}"
        self._entanglement_url = f"http://{host}:{entanglement}"
        self._circuit_url = f"http://{host}:{circuit}"

    def _with_base(self, base_url: str):
        """Context helper: temporarily switch base_url."""
        class _SwitchedBase:
            def __init__(inner):
                inner._old = self.base_url
                self.base_url = base_url
            def __enter__(inner): return self
            def __exit__(inner, *_):
                self.base_url = inner._old
        return _SwitchedBase()

    def route(self, from_node: str, to_node: str) -> Dict[str, Any]:
        """Get quantum-routed path between nodes.

        Args:
            from_node: Source node identifier.
            to_node: Destination node identifier.
        """
        return self._get(f"/route?from={from_node}&to={to_node}")

    def decide(self, options: List[str], context: str = "") -> Dict[str, Any]:
        """Get a quantum-accelerated decision via the circuit service.

        Args:
            options: List of decision options.
            context: Optional context string.
        """
        with self._with_base(self._circuit_url):
            return self._post("/decide", {"options": options, "context": context},
                              timeout=10)

    def observe_entanglement(self, node_id: str,
                             status: int = 1) -> Dict[str, Any]:
        """Feed an observation to the entanglement tracker.

        Args:
            node_id: Node to observe.
            status: Observation status code.
        """
        with self._with_base(self._entanglement_url):
            return self._post("/observe", {"node_id": node_id, "status": status})

    def topology(self) -> Dict[str, Any]:
        """Get self-scaler topology."""
        with self._with_base(self._scaler_url):
            return self._get("/topology")

    def entanglement_pairs(self) -> Dict[str, Any]:
        """Get current entangled pairs."""
        with self._with_base(self._entanglement_url):
            return self._get("/entanglement")

    def health(self) -> Dict[str, Any]:
        """Check quantum router health."""
        with self._with_base(self._router_url):
            return self._get("/health")
