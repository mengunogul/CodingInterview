from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = 0
        for house in nums:
            temp = first
            first = max(second + house, first)
            second = temp

        return first
