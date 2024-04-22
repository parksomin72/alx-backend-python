#!/usr/bin/env python3
"""
Module for concurrent coroutines.
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


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
