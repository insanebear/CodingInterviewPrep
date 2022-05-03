"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = []
        q.append((root, 0))
        
        while q:
            elem = q.pop(0)
            node, depth = elem[0], elem[1]
            
            if q and q[0][1] == depth:
                node.next = q[0][0]
            
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        
        return root
