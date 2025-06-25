from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_freq = Counter(s1)
        window_freq: dict[str, int] = {}
        left = 0
        for right in range(len(s2)):
            cur_char_freq = window_freq.get(s2[right], 0) + 1
            window_freq[s2[right]] = cur_char_freq

            target_char_freq = target_freq.get(s2[right], 0)
            while cur_char_freq > target_char_freq and left <= right:
                window_freq[s2[left]] -= 1
                if window_freq[s2[left]] == 0:
                    del window_freq[s2[left]]
                cur_char_freq = window_freq.get(s2[right], 0)
                left += 1

            print(left, right, window_freq)
            if target_freq == window_freq:
                return True
        return False
