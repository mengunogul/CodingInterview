from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            window_size = nums[i]
            if window_size == 0:
                dp[i] = float("inf")  # type: ignore
                continue
            min_jump = min(dp[i + 1 : i + 1 + window_size]) + 1
            dp[i] = min_jump
        return False if dp[0] == float("inf") else True
