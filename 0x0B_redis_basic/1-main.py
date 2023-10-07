""" Main file """

Cache = __import__('exercise').Cache

def test_cache():
    cache = Cache()

    # Test store and retrieve a string
    key1 = cache.store("first")
    assert cache.get_str(key1) == "first"

    # Test store and retrieve an int
    key2 = cache.store(2)
    assert cache.get_int(key2) == 2

    print("All tests passed successfully")

if __name__ == "__main__":
    test_cache()