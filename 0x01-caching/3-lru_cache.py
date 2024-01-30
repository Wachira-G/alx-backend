#!/usr/bin/env python3
"""Inherits from BaseCaching and is a chaching system."""

from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Implements LRU caching."""

    def __init__(self):
        """Initialize by overloading parent's initialization."""
        self.ordered_dict = OrderedDict()
        super().__init__()
        self.ordered_dict.update(self.cache_data)

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS:
        you must discard the least recently used item (LRU algorithm)
        you must print DISCARD: with the key discarded
        and following by a new line
        """
        if key is not None and item is not None:
            # update existing cache
            if key in self.cache_data.keys():
                self.ordered_dict.move_to_end(key)
            # new key and cache full to capacity
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed_item = self.ordered_dict.popitem(last=False)
                self.cache_data.pop(removed_item[0])
                print(f"DISCARD: {removed_item[0]}")

            self.cache_data[key] = item
            self.ordered_dict[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key) if key is not None else None
