from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # forward pass
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            res[i] *= product

        # backward pass
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            res[i] *= product

        return res
