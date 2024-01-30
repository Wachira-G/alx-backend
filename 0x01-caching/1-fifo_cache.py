#!/usr/bin/env python3
"""Inherits from BaseCaching and is a chaching system."""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Implements FIFO caching."""

    def __init__(self):
        """Initialize by overloading parent's initialization."""
        self.indexing = []
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded
        and following by a new line
        """
        first_inserted = None
        if key is not None and item is not None:
            if key not in self.indexing:
                self.indexing.append(key)
            self.cache_data[key] = item
            if len(self.indexing) > self.MAX_ITEMS:
                first_inserted = self.indexing.pop(0)
                del self.cache_data[first_inserted]
                print(f"DISCARD: {first_inserted}")

    def get(self, key):
        """Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key) if key is not None else None
