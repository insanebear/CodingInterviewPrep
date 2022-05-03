"""
<https://leetcode.com/problems/subtree-of-another-tree/>
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isIdentical(self, lhs: Optional[TreeNode], rhs: Optional[TreeNode]) -> bool:
        if lhs is None and rhs is None:
            return True

        if lhs is None or rhs is None:
            return False

        if lhs.val != rhs.val:
            return False

        return self.isIdentical(lhs.left, rhs.left) and self.isIdentical(
            lhs.right, rhs.right
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None and root is None:
            return True
        if root is None:
            return False

        if root.val == subRoot.val:
            if self.isIdentical(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
