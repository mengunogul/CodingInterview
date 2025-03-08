"""
Question: https://neetcode.io/problems/max-water-container

This module provides an optimized solution for finding the maximum area of water a container can hold.
A two-pointer approach is used to achieve O(n) time complexity.
"""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Calculate the maximum area of water that can be contained.

        The function uses a two-pointer technique:
        - Initialize pointers at both ends.
        - Move the pointer with the smaller height inward.
        - Update the maximum area at each step.

        :param heights: A list of non-negative integers representing container heights.
        :return: The maximum area of water the container can hold.
        """
        left: int = 0
        right: int = len(heights) - 1
        max_area: int = 0

        while left < right:
            # Calculate area using the lower of the two heights.
            current_area: int = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, current_area)

            # Move the pointer corresponding to the shorter height.
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    # Example usage:
    solution = Solution()
    heights: List[int] = [1, 7, 2, 5, 4, 7, 3, 6]
    result: int = solution.maxArea(heights)
    print("Maximum water container area:", result)
