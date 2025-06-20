from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = float("-inf")
        prev = float("-inf")
        for i in nums:
            sub = max(prev + i, i)
            prev = sub
            max_sub = max(sub, max_sub)
        return max_sub  # type: ignore
