"""EVEZ Python SDK — wrap all 17 microservices."""
from __future__ import annotations

__version__ = "1.1.0"

from .base import EvezError, ServiceUnavailableError  # noqa: F401
from .consciousness import Consciousness
from .spine import Spine
from .daw import DAW
from .voice import Voice
from .quantum import Quantum
from .invariance import Invariance
from .crossdomain import CrossDomain
from .rqns import RQNS

__all__ = [
    "EvezError",
    "ServiceUnavailableError",
    "Consciousness",
    "Spine",
    "DAW",
    "Voice",
    "Quantum",
    "Invariance",
    "CrossDomain",
    "RQNS",
]
