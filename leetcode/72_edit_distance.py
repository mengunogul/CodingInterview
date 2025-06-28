class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS = len(word1) + 1
        COLS = len(word2) + 1

        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for i in range(ROWS):
            dp[i][0] = i
        for j in range(COLS):
            dp[0][j] = j

        for row in range(1, ROWS):
            for col in range(1, COLS):
                cost = 0 if word1[row - 1] == word2[col - 1] else 1
                dp[row][col] = min(
                    dp[row - 1][col] + 1,
                    dp[row][col - 1] + 1,
                    dp[row - 1][col - 1] + cost,
                )
        return dp[ROWS - 1][COLS - 1]
