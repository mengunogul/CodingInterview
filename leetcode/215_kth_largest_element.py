from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        kth_element = None
        for _ in range(len(nums) - k + 1):
            kth_element = heapq.heappop(nums)
        return kth_element  # type: ignore
