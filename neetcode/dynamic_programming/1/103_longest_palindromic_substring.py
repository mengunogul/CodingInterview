"""
Question: https://neetcode.io/problems/longest-palindromic-substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Return the longest palindromic substring in s using center expansion."""
        if not s:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self._expand_from_center(s, i, i)
            len2 = self._expand_from_center(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start : end + 1]

    def _expand_from_center(self, s: str, left: int, right: int) -> int:
        """Expand around the center and return the length of the palindrome."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == "__main__":
    solution = Solution()
    s = "a"
    print(solution.longestPalindrome(s))
