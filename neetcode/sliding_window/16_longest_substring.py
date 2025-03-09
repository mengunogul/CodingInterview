"""
Question: https://neetcode.io/problems/longest-substring-without-duplicates
"""

from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Args:
            s: Input string

        Returns:
            Length of the longest substring without repeating characters
        """
        if not s:
            return 0

        char_index: Dict[str, int] = {}  # Maps character to its most recent index
        max_length = 0
        window_start = 0

        for window_end, char in enumerate(s):
            # If we've seen this character before and it's within our current window
            if char in char_index and char_index[char] >= window_start:
                # Move window start to the position after the last occurrence
                window_start = char_index[char] + 1

            # Update the most recent position of this character
            char_index[char] = window_end

            # Update max_length if current window is longer
            current_length = window_end - window_start + 1
            max_length = max(max_length, current_length)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(f"Length of longest substring: {sol.lengthOfLongestSubstring(s)}")

    # Additional test cases
    test_cases = ["", "bbbbb", "pwwkew"]
    for test in test_cases:
        print(f'"{test}": {sol.lengthOfLongestSubstring(test)}')
