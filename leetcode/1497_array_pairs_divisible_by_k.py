from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = Counter([el % k for el in arr])

        if freq.get(0, 0) % 2 != 0:
            return False
        if 0 in freq:
            del freq[0]

        for key in freq:
            target = k - key
            if freq[key] != freq[target]:
                return False
        return True
