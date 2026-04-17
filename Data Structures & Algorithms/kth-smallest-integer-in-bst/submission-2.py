# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def search(node, i):   
            if node.left: 
                i, res = search(node.left, i)
                if res != None: return (i, res)
            i+=1
            if i == k: return (i, node.val)
            if node.right:
                return search(node.right, i)
            return (i, None)
        return search(root, 0)[1]
    