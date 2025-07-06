from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        n = len(stack)

        operations = (n - 1) // 2

        cur = head
        while operations:
            node = stack.pop()
            temp = cur.next
            cur.next = node
            node.next = temp
            cur = temp
            operations -= 1
        if n % 2 == 1:
            cur.next = None
        else:
            cur.next.next = None
