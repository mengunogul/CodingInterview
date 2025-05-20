"""
Question:
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        not_surrounded = set()

        def bfs(r, c):
            if r < 0 or c < 0:
                return
            if r == ROWS or c == COLS:
                return
            if board[r][c] == "X" or (r, c) in not_surrounded:
                return
            not_surrounded.add((r, c))
            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)

        for r in range(ROWS):
            bfs(r, 0)
            bfs(r, COLS - 1)

        for c in range(COLS):
            bfs(0, c)
            bfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in not_surrounded:
                    board[r][c] = "X"
