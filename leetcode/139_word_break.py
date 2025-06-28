from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        dp.append(True)

        for start in range(len(s) - 1, -1, -1):
            for word in wordDict:
                end = start + len(word)
                if s[start:end] == word and dp[end]:
                    print(start, end, s[start:end], dp)
                    dp[start] = dp[end]
        return dp[0]
