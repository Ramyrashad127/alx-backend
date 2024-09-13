#!/usr/bin/env python3


"""import modules"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """child caching class"""
    def __init__(self):
        """constructor of class"""
        super().__init__()
        self.data = []

    def put(self, key, item):
        """assign item to dictionary"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.data.remove(key)
            self.data.append(key)
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                remove = self.data.pop(0)
                print(f"DISCARD: {remove}")
                self.cache_data.pop(remove)

            self.cache_data[key] = item
            self.data.append(key)

    def get(self, key):
        """get item from cachie"""
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        self.data.remove(key)
        self.data.append(key)
        return self.cache_data[key]
