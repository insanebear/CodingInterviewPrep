# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathSum = -1000

        def recMaxPathSum(cur):
            nonlocal pathSum
            if cur is None:
                return 0

            left = max(recMaxPathSum(cur.left), 0)
            right = max(recMaxPathSum(cur.right), 0)
            localPathSum = cur.val + left + right
            pathSum = max(localPathSum, pathSum)

            return cur.val + max(left, right)

        recMaxPathSum(root)
        return pathSum