"""
Question: https://neetcode.io/problems/copy-linked-list-with-random-pointer
This module creates a deep copy of a linked list where each node has an additional random pointer.
It uses a defaultdict to automatically create new nodes for missing key references.
"""

from typing import Optional, DefaultDict, List
from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        """
        Initialize a new Node.

        Args:
            x (int): The node's value.
            next (Optional[Node], optional): Pointer to the next node in the linked list.
            random (Optional[Node], optional): Pointer to a random node in the linked list.
        """
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Create a deep copy of a linked list that includes random pointers.

        Args:
            head (Optional[Node]): The head of the original linked list.

        Returns:
            Optional[Node]: The head of the deep copied linked list.
        """
        # Create a DefaultDict mapping original nodes to their clones.
        # For any missing key, it creates a new Node with a default value of 0.
        to_copy: DefaultDict[Optional[Node], Node] = defaultdict(lambda: Node(0))
        # Map None to None for convenience.
        to_copy[None] = None  # type: ignore

        cur = head
        while cur:
            # Copy the current node's value.
            to_copy[cur].val = cur.val
            # Link the next pointer of the current copy to the clone of cur.next.
            to_copy[cur].next = to_copy[cur.next]
            # Link the random pointer of the current copy to the clone of cur.random.
            to_copy[cur].random = to_copy[cur.random]
            cur = cur.next
        return to_copy[head]


def create_linked_list(input_list: List[List[Optional[int]]]) -> Optional[Node]:
    """
    Create a linked list with random pointers from the given input list.
    Each element in input_list is in the form [val, random_index].

    Args:
        input_list (List[List[Optional[int]]]): Input list of [val, random_index] pairs.

    Returns:
        Optional[Node]: The head of the created linked list.
    """
    if not input_list:
        return None

    # First pass: create all nodes.
    nodes: List[Node] = []
    for val, _ in input_list:
        nodes.append(Node(val))  # type: ignore

    # Second pass: connect next pointers.
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Third pass: connect random pointers.
    for i, (_, random_index) in enumerate(input_list):
        if random_index is not None:
            nodes[i].random = nodes[random_index]
        else:
            nodes[i].random = None
    return nodes[0]


def print_linked_list(head: Optional[Node]) -> None:
    """
    Print the linked list with random pointers in a readable format.
    Each node is displayed as [value, random_node_index].

    Args:
        head (Optional[Node]): The head of the linked list.
    """
    result = []
    node_map = {}  # Map each node id to its position.

    # First pass: map nodes to positions.
    pos = 0
    curr = head
    while curr:
        node_map[id(curr)] = pos
        curr = curr.next
        pos += 1

    # Second pass: build result.
    curr = head
    while curr:
        random_pos = node_map.get(id(curr.random)) if curr.random else None
        result.append([curr.val, random_pos])
        curr = curr.next

    print(result)


if __name__ == "__main__":
    solver = Solution()
    # Create test case: Each entry is [node value, random pointer index]
    head = [[3, None], [7, 3], [4, 0], [5, 1]]
    head = create_linked_list(head)  # type: ignore
    copied = solver.copyRandomList(head)  # type: ignore

    print("Original:")
    print_linked_list(head)  # type: ignore
    print("Copy:")
    print_linked_list(copied)
