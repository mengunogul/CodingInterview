from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)
        count = 0
        repeat_flag = 0
        for word in freq:
            # case 1: repetitive chars
            if word[0] == word[1]:
                quotinent, remainder = divmod(freq[word], 2)
                count += quotinent * 2
                if remainder:
                    repeat_flag = 1
            # case 2: mirrored chars
            else:
                count += min(freq.get(word[::-1], 0), freq.get(word, 0))

        return (count + repeat_flag) * 2
