"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        prev = head
        cur = head.next
        new_head = Node(head.val, None, None)
        new_cur = new_head

        while cur != None:
            new_cur.next = Node(cur.val, None, None)
            prev = prev.next
            cur = cur.next
            new_cur = new_cur.next

        # find
        ori_node = head
        new_node = new_head
        while ori_node is not None:
            target = ori_node.random
            cur = head
            new_random = new_head
            if target is not None:
                while cur is not None:
                    if cur == target:
                        new_node.random = new_random
                        break
                    cur = cur.next
                    new_random = new_random.next
            ori_node = ori_node.next
            new_node = new_node.next

        return new_head
