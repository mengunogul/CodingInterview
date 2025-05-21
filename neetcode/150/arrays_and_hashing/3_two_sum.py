"""
Question: https://neetcode.io/problems/two-integer-sum
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compelements: dict[int, int] = {}
        for index, val in enumerate(nums):
            complement = target - val
            if complement in compelements:
                return [compelements[complement], index]
            elif val in compelements:
                pass
            else:
                compelements[val] = index
        return []


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print("Resulting indices:", result)
