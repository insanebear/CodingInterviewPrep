# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        return recur(root, subRoot)
    
def recur(root, subRoot):
    isF1 = False
    isF2 = False
    isT = False
    if root == None:
        return False
    if root.val == subRoot.val:
        isT=recur2(root, subRoot)
    
    isF1 = recur(root.left, subRoot)
    # print(isF1)
    isF2 = recur(root.right, subRoot)
    # print(isF2)
    if isT or isF1 or isF2:
        return True
    else:
        return False
    
def recur2(indexRoot, indexSub):
    isF1 = True
    isF2 = True
    if (indexRoot is None) and (indexSub is not None):
        return False
    elif (indexRoot is not None) and (indexSub is None):
        return False
    elif (indexRoot is not None) and (indexSub is not None):
        if indexRoot.val != indexSub.val:
            return False
        isF1 = recur2(indexRoot.left, indexSub.left)
        isF2 = recur2(indexRoot.right, indexSub.right)
    else:
        # print('True')
        return True
    
    if not isF1 or not isF2:
        return False
    else:
        return True
        
        