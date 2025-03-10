"""
Question: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
This module finds the minimum element in a rotated sorted array using a binary search approach.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum element in a rotated sorted array.

        Args:
            nums (List[int]): A rotated sorted array of integers.

        Returns:
            int: The minimum element in the array.
        """
        left = 0
        right = len(nums) - 1

        # Use binary search to locate the minimum element.
        while left < right:
            mid = (left + right) // 2  # Get the middle index.
            # If middle element is less than the element at right,
            # the minimum is in the left half (including mid).
            if nums[mid] < nums[right]:
                right = mid
            else:
                # Otherwise, the minimum must be in the right half.
                left = mid + 1

        # When left equals right, the smallest element is found.
        return nums[left]


if __name__ == "__main__":
    solution = Solution()
    # Test case: find the minimum element in a rotated array.
    test_case = [4, 5, 6, 7]
    print(solution.findMin(test_case))
