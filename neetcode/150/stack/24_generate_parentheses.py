"""
Question: https://neetcode.io/problems/generate-parentheses

This module generates all combinations of well-formed parentheses using backtracking.
It avoids duplicate combinations by strictly controlling the addition of opening and closing brackets.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all valid combinations of n pairs of parentheses.

        :param n: The number of pairs of parentheses.
        :return: List of valid parentheses combinations.
        """
        result: List[str] = []  # List to store the final valid combinations

        def backtrack(open_count: int, close_count: int, current: str) -> None:
            """
            Recursively build valid parentheses combinations using backtracking.

            :param open_count: Current count of '(' used.
            :param close_count: Current count of ')' used.
            :param current: The current parentheses string being formed.
            """
            # If the current combination is complete, add it to result.
            if open_count == n and close_count == n:
                result.append(current)
                return

            # If we can add an opening bracket, do it.
            if open_count < n:
                backtrack(open_count + 1, close_count, current + "(")

            # If we can add a closing bracket, and it would not lead to an invalid combination, do it.
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current + ")")

        # Start the backtracking with no brackets added.
        backtrack(0, 0, "")
        return result


if __name__ == "__main__":
    sol = Solution()
    result = sol.generateParenthesis(3)
    print("Generated parentheses combinations:", result)
