"""
Question: https://neetcode.io/problems/longest-increasing-subsequence
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo: dict[
            str, bool
        ] = {}  # Dictionary to cache computed results for substrings

        def dfs(string):
            # If result is already computed for the current substring, return it
            if string in memo:
                return memo[string]
            # Base case: when the string is empty, segmentation is successful
            if not string:
                memo[string] = True
                return True
            # Try every word in the dictionary as a potential prefix
            for word in wordDict:
                # If the current substring starts with the word
                if string[: len(word)] == word:
                    # Recursively check if the remainder of the string can be segmented
                    if dfs(string[len(word) :]):
                        memo[string] = True  # Cache the result as True
                        return True
            memo[string] = False  # Cache the result as False when segmentation fails
            return False

        return dfs(s)


if __name__ == "__main__":
    sol = Solution()
    s = "catsincars"  # Example string to segment
    wordDict = ["cats", "cat", "sin", "in", "car"]  # List of valid words
    print(sol.wordBreak(s, wordDict))
