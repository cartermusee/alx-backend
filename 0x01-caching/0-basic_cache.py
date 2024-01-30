#!/usr/bin/env python3
"""module for class BasicCache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class for basic cache"""
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None and item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """geta an item in cache
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.cache_data.get(key)
