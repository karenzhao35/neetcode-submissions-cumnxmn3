# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        Q = deque([root])
        visited = set([root])

        while Q:
            res.append([])
            for _ in range(len(Q)):
                nd = Q.popleft()
                res[-1].append(nd.val)
                if nd.left: Q.append(nd.left)
                if nd.right: Q.append(nd.right)
        return res
