"""
Question: https://leetcode.com/problems/n-queens/description/
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Solve the N-Queen problem and return all solutions.
        Each solution is represented as a list of strings (board layout).

        :param n: The size of the board (n x n).
        :return: List of board solutions.
        """
        board = [["." for _ in range(n)] for _ in range(n)]
        self.sol: List[List[str]] = []
        self.backtracking(board, 0, n)
        return self.sol

    def is_valid(self, board: List[List[str]], row: int, col: int, n: int) -> bool:
        """
        Check if it's safe to place a queen at board[row][col].
        Only rows above the current row need to be checked.

        :param board: The current state of the board.
        :param row: Current row index.
        :param col: Current column index.
        :param n: Board size.
        :return: True if placement is valid; False otherwise.
        """
        # Check same column in previous rows.
        for i in range(row):
            if board[i][col] == "Q":
                return False
        # Check upper left diagonal.
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        # Check upper right diagonal.
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def backtracking(self, board: List[List[str]], row: int, n: int) -> None:
        """
        Place queens row by row using backtracking.
        When a solution is found, append the list of queen positions (1-indexed) to self.sol.

        :param board: The current board.
        :param row: The current row to fill.
        :param n: Board size.
        """
        if row == n:
            # Instead of a list of indices, extract each row as a string.
            solution = ["".join(r) for r in board]
            self.sol.append(solution)
            return

        for col in range(n):
            if self.is_valid(board, row, col, n):
                board[row][col] = "Q"
                self.backtracking(board, row + 1, n)
                board[row][col] = "."


if __name__ == "__main__":
    solver = Solution()
    answer = solver.solveNQueens(4)
    print(answer)
