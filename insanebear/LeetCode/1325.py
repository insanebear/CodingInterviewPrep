# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def isLeaf(node):
            if node.left == None and node.right == None:
                return True
            return False
        
        def dfs(node):
            if isLeaf(node): # until meets leaf
                return
            
            # visit children then cut them if they are leaves
            if node.left != None:
                dfs(node.left)
                
                if isLeaf(node.left) and node.left.val == target:
                    node.left = None
            
            if node.right != None:
                dfs(node.right)
                
                if isLeaf(node.right) and node.right.val == target:
                    node.right = None
        
        dfs(root)
        
        return None if isLeaf(root) and root.val == target else root