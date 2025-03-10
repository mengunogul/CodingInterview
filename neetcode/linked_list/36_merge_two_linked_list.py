"""
Question: https://neetcode.io/problems/merge-two-sorted-lists
This module provides a solution for merging two sorted singly-linked lists.
It also includes helper functions to build and print linked lists.
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return it as a new sorted list.

        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        # Create a dummy node to simplify edge cases.
        merged_list = ListNode()
        tail = merged_list
        # Iterate as long as both lists have nodes.
        while list1 and list2:
            # Choose the node with the smaller value.
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Advance the tail pointer.
        # Append any remaining nodes from list1 or list2.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return merged_list.next


def build_linked_list(nums: List[int]) -> Optional[ListNode]:
    """
    Build a linked list from a list of integers.

    Args:
        nums (List[int]): The list of integers for the linked list.

    Returns:
        Optional[ListNode]: The head of the constructed linked list.
    """
    dummy = ListNode(0)
    cur = dummy
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


def print_linked_list(head: Optional[ListNode]) -> None:
    """
    Print the linked list nodes in order.

    Args:
        head (Optional[ListNode]): The head of the linked list.
    """
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))


if __name__ == "__main__":
    # Build the linked lists from arrays.
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 5])

    # Merge the two sorted linked lists.
    sol = Solution()
    merged = sol.mergeTwoLists(l1, l2)

    # Print the merged linked list.
    print_linked_list(merged)
