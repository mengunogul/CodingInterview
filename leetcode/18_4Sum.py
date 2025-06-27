from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        # pick first index a
        for a in range(n - 3):
            # skip duplicates for the first number
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            # pick second index b
            for b in range(a + 1, n - 2):
                # skip duplicates for the second number
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                # now use two pointers for the remaining two numbers
                left, right = b + 1, n - 1
                while left < right:
                    s = nums[a] + nums[b] + nums[left] + nums[right]
                    if s == target:
                        res.append([nums[a], nums[b], nums[left], nums[right]])

                        # move both pointers, but skip over duplicates
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return res
