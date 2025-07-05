from typing import List
import random


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq: dict[str, int] = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        def quick_select(arr, k):
            pivot = random.choice(arr)
            left = [i for i in arr if i[0] < pivot[0]]
            equal = [i for i in arr if i[0] == pivot[0]]
            right = [i for i in arr if i[0] > pivot[0]]

            if len(right) >= k:
                return quick_select(right, k)
            elif len(right) + len(equal) >= k:
                return right + equal[: k - len(right)]
            else:
                return right + equal + quick_select(left, k - len(right) - len(equal))

        freq_list = [[count, word] for word, count in freq.items()]
        return [word for _, word in quick_select(freq_list, k)]
