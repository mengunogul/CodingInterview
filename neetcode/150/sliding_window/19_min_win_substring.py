"""
Question: https://neetcode.io/problems/minimum-window-with-characters

This module provides a solution for the Minimum Window Substring problem using
a sliding window technique with two pointers. The solution runs in O(n) time.
"""

from collections import Counter
from math import inf
from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the minimum window substring in s that contains all characters in t.

        :param s: The source string.
        :param t: The target string whose characters must be included in the window.
        :return: The smallest substring of s covering all characters in t. If no such substring exists, return "".
        """
        if not s or not t:
            return ""

        t_freq: Dict[str, int] = Counter(t)
        window_counts: Dict[str, int] = {}
        required: int = len(t_freq)
        formed: int = (
            0  # count of characters that meet required frequency in current window
        )

        left: int = 0
        min_len: float = inf  # type: ignore
        min_window: tuple = (-1, -1)

        # Expand the window with right pointer
        for right, char in enumerate(s):
            # Add current character to window count
            window_counts[char] = window_counts.get(char, 0) + 1

            # If this character is needed and count matches t's requirement, increment formed
            if char in t_freq and window_counts[char] == t_freq[char]:
                formed += 1

            # Contract the window as long as it satisfies the condition
            while left <= right and formed == required:
                # Update minimum window if smaller window is found
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)

                # Prepare to contract: remove the leftmost character from window_counts
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in t_freq and window_counts[left_char] < t_freq[left_char]:
                    formed -= 1
                left += 1

        if min_len == inf:
            return ""
        start, end = min_window
        return s[start : end + 1]


if __name__ == "__main__":
    # Example usage:
    solution = Solution()
    s: str = "OUZODYXAZV"
    t: str = "XYZ"
    result: str = solution.minWindow(s, t)
    print("Minimum window substring:", result)
