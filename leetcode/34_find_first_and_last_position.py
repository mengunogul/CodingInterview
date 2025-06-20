from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index = float("inf")
        end_index = -1
        for i, val in enumerate(nums):
            if val == target:
                start_index = min(start_index, i)
                end_index = max(end_index, i)
        if start_index == float("inf") and end_index == -1:
            return [-1, -1]
        return [start_index, end_index]  # type: ignore
