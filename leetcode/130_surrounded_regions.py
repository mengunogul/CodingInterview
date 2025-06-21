from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        dq: deque = deque()

        # Enqueue all 'O's on the border
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == "O":
                    dq.append((r, c))
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == "O":
                    dq.append((r, c))

        # Mark all border-connected 'O's as 'E' (escaped)
        while dq:
            r, c = dq.popleft()
            if board[r][c] != "O":
                continue
            board[r][c] = "E"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    dq.append((nr, nc))

        # Flip all remaining 'O's to 'X', and restore 'E' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"
