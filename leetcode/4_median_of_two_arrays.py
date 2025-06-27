from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        if len(merged) % 2 == 1:
            return merged[len(merged) // 2]
        else:
            mid = len(merged) // 2
            return (merged[mid] + merged[mid - 1]) / 2
