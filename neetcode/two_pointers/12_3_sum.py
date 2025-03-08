"""
Question: https://neetcode.io/problems/three-integer-sum

This module provides a solution to the 3-sum problem using a two-pointer approach.
It returns a list of unique triplets (as lists) that sum up to zero.
"""

from typing import List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the list that add up to zero.

        The list is first sorted. Then, for each number in the list treated as a pivot,
        a two-pointer technique is used to find two additional numbers that sum with the pivot to zero.

        :param nums: List of integers.
        :return: List of unique triplets (each triplet is a list of integers) that sum to zero.
        """
        # Sort the array to simplify the two-pointer approach.
        nums.sort()
        triplets: Set[Tuple[int, int, int]] = set()

        # Iterate through each index treating it as pivot.
        for pivot_index, pivot in enumerate(nums):
            left: int = 0
            right: int = len(nums) - 1

            # Use two pointers to find valid pairs.
            while left < right:
                # Skip if the pointer coincides with the pivot.
                if left == pivot_index:
                    left += 1
                    continue
                if right == pivot_index:
                    right -= 1
                    continue

                current_sum: int = pivot + nums[left] + nums[right]
                if current_sum < 0:
                    # Sum too low, increase left pointer.
                    left += 1
                elif current_sum > 0:
                    # Sum too high, decrease right pointer.
                    right -= 1
                else:
                    # Valid triplet found, add it as a sorted tuple to prevent duplicates.
                    triplets.add(tuple(sorted((pivot, nums[left], nums[right]))))  # type: ignore
                    left += 1
                    right -= 1

        # Convert each tuple in the set to a list.
        return [list(triplet) for triplet in triplets]


if __name__ == "__main__":
    # Example usage:
    sol = Solution()
    test_nums: List[int] = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    result: List[List[int]] = sol.threeSum(test_nums)
    print("Unique triplets that sum to zero:", result)
