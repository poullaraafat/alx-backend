#!/usr/bin/python3

""" LIFOCache  module
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    '''A class `LIFOCache` that inherits from `BaseCaching`
       and is a caching system
    '''
    def __init__(self):
        """ Initialize BasicCaching by calling the parent class initializer """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data` the
           `item` value for the key `key`
        '''

        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >=\
                BaseCaching.MAX_ITEMS:
            last_item, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_item}")

        self.cache_data[key] = item

    def get(self, key):
        '''return the value in `self.cache_data` linked to `key`
        '''
        return self.cache_data.get(key, None)
