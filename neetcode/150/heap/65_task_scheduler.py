"""
Question: https://neetcode.io/problems/task-scheduling
"""

from typing import List
import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Build frequency map of tasks
        taks_freq = Counter(tasks)
        # Create a max-heap from task frequencies (using negative counts)
        maxHeap = [-cnt for cnt in taks_freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        # Queue to hold tasks during their cooldown period; each element is [remaining_count, available_time]
        q = deque()  # type: ignore
        # Process tasks until both heap and waiting queue are empty
        while maxHeap or q:
            time += 1  # Increment time at each unit
            # If heap is empty, jump ahead to the time when the next task becomes available
            if not maxHeap:
                # Debug: No tasks ready, jumping to next available task time
                time = q[0][1]
            else:
                # Pop the most frequent task (simulation)
                cnt = 1 + heapq.heappop(
                    maxHeap
                )  # Increment since counts are stored as negatives
                # If there are still pending executions, add task to the waiting queue with its next available time
                if cnt:
                    # Debug: Append task to the queue with cooldown finish time (current time + n)
                    q.append([cnt, time + n])
            # Check if any task in the waiting queue is ready to be scheduled again
            if q and q[0][1] == time:
                # Debug: Task cooldown finished; push back to heap
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


if __name__ == "__main__":
    solution = Solution()
    tasks = ["X", "X", "Y", "Y"]
    n = 2
    result = solution.leastInterval(tasks, n)
    print("Least interval:", result)
