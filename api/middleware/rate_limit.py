from fastapi import Request, HTTPException
from typing import Dict, Tuple
from datetime import datetime, timedelta
from collections import defaultdict

class RateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.requests_per_minute = requests_per_minute
        self.requests: Dict[str, list] = defaultdict(list)
    
    async def __call__(self, request: Request):
        client_ip = request.client.host
        now = datetime.now()
        
        # Clean old requests
        self.requests[client_ip] = [
            req_time for req_time in self.requests[client_ip]
            if now - req_time < timedelta(minutes=1)
        ]
        
        # Check rate limit
        if len(self.requests[client_ip]) >= self.requests_per_minute:
            raise HTTPException(
                status_code=429,
                detail="Too many requests"
            )
        
        self.requests[client_ip].append(now)
        return True