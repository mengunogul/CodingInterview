from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        memo = [0] * (n + 1)
        res = []
        for i in range(n):
            if memo[nums[i]] == 1:
                res.append(nums[i])
            memo[nums[i]] += 1
        return res
