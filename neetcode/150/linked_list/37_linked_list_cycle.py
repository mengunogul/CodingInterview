"""
Question: https://neetcode.io/problems/linked-list-cycle-detection
This module implements cycle detection in a singly-linked list using Floyd's Tortoise and Hare algorithm.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.

        Args:
            val (int): The node's value.
            next (Optional[ListNode]): The next node in the linked list.
        """
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if the linked list has a cycle using Floyd's algorithm.

        Args:
            head (Optional[ListNode]): Head of the linked list.

        Returns:
            bool: True if a cycle exists, otherwise False.
        """
        fast = head  # Fast pointer moves two steps at a time.
        slow = head  # Slow pointer moves one step at a time.

        # Iterate while there are nodes to visit.
        while fast and fast.next:
            fast = fast.next.next  # Advance fast pointer by two steps.
            # Advance slow pointer by one step.
            slow = slow.next  # type: ignore
            # If both pointers meet, a cycle exists.
            if fast == slow:
                return True
        # If no cycle, return False.
        return False
