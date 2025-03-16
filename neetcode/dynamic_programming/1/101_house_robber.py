"""
Question: https://neetcode.io/problems/house-robber
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize two variables:
        # rob_1: maximum money robbed up to the house before the previous one.
        # rob_2: maximum money robbed up to the previous house.
        rob_1 = 0  # No money robbed from houses before the first.
        rob_2 = 0  # No money robbed from the first house yet.

        # Process each house in the nums list.
        for n in nums:
            # Calculate the maximum money if choosing to rob this house versus skipping it.
            # If robbing, add current house's money (n) to rob_1 (money from houses not adjacent).
            # If skipping, keep rob_2.
            temp = max(n + rob_1, rob_2)
            # Update rob_1 to the previous rob_2 for the next iteration.
            rob_1 = rob_2
            # Update rob_2 to the current maximum value.
            rob_2 = temp

        # Return the computed maximum amount after processing all houses.
        return rob_2


if __name__ == "__main__":
    solution = Solution()
    # Example test case where each element represents the money in that house.
    nums = [2, 9, 8, 3, 6]
    # Execute the rob method and print the maximum money that can be robbed.
    print(solution.rob(nums))
