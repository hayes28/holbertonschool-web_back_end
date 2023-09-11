#!/usr/bin/python3
"""Create a class BasicCache that inherits from
BaseCaching and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Create a class BasicCache"""
    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
