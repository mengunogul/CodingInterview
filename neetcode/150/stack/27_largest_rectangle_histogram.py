"""
Question: https://neetcode.io/problems/largest-rectangle-in-histogram
This module solves the Largest Rectangle in Histogram problem from Neetcode.
It calculates the maximum rectangular area in a histogram.
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Calculate the largest rectangle area in the histogram.

        Args:
            heights (List[int]): List of integers representing the histogram's bar heights.

        Returns:
            int: The area of the largest rectangle.
        """
        n = len(heights)
        maxArea = 0
        stack: List = []  # stack to store indices

        # Iterate through all bars plus one extra iteration to flush the stack.
        for i in range(n + 1):
            # Check if the current bar is lower than the last bar in the stack.
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                # Pop the last index and calculate area with the popped bar as the smallest bar.
                height = heights[stack.pop()]
                # Determine the width of the rectangle with the popped bar.
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            # Push current index onto stack.
            stack.append(i)
        return maxArea


if __name__ == "__main__":
    sol = Solution()
    # Test case: demonstrate calculation of largest rectangle area.
    test_heights = [7, 1, 7, 2, 2, 4]
    result = sol.largestRectangleArea(test_heights)
    print("Largest rectangle area:", result)
