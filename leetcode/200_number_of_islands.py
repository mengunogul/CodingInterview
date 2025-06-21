from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= ROWS:
                return
            if col < 0 or col >= COLS:
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        num_islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_islands += 1
        return num_islands
