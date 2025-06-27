from collections import Counter
import math
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ones = freq.get(1, 0)
        max_len = ones if ones % 2 != 0 else ones - 1

        unique_nums = sorted(list(freq.keys()), reverse=True)
        for num in unique_nums:
            count = 1
            cur_num = math.sqrt(num)
            while cur_num in freq and freq.get(cur_num, 0) >= 2 and cur_num != 1:  # type: ignore
                cur_num = math.sqrt(cur_num)
                count += 2
            max_len = max(max_len, count)
        return max_len
