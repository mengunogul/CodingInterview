"""
Question: https://neetcode.io/problems/find-duplicate-integer
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Method 1: Sorting approach
        # Time Complexity: O(n log n) due to sorting
        # Space Complexity: O(1) as we sort in-place (though the sort implementation may use O(log n) space)

        # Sort the array to bring duplicates next to each other
        nums.sort()  # inplace sorting

        # Keep track of the previous number as we iterate
        prev = nums[0]

        # Iterate through the sorted array starting from the second element
        for cur in nums[1:]:
            # If current number matches previous, we found our duplicate
            if cur == prev:
                return cur
            # Update previous number for next iteration
            prev = cur

        # Note: Problem guarantees at least one duplicate exists, so this return is never reached
        return -1
