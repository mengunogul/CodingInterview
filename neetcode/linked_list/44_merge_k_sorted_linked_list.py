"""
Question: https://neetcode.io/problems/merge-k-sorted-linked-lists
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge k sorted linked lists into a single sorted linked list.

        Args:
            lists (List[Optional[ListNode]]): A list containing the head nodes of k sorted linked lists.

        Returns:
            Optional[ListNode]: The head node of the merged sorted linked list.
        """
        # Create a dummy node to simplify list merging.
        dummy_head = ListNode()
        merge = dummy_head

        # Continue iterating until all lists are completely traversed.
        while any(node is not None for node in lists):
            min_index = -1
            min_value = float("inf")
            # Identify the smallest current node among the lists.
            for idx, node in enumerate(lists):
                if node is not None and node.val < min_value:
                    min_value = node.val
                    min_index = idx

            # Append the smallest node’s value to the merged list.
            merge.next = ListNode(min_value)
            merge = merge.next

            # Move to the next node in the list that provided the smallest node.
            lists[min_index] = lists[min_index].next  # type: ignore

        return dummy_head.next
