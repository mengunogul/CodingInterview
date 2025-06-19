from typing import List


class Solution:
    def maxCompatibilitySum(
        self, students: List[List[int]], mentors: List[List[int]]
    ) -> int:
        """
        Calculate the maximum compatibility sum using backtracking.
        """
        n = len(students)
        self.max_score = 0

        def backtrack(student_idx: int, used_mentors: set, current_score: int):
            if student_idx == n:
                self.max_score = max(self.max_score, current_score)
                return

            for mentor_idx, mentor in enumerate(mentors):
                if mentor_idx not in used_mentors:
                    compatibility = self.calculate_compatibility_score(
                        students[student_idx], mentor
                    )
                    used_mentors.add(mentor_idx)
                    backtrack(
                        student_idx + 1, used_mentors, current_score + compatibility
                    )
                    used_mentors.remove(mentor_idx)

        backtrack(0, set(), 0)
        return self.max_score

    def calculate_compatibility_score(
        self, student: List[int], mentor: List[int]
    ) -> int:
        """
        Calculate compatibility score based on matching answers.
        """
        return sum(s == m for s, m in zip(student, mentor))


if __name__ == "__main__":
    sol = Solution()
    students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
    mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    print(sol.maxCompatibilitySum(students, mentors))
