"""
Question: https://neetcode.io/problems/rotting-fruit
"""

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue: deque = deque()
        fresh = 0

        def add_neighbor(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                grid[r][c] = 2  # Mark as rotten
                queue.append((r, c))
                return True
            return False

        # Initial setup
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if add_neighbor(r + 1, c):
                    fresh -= 1
                if add_neighbor(r - 1, c):
                    fresh -= 1
                if add_neighbor(r, c + 1):
                    fresh -= 1
                if add_neighbor(r, c - 1):
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
