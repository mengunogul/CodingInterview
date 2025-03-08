"""
Question: https://neetcode.io/problems/products-of-array-discluding-self
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


if __name__ == "__main__":
    sol = Solution()
    result = sol.productExceptSelf([1, 2, 4, 6])
    print(result)
