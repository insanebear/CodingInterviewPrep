# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        
        def dfs(node):
            nonlocal max_sum # to update max_sum
            
            if node == None:
                return 0
            
            # calculate left, right subtree
            # if root, right and left are positive, max_sum would be root+right+left.
            # if the partial sum is negative, it won't be chosen. (= 0)
            
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)
            
            potential_max = node.val + left_sum + right_sum
            
            # update max_sum
            max_sum = max(max_sum, potential_max)
            
            
            # to use the sum value in upper level
            # 'node' must be considered, and then either left or right
            return node.val + max(left_sum, right_sum)
        
        dfs(root)
        
        return max_sum