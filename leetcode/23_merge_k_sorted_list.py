import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur = dummy_head
        min_heap: list[int] = []
        for head in lists:
            while head:
                heapq.heappush(min_heap, head.val)
                head = head.next

        while min_heap:
            val = heapq.heappop(min_heap)
            cur.next = ListNode(val=val)
            cur = cur.next

        return dummy_head.next
