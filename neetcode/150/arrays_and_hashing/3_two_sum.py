"""
Question: https://neetcode.io/problems/two-integer-sum
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print("Resulting indices:", result)
