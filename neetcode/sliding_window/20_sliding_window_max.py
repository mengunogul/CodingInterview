"""
Question: https://neetcode.io/problems/sliding-window-maximum

This module implements a solution for the Sliding Window Maximum problem.
It calculates the maximum value in each sliding window of size k over the input list.
"""

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Return a list containing the maximum value in every sliding window of size k.

        :param nums: List of integer values.
        :param k: Size of the sliding window.
        :return: List of maximum values for each window.
        """
        max_list = []  # List to store the maximum of each sliding window
        left = 0  # Initialize left pointer of the window

        # Iterate with right pointer such that each window from left to right has size k.
        for right in range(k, len(nums) + 1):
            window = nums[left:right]  # Current sliding window slice
            max_list.append(max(window))  # Append the maximum value in current window
            left += 1  # Move the window one position to the right
        return max_list


if __name__ == "__main__":
    # Example usage:
    nums = [1, 2, 1, 0, 4, 2, 6]
    k = 3
    solution = Solution()
    result = solution.maxSlidingWindow(nums, k)
    print(result)
