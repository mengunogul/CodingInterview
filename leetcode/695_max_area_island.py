from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            area = 0
            q: deque = deque()
            q.append((r, c))
            while q:
                row, col = q.popleft()
                if row < 0 or row >= ROWS:
                    continue
                if col < 0 or col >= COLS:
                    continue
                if grid[row][col] == 0:
                    continue
                area += 1
                grid[row][col] = 0

                q.append((row + 1, col))
                q.append((row - 1, col))
                q.append((row, col + 1))
                q.append((row, col - 1))
            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        return max_area
