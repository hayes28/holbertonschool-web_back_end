#!/usr/bin/env python3
""" Redis basic Project Tasks: 0-4 """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class """
    def __init__(self):
        """  Create an instance of the Redis client and flush the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store the input data in Redis using a randomly generated key """
        # Generate a random key
        key = str(uuid.uuid4())
        # Store the input data in Redis using the random key
        self._redis.set(key, data)
        return key