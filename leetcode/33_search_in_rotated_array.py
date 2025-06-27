from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        pivot = left

        if target >= nums[pivot] and target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
