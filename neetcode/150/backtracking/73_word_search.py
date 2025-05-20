"""
Question: https://neetcode.io/problems/search-for-word
This module solves the Word Search problem where we need to find if a word exists in a 2D board.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Determine if a word exists in a 2D board by searching adjacent characters.

        Args:
            board (List[List[str]]): 2D board of characters.
            word (str): Word to search for.

        Returns:
            bool: True if the word can be constructed from adjacent letters, False otherwise.
        """
        # Define the four possible directions to move on the board
        directions = {
            "D": (0, 1),  # Down
            "U": (0, -1),  # Up
            "R": (1, 0),  # Right
            "L": (-1, 0),
        }  # Left
        res = []  # Store paths that form the word

        def backtrack(
            iter: int, row: int, col: int, string: str, path: List[List[int]] = []
        ):
            """
            Recursive backtracking function to explore possible paths.

            Args:
                iter (int): Current position in the word.
                row (int): Current row in the board.
                col (int): Current column in the board.
                string (str): Current constructed string.
                path (List[List[int]]): Path taken so far to construct the string.
            """
            # Base Cases
            # Case 1: Check if we've found the word
            print(string, string == word)
            if string == word:
                res.append(path)
                return
            # Case 2: Check if we've gone beyond the word length
            if iter + 1 >= len(word):
                return

            # Explore in all four directions
            for x, y in directions.values():
                # Calculate the new position
                new_row = row + x
                new_col = col + y

                # Case 1: Skip if already visited in the current path
                if [new_row, new_col] in path:
                    continue
                # Case 2: Skip if out of bounds (row check)
                if new_row < 0 or new_row >= len(board):
                    continue
                # Case 3: Skip if out of bounds (column check)
                if new_col < 0 or new_col >= len(board[row]):
                    continue

                # Continue exploring with updated path and string
                backtrack(
                    iter + 1,
                    new_row,
                    new_col,
                    string + board[new_row][new_col],
                    path + [[new_row, new_col]],
                )

        # Try each cell as a starting point if it matches the first letter
        for r, row in enumerate(board):
            for c, _ in enumerate(row):
                if board[r][c] == word[0] and not res:
                    backtrack(0, r, c, word[0], [[r, c]])

        # Return True if any path was found, False otherwise
        return True if res else False


if __name__ == "__main__":
    solver = Solution()
    # Sample test case
    board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]]
    word = "CAT"
    print(solver.exist(board, word))
