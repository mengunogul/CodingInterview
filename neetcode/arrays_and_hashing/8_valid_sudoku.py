"""
Question: https://neetcode.io/problems/valid-sudoku

This solution checks each row, column, and 3x3 sub-grid using sets to ensure
there are no duplicate digits.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.

        :param board: 9x9 grid representing the board with digits or '.'.
        :return: True if board is valid, False otherwise.
        """
        # Check rows
        for row in board:
            seen = set()
            for char in row:
                if char != ".":
                    if char in seen:
                        return False
                    seen.add(char)

        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):  # type: ignore
                char = board[row][col]  # type: ignore
                if char != ".":
                    if char in seen:
                        return False
                    seen.add(char)

        # Check 3x3 sub-boxes
        for block_row in range(3):
            for block_col in range(3):
                seen = set()
                for i in range(block_row * 3, block_row * 3 + 3):
                    for j in range(block_col * 3, block_col * 3 + 3):
                        char = board[i][j]
                        if char != ".":
                            if char in seen:
                                return False
                            seen.add(char)
        return True


if __name__ == "__main__":
    # Test sample board
    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solution = Solution()
    if solution.isValidSudoku(board):
        print("Board is valid")
    else:
        print("Board is invalid")
