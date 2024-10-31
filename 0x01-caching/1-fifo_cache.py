#!/usr/bin/python3
""" FIFOCache  module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from `BaseCaching`
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
        if key is None and item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_item)

        self.cache_data[key] = item

    def get(self, key):
        '''return the value in `self.cache_data` linked to `key`
        '''

        return self.cache_data.get(key, None)
