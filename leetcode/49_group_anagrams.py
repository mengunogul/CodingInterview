from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        clusters: dict[str, List[str]] = {}
        for string in strs:
            key = "".join(sorted(string))
            cluster = clusters.get(key, [])
            cluster.append(string)
            clusters[key] = cluster
        return list(clusters.values())
