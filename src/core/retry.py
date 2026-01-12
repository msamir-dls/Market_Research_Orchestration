import asyncio
import random

async def retry_async(
    fn,
    retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 10.0
):
    for attempt in range(retries):
        try:
            return await fn()
        except Exception as e:
            if attempt == retries - 1:
                raise
            delay = min(max_delay, base_delay * (2 ** attempt))
            delay += random.uniform(0, 0.3)
            await asyncio.sleep(delay)
