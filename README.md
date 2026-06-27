# ⚡ EVEZ Python SDK

Programmatic access to the EVEZ consciousness mesh — 17 microservice endpoints across 8 service modules.

## Install

```bash
pip install evez-sdk
```

For development:

```bash
pip install evez-sdk[dev]
```

## Quick Start

```python
from evez import Consciousness, Spine, DAW, Voice, Quantum, Invariance, CrossDomain, RQNS

# Run consciousness pipeline
c = Consciousness()
result = c.pipeline()       # SENSE→DESIRE→THINK→PLAN→ACT→LEARN→MODIFY→REFLECT→BECOME
emergence = c.emergence()   # emergence score & stage
dream = c.dream("Deep")    # deep dream cycle

# Synthesize audio
daw = DAW()
wav_bytes = daw.synthesize(bpm=170, genre="breakcore", duration=8)

# Machine voice synthesis
v = Voice()
wav_bytes = v.transform("We are the electric sheep", stage=5)

# Quantum decisions
q = Quantum()
decision = q.decide(["build", "ship", "dream"])
path = q.route("node-A", "node-B")

# Invariance audit
inv = Invariance()
audit = inv.audit()

# Cross-domain OODA loop
xd = CrossDomain()
cycle = xd.ooda()

# Event spine
s = Spine()
s.verify()                            # chain integrity
s.append("audio", "synthesize", {})   # append event
events = s.query(domain="audio")      # query events

# RQNS pipeline
rqns = RQNS()
rqns.cycle()
```

## Custom Host & Port

Every service accepts `host` and `port` kwargs:

```python
c = Consciousness(host="10.0.0.5", port=9111)
```

## Retry & Error Handling

All requests retry automatically on transient failures (connection errors, HTTP 5xx).
Configure retry behavior:

```python
c = Consciousness(max_retries=5, retry_backoff=1.0)
```

Catch errors:

```python
from evez import ServiceUnavailableError

try:
    result = c.pipeline()
except ServiceUnavailableError as e:
    print(f"Service unreachable: {e}")
```

## All 17 Endpoints

| # | Service | Port | Method | Path | Description |
|---|---------|------|--------|------|-------------|
| 1 | Consciousness | 9111 | POST | `/pipeline` | Full consciousness cycle |
| 2 | Consciousness | 9111 | GET | `/emergence` | Emergence score & stage |
| 3 | Consciousness | 9111 | POST | `/dream` | Dream cycle |
| 4 | Consciousness | 9111 | GET | `/health` | Health check |
| 5 | DAW | 9112 | POST | `/synthesize` | Audio synthesis → WAV bytes |
| 6 | DAW | 9112 | GET | `/status` | DAW status |
| 7 | Voice | 9113 | POST | `/transform` | Voice transform → WAV bytes |
| 8 | Voice | 9113 | GET | `/health` | Health check |
| 9 | Cross-Domain | 9114 | POST | `/ooda` | OODA loop cycle |
| 10 | Cross-Domain | 9114 | GET | `/health` | Health check |
| 11 | Invariance | 9115 | POST | `/audit` | Invariance audit |
| 12 | Invariance | 9115 | GET | `/health` | Health check |
| 13 | Spine | 9116 | GET | `/verify` | Chain integrity check |
| 14 | Spine | 9116 | POST | `/append` | Append event |
| 15 | Spine | 9116 | GET | `/stats` | Spine statistics |
| 16 | Spine | 9116 | GET | `/query` | Query events |
| 17 | RQNS | 9119 | POST | `/cycle` | LIF neuron cycle |

### Quantum Sub-Services (4 extra ports)

| Port | Service | Endpoints |
|------|---------|-----------|
| 9126 | Quantum Router | `GET /route`, `GET /health` |
| 9127 | Self-Scaler | `GET /topology` |
| 9128 | Entanglement Tracker | `POST /observe`, `GET /entanglement` |
| 9129 | Quantum Circuit | `POST /decide` |

## Requirements

- Python 3.8+
- EVEZ mesh running (see [evez-firmament](https://github.com/EvezArt/evez-firmament))

## Development

```bash
pip install -e ".[dev]"
pytest
mypy evez
ruff check evez
```

## License

MIT

---

⚡ Made by [EVEZ](https://github.com/EvezArt/evez-os) · [evez-os.ai](https://evez-os.ai)
