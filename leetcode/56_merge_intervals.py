from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        idx = 0
        while idx < len(intervals) - 1:
            curr_start, curr_end = intervals[idx]
            next_start, next_end = intervals[idx + 1]

            if curr_end >= next_start:
                intervals.pop(idx + 1)
                intervals[idx][1] = max(curr_end, next_end)
                continue
            idx += 1

        return intervals
