class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_max = 0
        left = 0
        visited: set[str] = set()
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[i])
            len_max = max(len_max, i - left + 1)
        return len_max
