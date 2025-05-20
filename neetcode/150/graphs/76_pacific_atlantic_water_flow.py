"""
Question: https://neetcode.io/problems/pacific-atlantic-water-flow
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac: set = set()
        atl: set = set()

        def dfs(r, c, visit, prev_height):
            if r < 0 or c < 0:
                return
            if r == ROWS or c == COLS:
                return
            if (r, c) in visit or heights[r][c] < prev_height:
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)

        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)

        intersect = pac.intersection(atl)
        return [list(loc) for loc in intersect]
