class Solution:
    """
    A class for finding the longest palindromic substring in a given string.
    """

    def longestPalindrome(self, s: str) -> str:
        """
        Returns the longest palindromic substring in s.
        """
        if not s:
            return ""
        longest = ""
        for i in range(len(s)):
            odd_palindrome = self._expand_from_center(i, i, s)
            even_palindrome = self._expand_from_center(i, i + 1, s)
            if len(odd_palindrome) >= len(longest):
                longest = odd_palindrome
            if len(even_palindrome) >= len(longest):
                longest = even_palindrome
        return longest

    def _expand_from_center(self, left: int, right: int, s: str) -> str:
        """
        Expands around a center and returns the palindromic substring.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]


if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    print(solution.longestPalindrome(s))
