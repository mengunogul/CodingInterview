from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 0
        check = head
        while check:
            check = check.next
            length += 1

        slow = head
        fast = head

        it = k % length
        if it == 0:
            return head

        for _ in range(it):
            fast = fast.next  # type: ignore

        while fast.next:  # type: ignore
            slow = slow.next  # type: ignore
            fast = fast.next  # type: ignore

        temp = slow.next  # type: ignore
        slow.next = None  # type: ignore
        fast.next = head  # type: ignore

        return temp
