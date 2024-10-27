from fastapi import Request, Response
from functools import wraps
from app.core.rate_limit import rate_limiter

async def rate_limit(
    request: Request,
    response: Response,
    limit: int = 5,
    window: int = 60,
    key_prefix: str = "rate_limit"
):
    headers = await rate_limiter.check_rate_limit(
        request,
        limit=limit,
        window=window,
        key_prefix=key_prefix
    )

    # Add rate limit headers to response
    for key, value in headers.items():
        response.headers[key] = value

def rate_limited(limit: int = 5, window: int = 60, key_prefix: str = "rate_limit"):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get("request")
            response = kwargs.get("response")

            if request and response:
                await rate_limit(request, response, limit, window, key_prefix)

            return await func(*args, **kwargs)
        return wrapper
    return decorator
