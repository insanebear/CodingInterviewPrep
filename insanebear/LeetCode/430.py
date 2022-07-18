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
        cur = head
        
        while cur:
            if cur.child:
                # add rest of nodes to the end of the child list
                rest = cur.next
                child = cur.child
                
                while child.next:
                    child = child.next
                
                # make double link child end <> rest
                if rest:
                    child.next = rest
                    rest.prev = child
                
                # recursively flatten child level
                cur.next = self.flatten(cur.child)
                
                # make double link cur <> child
                cur.child.prev = cur
                cur.child = None
            
            cur = cur.next
        
        return head
        