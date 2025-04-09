"""
Question: https://neetcode.io/problems/reconstruct-flight-path
"""

from typing import List, Dict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph: Dict[str, List[str]] = {src: [] for src, dest in tickets}

        for src, dest in tickets:
            graph[src].append(dest)

        self.res: List[str] = []

        def dfs(src, adj, path):
            # Base Case
            if len(path) == len(tickets) + 1:
                self.res = path
                return True
            if src not in adj:
                return False

            for idx, dest in enumerate(adj[src]):
                adj[src].pop(idx)
                if dfs(dest, adj, path + [dest]):
                    return True
                adj[src].insert(idx, dest)
            return False

        dfs("JFK", graph, ["JFK"])
        return self.res


if __name__ == "__main__":
    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    sol = Solution()
    itinerary = sol.findItinerary(tickets)
    print(itinerary)
