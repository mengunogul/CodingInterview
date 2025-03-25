"""
Question: https://neetcode.io/problems/kth-largest-element-in-an-array
"""

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
