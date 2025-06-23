from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq: dict[int, List[int]] = {i: [] for i in range(len(nums) + 1)}

        for key, val in count.items():
            freq[val].append(key)

        res = []
        for i in range(len(nums), -1, -1):
            for key in freq[i]:
                res.append(key)
                if len(res) == k:
                    return res
        return res
