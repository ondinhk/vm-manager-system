import asyncio
import random


async def sleep_random(max_wait=120, min_wait=1):
    random_number = random.randint(min_wait, max_wait)
    await asyncio.sleep(random_number)
