"""
Question: https://neetcode.io/problems/combination-target-sum
This module generates all unique combinations from a list of numbers that sum to a target.
It uses a backtracking approach with recursion and accumulators to avoid repeated computation.
"""

from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Find all combinations of numbers in 'nums' that sum up to 'target'.

        Args:
            nums (List[int]): List of candidate numbers.
            target (int): The target sum for the combinations.

        Returns:
            List[List[int]]: A list of all valid combinations.
        """
        combinations = []

        def backtracking(index: int, current: List[int], current_sum: int) -> None:
            # Base Case: If the current sum equals the target, record a copy of the current combination.
            if current_sum == target:
                combinations.append(current.copy())
                return
            # If the current sum exceeds the target, no further exploration is needed.
            if current_sum > target:
                return

            # Iterate over possible candidates starting at the current index.
            for i in range(index, len(nums)):
                # Include nums[i] in the current combination.
                current.append(nums[i])
                # Recursively try including the same candidate (allowing repeats)
                # by not incrementing i, or move to the next candidate by using i as the next start.
                backtracking(i, current, current_sum + nums[i])
                # Backtrack: remove the last element added and try the next candidate.
                current.pop()

        backtracking(0, [], 0)
        return combinations


if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2, 5, 6, 9], 9))
