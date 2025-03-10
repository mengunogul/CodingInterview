"""
Question: https://neetcode.io/problems/search-in-rotated-sorted-array
This module searches for a target value in a rotated sorted array.
It first locates the pivot (the smallest element) and then performs a standard binary search
in the appropriate sorted subarray.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for a target value in a rotated sorted array.

        This function first finds the pivot point (the index of the smallest element) in the array,
        determines which of the two sorted subarrays may contain the target, and then performs
        a standard binary search on that subarray.

        Args:
            nums (List[int]): A rotated sorted array of integers.
            target (int): The integer value to search for.

        Returns:
            int: The index of the target if found, otherwise -1.
        """
        left = 0
        right = len(nums) - 1

        # First Pass: Find pivot (index of smallest element) using binary search.
        while left < right:
            mid = (left + right) // 2  # Calculate middle index.
            # If mid element is less than the rightmost element,
            # the pivot is in the left half (including mid).
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        pivot = left  # Pivot where the smallest element is located.

        # Second Pass: Standard binary search in the chosen subarray.
        # Determine which sorted subarray to search for the target.
        if target >= nums[pivot] and target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot - 1

        while left <= right:
            mid = (left + right) // 2  # Re-calculate middle index.
            if target == nums[mid]:
                return mid  # Target found.
            elif nums[mid] < target:
                left = mid + 1  # Search in the right half.
            else:
                right = mid - 1  # Search in the left half.
        return -1


if __name__ == "__main__":
    solution = Solution()
    # Test case: Search for a target in a rotated sorted array.
    test_case = [4, 5, 6, 7, 0, 1, 2]
    print(solution.search(test_case, 0))
