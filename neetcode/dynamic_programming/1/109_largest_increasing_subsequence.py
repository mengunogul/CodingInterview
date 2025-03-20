"""
Question:
"""

from typing import List
from functools import lru_cache


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(index, last):
            if index >= len(nums):
                return 0

            max_length = 0
            for i in range(index, len(nums)):
                if nums[i] > last:
                    max_length = max(max_length, 1 + dfs(i + 1, nums[i]))
            return max_length

        return dfs(0, float("-inf"))


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(sol.lengthOfLIS(nums))
