#!/usr/bin/env python3
"""
Module for measuring runtime.
"""

import time
from typing import Callable


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that executes multiple coroutines concurrently.

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay in seconds for each coroutine.

    Returns:
        List[float]: List of delays in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)

def measure_time(n: int, max_delay: int) -> float:
    """
    Function to measure the total execution time for wait_n(n, max_delay)
    and return the average time per coroutine.

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay in seconds for each coroutine.

    Returns:
        float: Average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
