"""
Question: https://neetcode.io/problems/reverse-a-linked-list
This module provides a solution for reversing a singly-linked list.
It includes helper functions to build and print a linked list.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.

        Args:
            val (int): The value of the node.
            next (ListNode, optional): Pointer to the next node.
        """
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly-linked list.

        Args:
            head (Optional[ListNode]): Head of the original linked list.

        Returns:
            Optional[ListNode]: Head of the reversed linked list.
        """
        prev = None
        curr = head
        # Iterate over the list and reverse the links.
        while curr:
            temp = curr.next  # Temporarily store the next node.
            curr.next = prev  # Reverse the current node's pointer.
            prev = curr  # Move prev to current node.
            curr = temp  # Advance to the next node.
        return prev


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Build a linked list from a list of integer values.

    Args:
        values (List[int]): List of values to create nodes.

    Returns:
        Optional[ListNode]: Head of the newly created linked list.
    """
    dummy = ListNode()  # Dummy head to ease list creation.
    curr = dummy
    for val in values:
        # Append each value as a new node to the list.
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linked_list(head: Optional[ListNode]) -> None:
    """
    Print the linked list in a readable format.

    Args:
        head (Optional[ListNode]): Head of the linked list to print.
    """
    curr = head
    vals = []
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print("[" + ", ".join(vals) + "]")


if __name__ == "__main__":
    # Build linked list from a list of values.
    head = build_linked_list([0, 1, 2, 3])
    sol = Solution()
    # Reverse the linked list.
    reversed_head = sol.reverseList(head)
    # Print the reversed linked list.
    print_linked_list(reversed_head)
