from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: dict[int, List[int]] = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        cache: dict[int, bool] = {}

        def dfs(course, prereqs):
            if course in prereqs:
                return False

            prereqs.add(course)
            for prereq in graph[course]:
                if cache.get(prereq, False):
                    continue
                if not dfs(prereq, prereqs):
                    return False
            cache[course] = True
            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        return True
