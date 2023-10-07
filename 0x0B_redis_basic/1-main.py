#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

if __name__ == "__main__":
    cache = Cache()

    # Test storing and retrieving a string
    key1 = cache.store("first")
    print(cache.get(key1, lambda x: x.decode("utf-8")))  # Should print "hello"

    # Test storing and retrieving an int
    key2 = cache.store(2)
    print(cache.get(key2, lambda x: int(x.decode("utf-8"))))  # Should print 42
