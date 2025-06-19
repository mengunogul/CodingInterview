from typing import List


class Solution:
    """
    Provides methods to generate letter combinations for a given phone number.
    """

    digits_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generate all possible letter combinations from input digits using backtracking.

        :param digits: A string containing digits from 2-9 inclusive.
        :return: A list of all letter combinations mapping to the digits.
        """
        self.combinations: List[str] = []
        if len(digits) == 0:
            return []
        self.backtrack(0, [], digits)
        return self.combinations

    def backtrack(self, index: int, path: List[str], digits: str) -> None:
        """
        Recursively build letter combinations.

        :param index: The current index in the digits string.
        :param path: The current combination being built.
        :param digits: The input digits string.
        """
        # base case: found a complete combination
        if index == len(digits):
            self.combinations.append("".join(path))
            return None
        # iterate for each possible letter of the current digit
        for letter in self.digits_to_letters[digits[index]]:
            path.append(letter)  # choose the letter
            self.backtrack(index + 1, path, digits)  # explore further
            path.pop()  # backtrack


if __name__ == "__main__":
    sol = Solution()
    ans = sol.letterCombinations("23")
    assert ans == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
