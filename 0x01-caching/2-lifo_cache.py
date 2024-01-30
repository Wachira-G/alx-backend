#!/usr/bin/env python3
"""Inherits from BaseCaching and is a chaching system."""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements LIFO caching."""

    def __init__(self):
        """Initialize by overloading parent's initialization."""
        self.indexing = []
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        you must print DISCARD: with the key discarded and following by a new line
        """
        last_inserted = None
        if key is not None and item is not None:
            if key in self.indexing:
                self.indexing.remove(key)
            self.indexing.append(key)
            self.cache_data[key] = item
            if len(self.indexing) > self.MAX_ITEMS:
                last_inserted = self.indexing.pop(-2)
                del self.cache_data[last_inserted]
                print(f"DISCARD: {last_inserted}")

    def get(self, key):
        """Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        return self.cache_data.get(key) if key != None else None
