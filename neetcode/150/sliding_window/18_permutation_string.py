"""
Question: https://neetcode.io/problems/permutation-string

This module provides an optimized solution for checking if s2 contains a permutation of s1.
An incremental sliding window approach is used with O(n) time complexity.
"""

from collections import Counter
from typing import Counter as CounterType  # for type annotation


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if s2 contains a permutation of s1.

        Uses a sliding window of size len(s1) and updates the frequency counter incrementally.

        :param s1: Target permutation string.
        :param s2: Source string to search within.
        :return: True if a permutation of s1 exists in s2, False otherwise.
        """
        len_s1: int = len(s1)
        len_s2: int = len(s2)
        if len_s1 > len_s2:
            return False

        s1_counter: CounterType[str] = Counter(s1)
        window_counter: CounterType[str] = Counter(s2[:len_s1])

        # Check first window
        if window_counter == s1_counter:
            return True

        # Slide the window, update counters incrementally.
        for i in range(len_s1, len_s2):
            # Remove the left character of the previous window.
            left_char: str = s2[i - len_s1]
            window_counter[left_char] -= 1
            if window_counter[left_char] == 0:
                del window_counter[left_char]

            # Add the new right character.
            right_char: str = s2[i]
            window_counter[right_char] = window_counter.get(right_char, 0) + 1

            if window_counter == s1_counter:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    s1: str = "ab"
    s2: str = "lecabee"
    result: bool = sol.checkInclusion(s1, s2)
    print("Permutation exists:" if result else "Permutation does not exist:", result)
