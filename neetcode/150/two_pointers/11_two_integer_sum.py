"""
Question: https://neetcode.io/problems/two-integer-sum-ii

This module provides a solution to find two numbers in a sorted list that sum up to a target,
returning their 1-indexed positions using a two-pointer approach.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers in the sorted list 'numbers' that add up to 'target'
        and return their indices (1-indexed).

        :param numbers: A list of integers sorted in ascending order.
        :param target: The target sum.
        :return: A list containing the 1-indexed positions of the two numbers.
        """
        left: int = 0
        right: int = len(numbers) - 1

        while left < right:
            cur_sum: int = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    # Example usage:
    sol = Solution()
    numbers: List[int] = [1, 2, 3, 4]
    target: int = 3  # Adjust target as needed
    result: List[int] = sol.twoSum(numbers, target)
    print("Indices of the two numbers:", result)
