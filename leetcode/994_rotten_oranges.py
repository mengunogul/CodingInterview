from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q: deque = deque()

        def bfs():
            max_min = 0
            while q:
                minute, row, col = q.popleft()
                if (row, col) in visited:
                    continue
                if row < 0 or row >= ROWS:
                    continue
                if col < 0 or col >= COLS:
                    continue
                if grid[row][col] == 0 or grid[row][col] == 2:
                    continue
                visited.add((row, col))
                grid[row][col] = 2
                max_min = max(max_min, minute)

                q.append((minute + 1, row + 1, col))
                q.append((minute + 1, row - 1, col))
                q.append((minute + 1, row, col + 1))
                q.append((minute + 1, row, col - 1))
            return max_min

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((1, row + 1, col))
                    q.append((1, row - 1, col))
                    q.append((1, row, col + 1))
                    q.append((1, row, col - 1))
        max_minutes = bfs()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return max_minutes
