#!/usr/bin/env python3


"""import modules"""
from base_caching import BaseCaching
import queue


class FIFOCache(BaseCaching):
    """child caching class"""
    def __init__(self):
        """constructor of class"""
        super().__init__()
        self.q = queue.Queue()

    def put(self, key, item):
        """assign item to dictionary"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                remove = self.q.get()
                print(f"DISCARD: {remove}")
                self.cache_data.pop(remove)
                self.cache_data[key] = item
                self.q.put(key)
            else:
                self.cache_data[key] = item
                self.q.put(key)

    def get(self, key):
        """get item from cachie"""
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
