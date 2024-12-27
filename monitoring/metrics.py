from prometheus_client import Counter, Histogram
from functools import wraps
import time

HTTP_REQUEST_COUNTER = Counter('http_requests_total', 'Total HTTP requests')
RESPONSE_TIME = Histogram('response_time_seconds', 'Response time in seconds')

def monitor_endpoint(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        HTTP_REQUEST_COUNTER.inc()
        start_time = time.time()
        response = await func(*args, **kwargs)
        RESPONSE_TIME.observe(time.time() - start_time)
        return response
    return wrapper