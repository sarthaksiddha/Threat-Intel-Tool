from fastapi import FastAPI, Request
from api.middleware.rate_limit import RateLimiter

app = FastAPI()
rate_limiter = RateLimiter(requests_per_minute=60)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    await rate_limiter(request)
    response = await call_next(request)
    return response