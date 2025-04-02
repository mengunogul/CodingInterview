"""
Question: https://neetcode.io/problems/islands-and-treasure
"""

from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue: deque = deque()

        def add_neighbors(r: int, c: int) -> None:
            # Check boundaries
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            # If it's an obstacle or already visited, skip it
            if grid[r][c] == -1 or (r, c) in visited:
                return
            queue.append((r, c))
            visited.add((r, c))

        # Start BFS from all cells with value 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        dist = 0
        # Process cells level by level to ensure correct distance assignment
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                add_neighbors(r + 1, c)
                add_neighbors(r - 1, c)
                add_neighbors(r, c + 1)
                add_neighbors(r, c - 1)
            dist += 1
        return grid
