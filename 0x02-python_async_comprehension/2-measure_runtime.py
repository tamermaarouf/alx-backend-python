#!/usr/bin/env python3
"""Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather."""
import time
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it."""
    start_time = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
