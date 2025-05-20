"""
Question: https://neetcode.io/problems/maximum-product-subarray
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # initialize current max, min, and global maximum with the first element
        cur_max = cur_min = global_max = nums[0]

        # iterate through the array starting from index 1
        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max  # swap when negative

            # update the current max and min products
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            # update the global maximum product
            global_max = max(global_max, cur_max)

        return global_max


if __name__ == "__main__":
    sol = Solution()
    nums = [-2, -1]
    print(sol.maxProduct(nums))
