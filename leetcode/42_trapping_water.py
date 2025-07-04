from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        while left < right:
            if left_max > right_max:
                trapped_water += right_max - height[right]
                right -= 1
            else:
                trapped_water += left_max - height[left]
                left += 1

            right_max = max(right_max, height[right])
            left_max = max(left_max, height[left])

        return trapped_water
