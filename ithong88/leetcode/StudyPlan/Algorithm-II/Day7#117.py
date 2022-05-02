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
        cur = root
        # next_level = cur.left
        prev = None
        queue = []
        cur_level_cnt = 1
        next_level_cnt = 0
        if root:
            queue.append(root)
        cnt = 0

        while queue:
            cur = queue.pop(0)
            cnt += 1
            if prev:
                prev.next = cur
            if cnt == cur_level_cnt:
                prev = None
            else:
                prev = cur

            if cur.left is not None:
                queue.append(cur.left)
                next_level_cnt += 1
            if cur.right is not None:
                queue.append(cur.right)
                next_level_cnt += 1
            if cnt == cur_level_cnt:
                cur_level_cnt = next_level_cnt
                next_level_cnt = 0
                cnt = 0

        return root
