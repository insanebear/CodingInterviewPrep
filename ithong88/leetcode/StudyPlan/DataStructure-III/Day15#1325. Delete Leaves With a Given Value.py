# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def recRemoveLeafNodes(parent, cur, target, direction):
            if cur is None:
                return
            recRemoveLeafNodes(cur, cur.left, target, "left")
            recRemoveLeafNodes(cur, cur.right, target, "right")

            if cur.left is None and cur.right is None and cur.val == target:
                if direction == "left":
                    parent.left = None
                elif direction == "right":
                    parent.right = None

        recRemoveLeafNodes(root, root.left, target, "left")
        recRemoveLeafNodes(root, root.right, target, "right")

        if root.left is None and root.right is None and root.val == target:
            root = None

        return root
