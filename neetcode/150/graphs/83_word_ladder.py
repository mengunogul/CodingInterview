"""
Question: https://neetcode.io/problems/word-ladder
"""

from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Returns the number of steps in the shortest transformation sequence from beginWord to endWord,
        where adjacent words differ by exactly one letter. Returns 0 if no such transformation exists.
        """

        def is_adjacent(word1: str, word2: str) -> bool:
            # Check if two words differ by exactly one letter.
            return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([beginWord])
        steps = 1
        while queue:
            for _ in range(len(queue)):
                current_word = queue.popleft()
                if current_word == endWord:
                    return steps
                # Iterate over a snapshot of word_set to find valid neighbors.
                for neighbor in list(word_set):
                    if is_adjacent(current_word, neighbor):
                        queue.append(neighbor)
                        word_set.remove(neighbor)
            steps += 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    beginWord = "cat"
    endWord = "sag"
    wordList = ["bat", "bag", "sag", "dag", "dot"]
    result = sol.ladderLength(beginWord, endWord, wordList)
    print(result)
