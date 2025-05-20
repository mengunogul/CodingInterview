"""
Question: https://neetcode.io/problems/kth-largest-integer-in-a-stream
"""

from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        return heapq.nlargest(self.k, self.nums)[-1]
