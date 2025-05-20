"""
Question: https://neetcode.io/problems/count-number-of-islands
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(row: int, col: int) -> None:
            if (
                row < 0
                or col < 0
                or row >= len(grid)
                or col >= len(grid[0])
                or grid[row][col] == "0"
            ):
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count


if __name__ == "__main__":
    grid = [
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    solution = Solution()
    print(solution.numIslands(grid))
