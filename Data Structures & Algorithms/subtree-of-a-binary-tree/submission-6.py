# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        check = self.sameTree(root, subRoot)
        if check: return True
        if not root or not subRoot: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, root, subRoot):
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        return root.val == subRoot.val and self.sameTree(root.right, subRoot.right) and self.sameTree(root.left, subRoot.left)