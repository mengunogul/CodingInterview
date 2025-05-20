"""
Question: https://neetcode.io/problems/last-stone-weight
"""

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) != 1:
            stone_1 = -heapq.heappop(stones)
            stone_2 = -heapq.heappop(stones)
            heapq.heappush(stones, -abs(stone_1 - stone_2))
        return -heapq.heappop(stones)


if __name__ == "__main__":
    stones = [2, 3, 6, 2, 4]
    solution = Solution()
    print(solution.lastStoneWeight(stones))
