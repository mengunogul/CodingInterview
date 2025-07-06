from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def isSufficientSpeed(cnt):
            return sum(ceil(i / cnt) for i in piles) <= h

        while left < right:
            mid = (left + right) // 2
            if isSufficientSpeed(mid):
                right = mid
            else:
                left = mid + 1

        return left
