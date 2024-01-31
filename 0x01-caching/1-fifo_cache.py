#!/usr/bin/env python3
"""module for class FIFOCache which inherits BasicCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class for fifo caching"""
    def __init__(self):
        super().__init__()
        self.temp_data = []

    def put(self, key, item):
        """to put item in cache
        Keyword arguments:
        key: the key to put
        item: value of the key
        Return: return_description
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.temp_data.remove(key)

        self.cache_data[key] = item
        self.temp_data.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = self.temp_data.pop(0)
            del self.cache_data[first_item]
            print("DISCARD: {}".format(first_item))

    def get(self, key):
        """geta an item in cache
        arg:
        key: the keyy to check for value
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
