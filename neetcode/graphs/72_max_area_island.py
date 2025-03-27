"""
Questions: https://neetcode.io/problems/max-area-of-island
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        self.area = 0

        def dfs(row: int, col: int, area: int) -> None:
            if (
                row < 0
                or col < 0
                or row >= len(grid)
                or col >= len(grid[0])
                or grid[row][col] == 0
            ):
                return
            self.area += 1
            self.max_area = max(self.area, self.max_area)
            grid[row][col] = 0
            dfs(row + 1, col, self.area)  # down
            dfs(row, col + 1, self.area)  # right
            dfs(row, col - 1, self.area)  # left
            dfs(row - 1, col, self.area)  # up

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j, self.area)

        return self.max_area


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    solution = Solution()
    print(solution.maxAreaOfIsland(grid))
