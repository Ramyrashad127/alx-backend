#!/usr/bin/env python3


"""import modules"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """child class caching"""

    def __init__(self):
        """constructor of class"""
        super().__init__()
        self.freq = {}
        self.usage_order = []

    def put(self, key, item):
        """delete lfu if sz is max"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                d = [k for k in self.usage_order if self.freq[k] == min_freq]
                discard = d[0]
                print(f"DISCARD: {discard}")
                del self.cache_data[discard]
                del self.freq[discard]
                self.usage_order.remove(discard)

            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """Return the value"""
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
