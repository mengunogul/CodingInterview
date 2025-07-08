from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(arr, val):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            return left

        res: List[int] = []
        for num in nums:
            idx = binary_search(res, num)
            if idx == len(res):
                res.append(num)
            else:
                res[idx] = num
        return len(res)
