"""
Question: https://neetcode.io/problems/combinations-of-a-phone-number
This module solves the Letter Combinations of a Phone Number problem.
It generates all possible letter combinations that can be formed by pressing the given digits on a phone keypad.
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generate all possible letter combinations from a string of digits.

        Args:
            digits (str): A string containing digits 2-9.

        Returns:
            List[str]: A list of all possible letter combinations.
        """
        # Handle edge case: empty input
        if not digits:
            return []

        # Dictionary mapping digits to their corresponding letters on a phone keypad
        phone_keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(index: int, combination: List[str]) -> None:
            """
            Backtracking function to build combinations recursively.

            Args:
                index (int): Current index in the digits string.
                combination (List[str]): Current combination being built.
            """
            # Base case: If we've processed all digits, add the combination to the result
            if index == len(digits):
                result.append("".join(combination))
                return

            # For each letter corresponding to the current digit, explore further
            current_digit = digits[index]
            for letter in phone_keys[current_digit]:
                # Add letter to the current combination
                combination.append(letter)
                # Move to the next digit
                backtrack(index + 1, combination)
                # Backtrack: remove the letter to try other possibilities
                combination.pop()

        # Start backtracking with empty combination from the first digit
        backtrack(0, [])
        return result


if __name__ == "__main__":
    solver = Solution()
    digits = "34"
    print(
        solver.letterCombinations(digits)
    )  # Test with '34', which should give combinations of 'def' and 'ghi'
