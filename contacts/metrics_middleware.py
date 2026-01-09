import time
from .hg_statsd import counter, timing_ms

class HostedGraphiteAppMetricsMiddleware:
    """
    App-wide metrics:
    - app.http.request_latency_ms (timing)
    - app.http.errors (counter, 5xx + unhandled exceptions)
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = None
        had_exception = False

        try:
            response = self.get_response(request)
            return response
        except Exception:
            had_exception = True
            raise
        finally:
            elapsed_ms = (time.perf_counter() - start) * 1000.0
            timing_ms("app.http.request_latency_ms", elapsed_ms)

            status = getattr(response, "status_code", 200) if response is not None else 200
            if had_exception or status >= 500:
                counter("app.http.errors", 1)
