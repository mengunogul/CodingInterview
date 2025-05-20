"""
Question: https://neetcode.io/problems/partition-equal-subset-sum
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        memo: dict[tuple, bool] = {}

        def dfs(index, current_sum):
            # If we've reached the target, a valid partition is found.
            if current_sum == target:
                return True
            # If out of bounds or current_sum exceeds target, stop exploring.
            if index >= len(nums) or current_sum > target:
                return False
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            # Try including nums[index] in the subset.
            include = dfs(index + 1, current_sum + nums[index])
            # Or skip the current number.
            skip = dfs(index + 1, current_sum)

            memo[(index, current_sum)] = include or skip
            return memo[(index, current_sum)]

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.canPartition(nums))
