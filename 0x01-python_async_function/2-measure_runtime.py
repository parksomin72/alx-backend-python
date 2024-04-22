#!/usr/bin/env python3
"""
Module for measuring runtime.
"""

import time
from typing import List
import asyncio
from 1-concurrent_coroutines import wait_n  # Assuming 1-concurrent_coroutines.py has the wait_n coroutine

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

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
