#!/usr/bin/env python3

"""Concurrent coroutines"""
import asyncio
import random
from typing import List
wait_random = async_generator = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n: spawn wait_random n times with the specified max_delay."""
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
