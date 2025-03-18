from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        subseq = [words[0]]  # Start with the first word.
        current_group = groups[0]
        for word, group in zip(words[1:], groups[1:]):  # Iterate remaining pairs.
            if group != current_group:
                subseq.append(word)
                current_group = group
        return subseq


if __name__ == "__main__":
    words = ["a", "b", "c", "d"]
    groups = [1, 0, 1, 1]
    sol = Solution()
    print(sol.getLongestSubsequence(words, groups))
