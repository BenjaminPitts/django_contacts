import os
import socket

STATSD_HOST = "statsd.hostedgraphite.com"
STATSD_PORT = 8125

HG_API_KEY = os.getenv("HG_API_KEY")
HG_PREFIX = os.getenv("HG_PREFIX", "demo.heroku_django")

_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def _enabled() -> bool:
    return bool(HG_API_KEY)

def counter(path: str, value: int = 1) -> None:
    if not _enabled():
        return

    key = f"{HG_API_KEY}.{HG_PREFIX}.{path}"
    msg = f"{key}:{value}|c"
    try:
        _sock.sendto(msg.encode("utf-8"), (STATSD_HOST, STATSD_PORT))
    except Exception:
        pass

def timing_ms(path: str, value_ms: float) -> None:
    if not _enabled():
        return

    key = f"{HG_API_KEY}.{HG_PREFIX}.{path}"
    msg = f"{key}:{value_ms:.3f}|ms"
    try:
        _sock.sendto(msg.encode("utf-8"), (STATSD_HOST, STATSD_PORT))
    except Exception:
        pass
