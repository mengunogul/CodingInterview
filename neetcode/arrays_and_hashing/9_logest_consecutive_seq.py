"""
Question: https://neetcode.io/problems/longest-consecutive-sequence

This module provides a solution to find the longest consecutive sequence in an unsorted array.
It uses a set-based approach for O(n) time complexity.
"""

from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Find the length of the longest consecutive elements sequence.

        This function converts the list to a set to eliminate duplicates and allow
        O(1) lookups. It then iterates over the set, and for each number that is the
        start of a sequence (i.e., num - 1 is not in the set), it counts the consecutive
        sequence length.

        :param nums: List of integers.
        :return: Length of the longest consecutive sequence.
        """
        num_set: Set[int] = set(nums)
        longest: int = 0

        # Iterate over all numbers in the set
        for num in num_set:
            # Only consider 'num' if it's the start of a sequence
            if num - 1 not in num_set:
                current_streak: int = 1
                # Count the length of the consecutive sequence starting at num
                while (num + current_streak) in num_set:
                    current_streak += 1
                # Update the longest sequence length found so far
                longest = max(longest, current_streak)
        return longest


if __name__ == "__main__":
    # Example usage:
    nums: List[int] = [2, 20, 4, 10, 3, 4, 5]
    sol = Solution()
    result: int = sol.longestConsecutive(nums)
    print("Longest consecutive sequence length:", result)
