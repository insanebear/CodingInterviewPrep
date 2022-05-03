"""
<https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/>
"""

import collections


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


## Using Level-order traversal
class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        node_queue = collections.deque([root, None])

        while node_queue:
            node = node_queue.popleft()
            if node is None:
                if node_queue:
                    node_queue.append(None)
                    continue
                else:
                    break

            node.next = node_queue[0]
            if node.left is not None:
                node_queue.append(node.left)
            if node.right is not None:
                node_queue.append(node.right)

        return root


## Optimize space complexity to O(1)
class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        curr_level = root
        leftmost = None
        next_level = None

        while curr_level is not None:

            def update_node(next_node, leftmost, next_level):
                if leftmost is None:
                    leftmost = next_node
                    next_level = leftmost
                else:
                    next_level.next = next_node
                    next_level = next_node
                return leftmost, next_level

            if curr_level.left is not None:
                leftmost, next_level = update_node(
                    curr_level.left, leftmost, next_level
                )

            if curr_level.right is not None:
                leftmost, next_level = update_node(
                    curr_level.right, leftmost, next_level
                )

            curr_level = curr_level.next
            if curr_level is None:
                curr_level = leftmost
                leftmost = None
                next_level = None

        return root
