from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table: dict[int, int] = {}  # boundary → run-length
        maxlen = 0

        for num in set(nums):
            left_len = table.get(num - 1, 0)
            right_len = table.get(num + 1, 0)
            new_len = left_len + 1 + right_len

            # compute the new interval’s true endpoints
            start = num - left_len
            end = num + right_len

            # overwrite those two boundaries
            table[start] = new_len
            table[end] = new_len

            maxlen = max(maxlen, new_len)

        return maxlen
