from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums1):
            mapping[num] = i

        res = [-1] * len(nums1)
        stack: List[int] = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                j = stack.pop()
                key = nums2[j]
                if key in mapping:
                    res[mapping[key]] = nums2[i]
            stack.append(i)
        return res
