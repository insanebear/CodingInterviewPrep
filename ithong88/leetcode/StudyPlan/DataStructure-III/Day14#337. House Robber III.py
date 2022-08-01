# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return [0, 0]

            l = helper(node.left)
            r = helper(node.right)

            rob = node.val + l[1] + r[1]

            not_rob = max(l) + max(r)

            return [rob, not_rob]

        return max(helper(root))