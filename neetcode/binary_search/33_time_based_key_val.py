"""
Question: https://neetcode.io/problems/time-based-key-value-store
This module implements a time-based key-value store that supports setting a key with a value and a timestamp,
and retrieving the value associated with a key at a given timestamp using efficient binary search.
"""

import bisect


class TimeMap:
    def __init__(self) -> None:
        """
        Initialize the TimeMap with an empty dictionary.
        The dictionary maps a key to a list of (timestamp, value) tuples.
        """
        self.store: dict = {}  # key: list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Set the key with the given value and timestamp.

        Args:
            key (str): The key to store.
            value (str): The value to associate with the key.
            timestamp (int): The timestamp associated with the value.
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieve the value associated with the key such that its timestamp is less than or equal to the given timestamp.

        Args:
            key (str): The key to retrieve.
            timestamp (int): The timestamp for the query.

        Returns:
            str: The value corresponding to the largest timestamp less than or equal to the given timestamp,
                 or an empty string if no such value exists.
        """
        if key not in self.store:
            return ""

        pairs = self.store[key]  # list of (timestamp, value), sorted by timestamp
        # Use bisect_right to find the insertion point for (timestamp, ...)
        idx = (
            bisect.bisect_right(pairs, (timestamp, chr(127))) - 1
        )  # chr(127) is a high-value placeholder
        if idx >= 0:
            return pairs[idx][1]
        return ""
