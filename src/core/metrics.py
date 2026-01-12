import time
import functools
import logging

logging.basicConfig(level=logging.INFO)

def timed(agent_name: str):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = await func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            logging.info(f"[METRICS] {agent_name} took {elapsed:.2f}s")
            return result
        return wrapper
    return decorator
