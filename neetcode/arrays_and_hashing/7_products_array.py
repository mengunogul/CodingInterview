"""
Question: https://neetcode.io/problems/products-of-array-discluding-self

This solution returns an array 'result' such that result[i] is equal to
the product of all the elements of nums except nums[i].
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Compute the product of all elements except self using prefix and postfix products.

        :param nums: List of integers.
        :return: List where each index i contains the product of all numbers in nums except nums[i].
        """
        n = len(nums)
        result: List[int] = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


if __name__ == "__main__":
    sol = Solution()
    test_input = [1, 2, 4, 6]
    result = sol.productExceptSelf(test_input)
    print("Products of array except self:", result)
