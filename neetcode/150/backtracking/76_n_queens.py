"""
Question: https://neetcode.io/problems/n-queens
This module solves the N-Queens problem using backtracking.
We place one queen per row and check for safety (column and both diagonals) before placement.
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def is_safe(row: int, col: int) -> bool:
            # Check same column (only rows above need to be checked)
            for r in range(row):
                if board[r][col] == "Q":
                    return False
            # Check upper left diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            # Check upper right diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            return True

        def backtrack(row: int, num_queens: int) -> None:
            # If we've placed queens in all rows, record the solution.
            if row == n:
                if num_queens == n:
                    # Deep copy the board as a list of strings.
                    solution = ["".join(r) for r in board]
                    result.append(solution)
                return

            # Try placing a queen in each column of the current row.
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1, num_queens + 1)
                    board[row][col] = "."

        backtrack(0, 0)
        return result


if __name__ == "__main__":
    solver = Solution()
    n = 4
    print(solver.solveNQueens(n))
