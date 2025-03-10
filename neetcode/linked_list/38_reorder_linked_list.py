"""
Question: https://neetcode.io/problems/reorder-linked-list
This module reorders a singly-linked list by interleaving nodes from the beginning and end.
The approach:
1. Find the middle of the list.
2. Reverse the second half.
3. Merge the two halves alternatingly.
"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.

        Args:
            val (int): The node's value.
            next (Optional[ListNode]): Pointer to the next node.
        """
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder the given linked list in-place by alternating nodes from the front and back.

        The reordering process involves three steps:
        1. Locate the middle of the list using slow and fast pointers.
        2. Reverse the second half of the list.
        3. Merge the first half with the reversed second half.

        Args:
            head (Optional[ListNode]): Head of the linked list.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next  # advance slow pointer by one.
            fast = fast.next.next  # advance fast pointer by two.

        # Step 2: Reverse the second half.
        reverse = slow.next  # Start of second half.
        prev = None
        slow.next = None  # Disconnect the first half from the second half.
        while reverse:
            next_node = reverse.next  # Store next node.
            reverse.next = prev  # Reverse the pointer.
            prev = reverse  # Move prev forward.
            reverse = next_node  # Move to the next node.

        # Step 3: Merge the two halves.
        first, second = head, prev
        while second:
            temp1 = first.next  # Store next node in first half.
            temp2 = second.next  # Store next node in second half.
            first.next = second  # Link current node of first half to current node of second half.
            second.next = (
                temp1  # Link current node of second half to next node of first half.
            )
            first = temp1  # Move first pointer.
            second = temp2  # Move second pointer.


def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """
    Convert a list of integers to a linked list.

    Args:
        arr (List[int]): List of integer values.

    Returns:
        Optional[ListNode]: Head of the resulting linked list.
    """
    dummy = ListNode(0)
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Convert a linked list to a list of integers.

    Args:
        head (Optional[ListNode]): Head of the linked list.

    Returns:
        List[int]: List of node values.
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    # Build a linked list from an array.
    head_vals = [2, 4, 6, 8]
    head = list_to_linked_list(head_vals)
    sol = Solution()
    # Reorder the linked list.
    sol.reorderList(head)
    # Convert the reordered linked list back to list and print.
    print(linked_list_to_list(head))
