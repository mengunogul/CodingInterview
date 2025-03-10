"""
Question: https://neetcode.io/problems/subsets
This module generates all possible subsets of a list of integers using backtracking.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all subsets of the list 'nums'.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[List[int]]: A list containing all subsets of nums.
        """
        result: List[List[int]] = []

        def backtrack(index: int, current: List[int]) -> None:
            # If we've considered all elements, record the current subset.
            if index == len(nums):
                result.append(current.copy())
                return

            # Decision 1: Do not include the current element.
            backtrack(index + 1, current)

            # Decision 2: Include the current element.
            current.append(nums[index])
            backtrack(index + 1, current)
            # Backtrack: Remove the last element before exploring other possibilities.
            current.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
