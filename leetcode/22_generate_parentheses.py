from typing import List


class Solution:
    """
    Generates all combinations of well-formed parentheses given n pairs.
    """

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all valid combinations of n pairs of parentheses.

        :param n: Number of pairs of parentheses.
        :return: List of valid parentheses combinations.
        """
        if n == 0:
            return []
        self.combinations: List[str] = []
        self.backtrack(n, "", 0, 0)
        return self.combinations

    def backtrack(self, n: int, comb: str, num_open: int, num_close: int) -> None:
        """
        Recursively build valid parentheses combinations.

        :param n: Total number of pairs.
        :param comb: Current combination being built.
        :param num_open: Count of open parentheses in comb.
        :param num_close: Count of close parentheses in comb.
        """
        total_length = 2 * n  # Total length when combination is complete
        if len(comb) == total_length:
            self.combinations.append(comb)
            return
        # Option to add an open parenthesis if not exceeded n
        if num_open < n:
            self.backtrack(n, comb + "(", num_open + 1, num_close)
        # Option to add a close parenthesis if valid (more opens than closes)
        if num_open > num_close:
            self.backtrack(n, comb + ")", num_open, num_close + 1)


if __name__ == "__main__":
    # test
    solution = Solution()
    answer = solution.generateParenthesis(3)
    print(answer)
    assert answer == ["((()))", "(()())", "(())()", "()(())", "()()()"]
