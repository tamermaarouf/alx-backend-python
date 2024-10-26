#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n.
code is nearly identical to wait_n except task_wait_random is being called."""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency."""
    tasks = [task_wait_random(max_delay) for delay in range(n)]
    task = asyncio.as_completed(tasks)
    result = [await res for res in task]
    return result
