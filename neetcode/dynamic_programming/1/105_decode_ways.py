"""
Question: https://neetcode.io/problems/decode-ways
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """Return the number of ways to decode the given string s."""
        if not s:
            return 0
        n = len(s)
        # Initialize dp with (n+1) elements; dp[i] stores decoding ways for s[i:]
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        return dp[0]


if __name__ == "__main__":
    solution = Solution()
    s = "1012"
    print(solution.numDecodings(s))
