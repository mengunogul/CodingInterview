from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        twenty_four_hours = 24 * 60
        for time in timePoints:
            hour, minute = time.split(":")
            total_mins = (int(hour) * 60) + int(minute)
            minutes.append(total_mins)

        minutes.sort()
        diff = [second - first for first, second in zip(minutes[:-1], minutes[1:])]
        boundry = twenty_four_hours - (minutes[-1] - minutes[0])
        diff.append(boundry)
        return min(diff)
