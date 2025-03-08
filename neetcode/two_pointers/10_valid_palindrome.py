"""
Question: https://neetcode.io/problems/is-palindrome

This module provides a solution to check if a string is a palindrome,
considering only alphanumeric characters and ignoring cases.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determine if the given string is a palindrome.

        The function filters out non-alphanumeric characters, converts the string
        to lowercase, and compares it with its reverse.

        :param s: The input string.
        :return: True if the string is a palindrome; False otherwise.
        """
        # Filter and convert to lowercase.
        cleaned: str = "".join(ch.lower() for ch in s if ch.isalnum())
        # Check if cleaned string equals its reverse.
        return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sample: str = "Was it a car or a cat I saw?"
    sol = Solution()
    result: bool = sol.isPalindrome(sample)
    print("Result:", result)
