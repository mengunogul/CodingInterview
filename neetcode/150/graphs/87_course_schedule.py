"""
Question: https://neetcode.io/problems/course-schedule
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map: dict[int, List[int]] = {}

        for course, prerequisite in prerequisites:
            prereqs = prereq_map.get(course, [])
            prereqs.append(prerequisite)
            prereq_map[course] = prereqs

        visited = set()
        rec_stack = set()

        def dfs(course):
            if course in rec_stack:
                return True  # cycle detected
            if course in visited:
                return False
            rec_stack.add(course)
            for req in prereq_map.get(course, []):
                if dfs(req):
                    return True
            rec_stack.remove(course)
            visited.add(course)
            return False

        for course in list(prereq_map.keys()):
            if dfs(course):
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    numCourses = 2
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    print(sol.canFinish(numCourses, prerequisites))
