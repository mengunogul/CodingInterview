from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_width = 0
        stack: List[int] = []

        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                idx = stack.pop()
                max_width = max(max_width, j - idx)

        return max_width
