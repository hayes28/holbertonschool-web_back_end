#!/usr/bin/env python3
""" Redis basic Project Tasks: 0-4 """
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """  Convert the data back to the desired format """
        # Convert the data back to the desired format
        data = self._redis.get(key)
        # If the key does not exist, return None
        if not data:
            return None
        # Apply the function fn if necessary
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """ Convert bytes to string """
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: bytes) -> int:
        """ Convert bytes to int """
        return self.get(key, fn=lambda x: int(x.decode("utf-8")))