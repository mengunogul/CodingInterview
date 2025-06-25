class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freq_window: dict[str, int] = {}

        start = 0
        for end in range(len(s)):
            freq = freq_window.get(s[end], 0) + 1
            freq_window[s[end]] = freq

            length = end - start + 1
            diff = length - max(freq_window.values())
            if diff > k:
                freq_window[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)
        return max_len
