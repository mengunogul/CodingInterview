from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result: int = 0
        min_distance: float = float("inf")

        for i in range(len(nums) - 2):
            left: int = i + 1
            right: int = len(nums) - 1

            while left < right:
                curr_sum: int = nums[i] + nums[left] + nums[right]
                distance: float = abs(target - curr_sum)

                if distance < min_distance:
                    min_distance = distance
                    result = curr_sum

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
