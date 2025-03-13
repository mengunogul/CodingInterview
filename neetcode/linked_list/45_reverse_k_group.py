"""
Module implementing reverse nodes in k-group in a linked list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    """
    Class for a node in a singly-linked list.

    Attributes:
        val (int): The value stored in the node.
        next (ListNode): The reference to the next node.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Provides a method to reverse nodes in groups of k.
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses the nodes of a linked list in groups of k.

        Args:
            head (ListNode): Head of the linked list.
            k (int): Size of each group to reverse.

        Returns:
            ListNode: New head of the modified list.
        """
        dummy = ListNode(0, head)
        groupPrev = dummy

        # Process the linked list in groups of k.
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:  # Less than k nodes remain.
                break
            groupNext = kth.next

            # Reverse nodes within the current k-group.
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Reconnect the reversed group with the previous part.
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        """
        Returns the k-th node from the starting node.

        Args:
            curr (ListNode): The starting node.
            k (int): The number of steps to move forward.

        Returns:
            ListNode: The k-th node if found, else None.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


if __name__ == "__main__":
    # Create linked list from [1, 2, 3, 4, 5]
    nodes = [ListNode(val) for val in [1, 2, 3, 4, 5]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    # Reverse nodes in groups with k=3.
    sol = Solution()
    new_head = sol.reverseKGroup(head, 3)

    # Traverse and print the resulting list.
    result = []
    current = new_head
    while current:
        result.append(current.val)
        current = current.next
    print(result)
