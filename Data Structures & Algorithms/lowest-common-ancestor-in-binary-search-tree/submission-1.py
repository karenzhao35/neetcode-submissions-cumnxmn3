# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = None
        def traverseChildren(node): 
            nonlocal ancestor
            if not node: return None
            if node.val == p.val or node.val == q.val: 
                if traverseChildren(node.left) or traverseChildren(node.right):
                    ancestor = node
                return node
            elif traverseChildren(node.left) and traverseChildren(node.right):
                ancestor = node
            
            return traverseChildren(node.left) or traverseChildren(node.right)
        traverseChildren(root)
        return ancestor
