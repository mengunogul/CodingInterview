from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        cover = [0] * (len(nums) + 1)
        for left, right in queries:
            cover[left] += 1
            cover[right + 1] -= 1

        for i in range(1, len(cover)):
            cover[i] += cover[i - 1]

        for i, val in enumerate(nums):
            if cover[i] < val:
                return False

        return True
