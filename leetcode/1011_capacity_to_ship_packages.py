from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check_days(capacity):
            days_needed = 1
            capacity_left = capacity
            for weight in weights:
                if capacity_left >= weight:
                    capacity_left -= weight
                else:
                    days_needed += 1
                    capacity_left = capacity - weight
            return days_needed

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            cur = check_days(mid)

            if cur > days:
                left = mid + 1
            else:
                right = mid

        return left
