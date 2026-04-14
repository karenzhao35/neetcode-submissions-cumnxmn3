# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        s = deque([root])
        res = []
        while s: 

            for _ in range(len(s)):
                nd = s.popleft()
                if nd.left: s.append(nd.left)
                if nd.right: s.append(nd.right)

            res.append(nd.val)
        
        return res
