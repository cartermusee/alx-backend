#!/usr/bin/env python3
"""module for class BasicCache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class for basic cache"""
    def put(self, key, item):
        """to put item in cache
        Keyword arguments:
        key: the key to put
        item: value of the key
        Return: return_description
        """
        if key is None and item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """geta an item in cache
        arg:
        key: the keyy to check for value
        Return: key of the item
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
