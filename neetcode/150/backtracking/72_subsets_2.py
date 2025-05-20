"""
Questions: https://neetcode.io/problems/subsets-ii
This module implements a solution for finding all possible unique subsets of a list that may contain duplicate elements.
The approach uses backtracking with sorting to handle duplicates efficiently.
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique subsets of the input array which may contain duplicate elements.

        Args:
            nums (List[int]): Input array which may contain duplicate elements.

        Returns:
            List[List[int]]: A list of all unique subsets.
        """
        subsets = []  # Store all unique subsets
        nums.sort()  # Sort to group duplicates together

        def backtrack(iter: int, subset: List[int]):
            """
            Recursive backtracking function to build all unique subsets.

            Args:
                iter (int): Current index in nums array
                subset (List[int]): Current subset being constructed
            """
            # Base case: when we've processed all elements
            if iter == len(nums):
                subsets.append(subset[:])  # Add a copy of the current subset
                return

            # Case 1: Include current element at index 'iter'
            subset.append(nums[iter])
            backtrack(iter + 1, subset[:])  # Recurse with current element included
            subset.pop()  # Backtrack: remove the element we just added

            # Case 2: Skip current element and all its duplicates
            while iter + 1 < len(nums) and nums[iter] == nums[iter + 1]:
                iter += 1  # Skip duplicates to avoid generating duplicate subsets
            backtrack(iter + 1, subset[:])  # Recurse after skipping duplicates

        backtrack(0, [])
        return subsets


if __name__ == "__main__":
    solver = Solution()
    nums = [1, 2, 1]
    print(solver.subsetsWithDup(nums))  # Test with a sample input containing duplicates
