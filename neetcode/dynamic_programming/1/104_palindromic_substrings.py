"""
Question: Count palindromic substrings in a given string.
"""


class Solution:
    def count_substrings(self, s: str) -> int:
        """Return the count of palindromic substrings in s."""
        count = 0
        for i in range(len(s)):
            count += self._expand_around_center(s, i, i)  # odd-length palindromes
            count += self._expand_around_center(s, i, i + 1)  # even-length palindromes
        return count

    def _expand_around_center(self, s: str, left: int, right: int) -> int:
        """Return the number of palindromic substrings expanding from the center."""
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    test_string = "aaa"
    print(solution.count_substrings(test_string))
