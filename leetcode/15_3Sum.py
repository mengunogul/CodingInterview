from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        results = set()
        visited = set()
        for i in range(len(nums)):
            complements = set()
            if nums[i] in visited:
                continue
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                if nums[j] in complements:
                    res = tuple(sorted([nums[i], complement, nums[j]]))
                    results.add(res)
                complements.add(complement)
            visited.add(nums[i])
        return [list(res) for res in results]
