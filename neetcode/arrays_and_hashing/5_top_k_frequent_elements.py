"""
Question: https://neetcode.io/problems/top-k-elements-in-list
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Return the k most frequent elements in nums.

        :param nums: List of integers.
        :param k: Number of top frequent elements to return.
        :return: List of k most frequent elements.
        """
        frequency = Counter(nums)
        return [num for num, _ in frequency.most_common(k)]


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = solution.topKFrequent(nums, k)
    print("Top k frequent elements:", result)
