from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        memo: dict[int, int] = {}

        max_len = 0
        prefix_sum = 0
        for idx, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1
            if prefix_sum == 0:
                max_len = idx + 1
            elif prefix_sum in memo:
                max_len = max(max_len, idx - memo.get(prefix_sum, prefix_sum))
            else:
                memo[prefix_sum] = idx
        return max_len
