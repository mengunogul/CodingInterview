from typing import List, Optional, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Modify board in-place to solve the Sudoku puzzle using backtracking.
        """
        self.backtracking(board)

    def find_empty_mrv(
        self, board: List[List[str]]
    ) -> Optional[Tuple[int, int, List[str]]]:
        """
        Find the empty cell with the minimum number of valid candidates.

        :param board: The current Sudoku board.
        :return: Tuple (row, col, candidates) of the empty cell with the fewest options,
                or None if the board is complete.
        """
        best: Optional[Tuple[int, int, List[str]]] = None
        min_options = 10  # More than maximum possible candidates (9)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    # Compute valid candidates for this cell
                    candidates = [
                        str(d)
                        for d in range(1, 10)
                        if self.is_valid(board, row, col, str(d))
                    ]
                    if len(candidates) < min_options:
                        min_options = len(candidates)
                        best = (row, col, candidates)
                        if min_options == 1:
                            return best
        return best

    def is_valid(
        self, board: List[List[str]], row: int, col: int, candidate: str
    ) -> bool:
        """
        Check if placing candidate at board[row][col] is valid.

        :param board: The current board.
        :param row: Row index.
        :param col: Column index.
        :param candidate: Candidate digit as a string.
        :return: True if valid, False otherwise.
        """
        # Check row
        if candidate in board[row]:
            return False

        # Check column
        if candidate in [board[r][col] for r in range(9)]:
            return False

        # Check 3x3 sub-box
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if board[r][c] == candidate:
                    return False
        return True

    def backtracking(self, board: List[List[str]]) -> bool:
        """
        Use backtracking with the MRV heuristic to fill the board.

        :param board: The Sudoku board.
        :return: True if a solution is found, False otherwise.
        """
        empty = self.find_empty_mrv(board)
        if not empty:
            return True  # Board complete

        row, col, candidates = empty
        for candidate in candidates:
            board[row][col] = candidate
            if self.backtracking(board):
                return True
            board[row][col] = "."  # backtrack
        return False


if __name__ == "__main__":
    solver = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solver.solveSudoku(board)
    assert board == [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
