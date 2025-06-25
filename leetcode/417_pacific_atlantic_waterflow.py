from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pacific_reach: set[tuple[int, int]] = set()
        atlantic_reach: set[tuple[int, int]] = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int, visited: set, prev_height: int):
            # bounds check
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            # already visited or height too low to flow “uphill”
            if (r, c) in visited or heights[r][c] < prev_height:
                return

            visited.add((r, c))
            # explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visited, heights[r][c])

        # run DFS from left and right rows
        for c in range(COLS):
            dfs(0, c, pacific_reach, float("-inf"))  # type: ignore
            dfs(ROWS - 1, c, atlantic_reach, float("-inf"))  # type: ignore
        # run DFS from top and bottom rows
        for r in range(ROWS):
            dfs(r, 0, pacific_reach, float("-inf"))  # type: ignore
            dfs(r, COLS - 1, atlantic_reach, float("-inf"))  # type: ignore

        # intersection = cells that can reach both
        result = pacific_reach & atlantic_reach
        # sort for consistent order
        return [[r, c] for r, c in sorted(result)]
