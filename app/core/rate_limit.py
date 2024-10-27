from fastapi import HTTPException, Request
from redis import Redis
from datetime import datetime
import os

class RateLimiter:
    def __init__(self):
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
        self.redis = Redis.from_url(redis_url, decode_responses=True)

    async def check_rate_limit(
        self,
        request: Request,
        limit: int = 5,  # Number of requests
        window: int = 60,  # Time window in seconds
        key_prefix: str = "rate_limit"
    ):
        # Get client IP
        client_ip = request.client.host

        # Create a unique key for this IP and endpoint
        path = request.url.path
        key = f"{key_prefix}:{client_ip}:{path}"

        # Get the current timestamp
        now = datetime.now().timestamp()

        # Clean up old requests
        self.redis.zremrangebyscore(key, 0, now - window)

        # Count recent requests
        request_count = self.redis.zcard(key)

        if request_count >= limit:
            raise HTTPException(
                status_code=429,
                detail={
                    "error": "Too many requests",
                    "wait_seconds": window - (now - float(self.redis.zrange(key, 0, 0)[0]))
                }
            )

        # Add this request to the sorted set
        self.redis.zadd(key, {str(now): now})

        # Set expiry on the key
        self.redis.expire(key, window)

        # Add rate limit info to response headers
        return {
            "X-RateLimit-Limit": str(limit),
            "X-RateLimit-Remaining": str(limit - request_count - 1),
            "X-RateLimit-Reset": str(int(now + window))
        }

rate_limiter = RateLimiter()
