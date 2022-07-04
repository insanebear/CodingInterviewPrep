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
        # empty input
        if not head:
            return None
        
        # create new nodes and connect them with next pointer
        cur = head
        copied_head = Node(cur.val, None, None)
        copied_cur = copied_head
        
        while cur.next:
            new_next_node = Node(cur.next.val, None, None)
            copied_cur.next = new_next_node
            copied_cur = copied_cur.next
            cur = cur.next
        
        cur = head
        copied_cur = copied_head
        while cur:
            # find random
            node = cur.random
            p1 = head
            p2 = copied_head
            while p1 is not node:
                p1 = p1.next
                p2 = p2.next
            
            # set new random
            copied_cur.random = p2
            
            # move pointer
            cur = cur.next
            copied_cur = copied_cur.next
            
        
        return copied_head