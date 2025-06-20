from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res: List[List[int]] = []

        def backtrack(it, comb):
            if it == len(nums):
                self.res.append(comb)
                return

            for i in nums:
                if i not in comb:
                    comb.append(i)
                    backtrack(it + 1, comb[:])
                    comb.pop()

        backtrack(0, [])
        return self.res
