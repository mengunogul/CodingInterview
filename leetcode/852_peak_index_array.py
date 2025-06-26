from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 1
        while left < right:
            mid = (right + left) // 2
            if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
            elif arr[mid - 1] > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
