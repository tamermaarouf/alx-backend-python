#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called."""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency."""
    tasks = [wait_random(max_delay) for delay in range(n)]
    result = [(await res) for res in asyncio.as_completed(tasks)]
    return result