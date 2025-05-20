"""
Question: https://neetcode.io/problems/binary-search
This module implements binary search to locate a target value within a sorted list.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Perform binary search on a sorted list to find the target value.

        Args:
            nums (List[int]): A sorted list of integers.
            target (int): The value to search for.

        Returns:
            int: Index of the target if found, else -1.
        """
        # For very small lists, do a quick check.
        if len(nums) < 2 and target not in nums:
            return -1

        left = 0
        right = len(nums) - 1

        # Continue while there is a valid search range.
        while left <= right:
            mid = (left + right) // 2  # Find the middle index.
            if nums[mid] == target:
                return mid  # Target found.
            elif nums[mid] < target:
                left = mid + 1  # Search the right half.
            else:
                right = mid - 1  # Search the left half.

        # Target was not found in the list.
        return -1


if __name__ == "__main__":
    sol = Solution()
    # Test binary search with an example sorted list.
    nums = [-1, 0, 2, 4, 6, 8]
    target = 4  # Expected to find target 4.
    result = sol.search(nums, target)
    print("Result:", result)
