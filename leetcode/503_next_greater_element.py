from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack: List[int] = []
        res = [-1] * n

        for i in range(n * 2):
            i = i % (n)
            while stack and nums[stack[-1]] < nums[i]:
                j = stack.pop()
                res[j] = nums[i]
            stack.append(i)
        return res
