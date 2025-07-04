from collections import Counter
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float(inf)
        min_left = 0

        target = Counter(t)
        window_state: dict[str, int] = {}

        remaining = len(target)
        left = 0

        for right, ch in enumerate(s):
            window_state[ch] = window_state.get(ch, 0) + 1
            if ch in target and window_state[ch] == target[ch]:
                remaining -= 1

            while remaining == 0 and left <= right:
                window_size = right - left + 1

                if window_size < min_len:
                    min_len = window_size
                    min_left = left

                # remove the leftmost char
                delete_char = s[left]
                window_state[delete_char] -= 1
                if (
                    delete_char in target
                    and window_state[delete_char] < target[delete_char]
                ):
                    remaining += 1
                left += 1

        return "" if min_len == inf else s[min_left : min_left + min_len]  # type: ignore
