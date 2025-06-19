class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Check if s is empty; an empty string is always a subsequence
        if not s:
            return True
        s_index = 0
        # Iterate through t to sequentially match characters from s
        for ch in t:
            if s[s_index] == ch:
                s_index += 1
            # If all characters in s have been matched, return True
            if s_index == len(s):
                return True
        # Return False if not all characters in s could be matched in t
        return False


if __name__ == "__main__":
    # Example usage: test the isSubsequence method with sample inputs
    s = "aec"
    t = "abcde"
    sol = Solution()
    print(sol.isSubsequence(s, t))
