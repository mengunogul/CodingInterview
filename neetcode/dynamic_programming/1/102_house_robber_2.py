"""
Question: https://neetcode.io/problems/house-robber-ii
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Rob houses excluding the first or the last house.
        return max(nums[0], self._rob_linearly(nums[1:]), self._rob_linearly(nums[:-1]))

    def _rob_linearly(self, houses: List[int]) -> int:
        """Helper method to compute the max rob amount for a linear street of houses."""
        prev, curr = 0, 0
        for money in houses:
            prev, curr = curr, max(curr, prev + money)
        return curr


if __name__ == "__main__":
    solution = Solution()
    # Example test case where each element represents the money in that house.
    nums = [3, 4, 3]
    # Execute the rob method and print the maximum money that can be robbed.
    print(solution.rob(nums))
