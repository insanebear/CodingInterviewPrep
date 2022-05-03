# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node1, node2):
            if node1 is not None and node2 is not None and node1.val == node2.val:
                return check(node1.left, node2.left) and check(node1.right, node2.right)
            elif node1 is None and node2 is None:
                return True
            else:
                return False

        if root == None:
            return False
        else:
            return check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
