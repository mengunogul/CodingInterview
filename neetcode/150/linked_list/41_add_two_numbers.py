"""
Question: https://neetcode.io/problems/add-two-numbers
This module adds two numbers represented by linked lists and returns the sum as a linked list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the result list.
        dummy_head = ListNode(0)
        sum_list = dummy_head

        carry = 0
        # Process each node for both lists and the carry.
        while l1 or l2 or carry:
            # Get current digit values, using 0 if a list is exhausted.
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            addition = l1_val + l2_val + carry
            # Update carry for the next addition.
            carry = addition // 10
            # Debug: Print current carry value (consider removing in production).
            print(carry)  # Debug output
            # Create a new node with the digit result of the addition.
            sum_list.next = ListNode(addition % 10)

            # Move to the next nodes in the input lists, if available.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # Advance the pointer in the result list.
            sum_list = sum_list.next
        return dummy_head.next
