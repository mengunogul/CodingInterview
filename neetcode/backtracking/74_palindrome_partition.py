"""
Question: https://neetcode.io/problems/palindrome-partitioning
This module partitions a string into all possible palindrome substrings using a split/no-split approach.
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Partition a string into all possible palindrome substrings.

        Args:
            s (str): Input string to partition

        Returns:
            List[List[str]]: All possible palindrome partitioning results
        """
        result = []

        def is_palindrome(string: str) -> bool:
            """Check if a string is a palindrome."""
            return string == string[::-1]

        def backtrack(start: int, partition: List[str]) -> None:
            """
            Backtracking function using split/no-split strategy.

            Args:
                start (int): Current index to consider for splitting
                partition (List[str]): Current partition being built
            """
            # If we've processed the entire string, check if all substrings are palindromes
            if start >= len(s):
                if all(is_palindrome(part) for part in partition):
                    result.append(partition[:])
                return

            # Option 1: Don't split at this index - extend the last substring
            if partition:
                # Save the last part
                last_part = partition[-1]
                # Extend the last part with current character
                partition[-1] = last_part + s[start]
                backtrack(start + 1, partition)
                # Restore for backtracking
                partition[-1] = last_part

            # Option 2: Split at this index - create a new substring
            partition.append(s[start])
            backtrack(start + 1, partition)
            partition.pop()  # Remove for backtracking

        backtrack(0, [])
        return result


if __name__ == "__main__":
    solver = Solution()
    s = "aab"
    print(solver.partition(s))
