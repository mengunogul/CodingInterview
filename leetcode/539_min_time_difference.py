from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []

        for time in timePoints:
            hour, minute = time.split(":")
            total_min = (int(hour) * 60) + int(minute)
            minutes.append(total_min)

        minutes.sort()
        print(minutes)
        min_minutes = float("inf")  # type: ignore
        for first, second in zip(minutes[0:-1], minutes[1:]):
            diff = second - first
            min_minutes = min(min_minutes, diff)

        diff = 24 * 60 - (minutes[-1] - minutes[0])
        min_minutes = min(min_minutes, diff)

        return min_minutes  # type: ignore
