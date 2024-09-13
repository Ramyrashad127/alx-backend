#!/usr/bin/env python3


"""import modules"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """child caching class"""
    def __init__(self):
        """constructor of class"""
        super().__init__()

    def put(self, key, item):
        """assign item to dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get item from cachie"""
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
