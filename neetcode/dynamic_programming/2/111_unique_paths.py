"""
Question: https://neetcode.io/problems/count-paths
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    m = 3
    n = 6
    print(sol.uniquePaths(m, n))
