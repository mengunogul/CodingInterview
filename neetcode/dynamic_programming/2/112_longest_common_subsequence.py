class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i = 0
        j = 0
        res = 0
        while i < len(text1) and j < len(text2):
            if text1[i] == text2[j]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    text1 = "cat"
    text2 = "crabt"
    print(sol.longestCommonSubsequence(text1, text2))
