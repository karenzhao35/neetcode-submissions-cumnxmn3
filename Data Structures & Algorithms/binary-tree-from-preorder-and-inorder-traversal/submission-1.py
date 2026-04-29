# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None

        root = TreeNode(val=preorder[0])
        i = 0
        while i < len(inorder):
            if inorder[i] == preorder[0]: break
            i+=1
        # print(preorder[1:i+1], inorder[:i])
        # print(preorder[i+1:], inorder[i+1:])
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root