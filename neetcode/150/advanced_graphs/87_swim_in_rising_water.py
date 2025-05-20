"""
Question: https://neetcode.io/problems/swim-in-rising-water
"""

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()
        heap = [(grid[0][0], 0, 0)]
        while heap:
            cur_time, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            if (r, c) == (n - 1, m - 1):
                return cur_time
            visited.add((r, c))
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                    cost = max(cur_time, grid[nr][nc])
                    heapq.heappush(heap, (cost, nr, nc))
        return cur_time
