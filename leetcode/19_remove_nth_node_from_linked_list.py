# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next  # type: ignore

        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next  # type: ignore

        if prev is not None:
            prev.next = slow.next  # type: ignore
            return head
        else:
            return slow.next  # type: ignore
