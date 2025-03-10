"""
Question: https://neetcode.io/problems/remove-node-from-end-of-linked-list
This module removes the nth node from the end of a singly-linked list.
It uses a dummy node and a two-pointer technique to efficiently locate and remove the target node.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.

        Args:
            val (int): The value stored in the node.
            next (Optional[ListNode]): Pointer to the next node.
        """
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the linked list.

        This method uses a dummy node to simplify edge cases and two pointers (fast and slow)
        to locate the target node for removal. The fast pointer is advanced n steps ahead,
        then both pointers are advanced until the fast pointer reaches the end.
        The slow pointer will then be just before the node to remove.

        Args:
            head (Optional[ListNode]): The head of the linked list.
            n (int): The position (from the end) of the node to remove.

        Returns:
            Optional[ListNode]: The head of the modified linked list.
        """
        # Create a dummy node that points to the head to simplify removal logic.
        dummy = ListNode(0, head)
        left = dummy  # Slow pointer
        right = head  # Fast pointer

        # Advance the fast pointer n steps ahead.
        while n > 0:
            right = right.next  # type: ignore
            n -= 1

        # Move both pointers until right reaches the end.
        while right:
            left = left.next
            right = right.next

        # left.next is the node to remove, so bypass it.
        left.next = left.next.next
        return dummy.next
