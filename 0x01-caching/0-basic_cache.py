#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCaching(BaseCaching):
    """ BasicCaching defines:
      """

    def put(self, key, item):
        """ Add an item in the cache if key and item are not None """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item by key if it exists in the cache """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
