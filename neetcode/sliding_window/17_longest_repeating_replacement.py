"""
Question: https://neetcode.io/problems/longest-repeating-substring-with-replacement

This module provides an optimized solution to find the length of the longest substring
that can be obtained by replacing at most k characters to make all characters identical.
It uses an incremental sliding window approach with O(n) time complexity.
"""

from typing import Dict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Determine the length of the longest substring achievable with at most k replacements
        so that every character in the substring is the same.

        :param s: The input string.
        :param k: Maximum number of allowed replacements.
        :return: Length of the longest valid substring.
        """
        window_start: int = 0
        max_length: int = 0
        max_freq: int = (
            0  # Frequency of the most common character in the current window
        )
        freq: Dict[str, int] = {}

        for window_end, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            # Update the count of the most frequent character in the window.
            max_freq = max(max_freq, freq[char])

            # Current window size minus count of most frequent character gives number of replacements needed.
            if (window_end - window_start + 1) - max_freq > k:
                # Shrink the window from the left if more than k replacements are needed.
                freq[s[window_start]] -= 1
                window_start += 1

            # Update maximum length of valid window.
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


if __name__ == "__main__":
    sol = Solution()
    test_string: str = "XYYX"
    k: int = 2
    result: int = sol.characterReplacement(test_string, k)
    print("Longest repeating substring with replacement length:", result)
