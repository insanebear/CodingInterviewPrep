"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        root.next = Node(0,None,None,None)
        q = deque()
        nodes = []
        bfs(root, q, nodes)
        level = 0
        prev = root
        
        for node in nodes:
            # print(node.val)
            if level == node.next.val:
                prev.next = node
                prev = node
            else:
                prev.next = None
                level = level+1
                prev = node
        if len(nodes) > 0: 
            nodes[len(nodes)-1].next = None
        else:
            root.next = None
        return root                     

def bfs(node, q, nodes):
    if node == None:
        return;
    if node.left != None:
        node.left.next = Node(0,None,None,None)
        node.left.next.val = node.next.val + 1
        q.append(node.left)
        nodes.append(node.left)
    if node.right != None:
        node.right.next = Node(0,None,None,None)
        node.right.next.val = node.next.val + 1
        q.append(node.right)
        nodes.append(node.right)
    if len(q) == 0:
        return;
    bfs(q.popleft(), q , nodes)
