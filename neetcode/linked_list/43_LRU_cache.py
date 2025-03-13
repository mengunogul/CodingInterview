"""
Question: https://neetcode.io/problems/lru-cache
"""

from collections import OrderedDict


class LRUCache:
    """A class implementing an LRU (Least Recently Used) cache with fixed capacity."""

    def __init__(self, capacity: int):
        """Initialize the cache with a given capacity."""
        # Initialize cache as an OrderedDict and set the capacity.
        self.cache: OrderedDict = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        """Retrieve the value associated with key and mark it as recently used.

        Returns:
            int: The value if key exists, otherwise -1.
        """
        # Check if key exists; if not, return -1.
        if key not in self.cache:
            return -1
        # Key exists: move it to the end to mark it as recently used.
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """Insert or update the key-value pair. Evicts the least recently used item if capacity is exceeded."""
        # If key is already in cache, update its position to recent.
        if key in self.cache:
            self.cache.move_to_end(key)
        # Insert or update the key with the new value.
        self.cache[key] = value

        # If cache exceeds its capacity, remove the least recently used item.
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
