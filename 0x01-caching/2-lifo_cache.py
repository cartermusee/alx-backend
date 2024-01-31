#!/usr/bin/env python3
"""module for class LIFOCache which inherits BasicCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None and item is None:
            pass
        else:
            if len(self.cache_data.get) >= BaseCaching.MAX_ITEMS:
                last_item = next(reversed(self.cache_data))
                print("DISCARD: {}".format(last_item))
                del self.cache_data[last_item]
            self.cache_data[key] = item

    def get(self, key):
        """geta an item in cache
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)