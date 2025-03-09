"""
Question: https://neetcode.io/problems/trapping-rain-water

This module provides a solution to compute the amount of trapped rain water.
It uses the two-pointer technique to achieve an O(n) time complexity solution.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Compute the total amount of trapped rain water given the list of heights.

        Uses a two-pointer approach to calculate left_max and right_max while traversing the list.

        :param height: List of non-negative integers representing the elevation map.
        :return: The total amount of water that can be trapped.
        """
        if not height or len(height) < 2:
            return 0

        left: int = 0
        right: int = len(height) - 1
        left_max: int = 0
        right_max: int = 0
        water: int = 0

        # Traverse the height list using two pointers.
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


if __name__ == "__main__":
    sol = Solution()
    heights: List[int] = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    result: int = sol.trap(heights)
    print("Trapped rain water:", result)
