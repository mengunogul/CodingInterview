class Solution:
    def minChanges(self, s: str) -> int:
        irregular = 0
        for i in range(0, len(s) - 1, 2):
            if s[i] != s[i + 1]:
                irregular += 1
        return irregular
