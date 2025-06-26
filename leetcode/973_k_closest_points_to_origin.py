import random
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[math.sqrt(x**2 + y**2), [x, y]] for x, y in points]

        def quick_select(arr, k):
            pivot = random.choice(arr)[0]
            less_than = [i for i in arr if i[0] < pivot]
            equal_to = [i for i in arr if i[0] == pivot]
            greater_than = [i for i in arr if i[0] > pivot]

            if k <= len(less_than):
                return quick_select(less_than, k)
            elif k <= len(less_than) + len(equal_to):
                return less_than + equal_to[: k - len(less_than)]
            else:
                return (
                    less_than
                    + equal_to
                    + quick_select(greater_than, k - len(less_than) - len(equal_to))
                )

        return [points for _, points in quick_select(distances, k)]
