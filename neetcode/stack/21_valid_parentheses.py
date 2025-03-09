"""
Question: https://neetcode.io/problems/validate-parentheses

This module provides a solution for validating whether a string of brackets is properly nested.
A string is considered valid if every opening bracket has a corresponding closing bracket of the same type,
and the brackets are closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string s is a valid sequence of brackets.

        The function uses a stack to keep track of opening brackets. When a closing bracket is encountered,
        it checks whether it matches the most recent opening bracket. If it does not match or the stack is empty
        when a closing bracket appears, the string is invalid.

        :param s: A string containing bracket characters.
        :return: True if the string is valid; otherwise, False.
        """
        # Define mapping from opening to closing brackets.
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []  # Stack to hold opening brackets.

        for ch in s:
            if ch in brackets:
                # If an opening bracket is encountered, push it onto the stack.
                stack.append(ch)
            else:
                # If a closing bracket is encountered, ensure there is a matching opening bracket.
                if not stack:  # No opener available.
                    return False
                last = stack.pop()
                if ch != brackets[last]:
                    # The closing bracket does not match the most recent opening bracket.
                    return False
        # If stack is empty, all brackets were matched; otherwise, some openings remain unmatched.
        return len(stack) == 0


if __name__ == "__main__":
    # Example usage:
    sol = Solution()
    test_str = "([{}])"
    result = sol.isValid(test_str)
    print("Is valid parentheses?:", result)
