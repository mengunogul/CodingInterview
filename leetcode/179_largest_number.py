from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def custom_cmp(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        s = list(map(str, nums))

        s.sort(key=cmp_to_key(custom_cmp))

        if s[0] == "0":
            return "0"

        return "".join(s)
