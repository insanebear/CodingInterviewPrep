"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        cur = head
        if cur is None:
            return None
        while cur.next is not None or len(stack) != 0 or cur.child is not None:
            
            if cur.child is not None:
                if cur.next is not None:
                    stack.append(cur.next)
                cur.next = cur.child
                prev = cur
                cur.child = None
                cur = cur.next
                cur.prev = prev
            elif cur.child is None and cur.next is not None:
                cur = cur.next
            elif cur.child is None and cur.next is None and len(stack) != 0:
                cur.next = stack.pop()
                cur.next.prev = cur
        
        cur = head
        
        return head