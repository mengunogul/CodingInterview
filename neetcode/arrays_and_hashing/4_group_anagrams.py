"""
Question: https://neetcode.io/problems/anagram-groups
"""

from typing import List, Dict
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together from the input list.

        :param strs: List of strings.
        :return: List of groups of anagrams.
        """
        groups: Dict[str, List[str]] = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = sol.groupAnagrams(test_input)
    print("Grouped Anagrams:", output)
