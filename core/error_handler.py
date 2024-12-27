from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import Union

class ThreatIntelException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code

async def error_handler(request, exc: Union[ThreatIntelException, Exception]):
    if isinstance(exc, ThreatIntelException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.message}
        )
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )