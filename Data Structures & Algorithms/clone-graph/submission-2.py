"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        res = Node(node.val)
        visited = {}
        def clone(curr, nd, visited): 
            visited[nd.val] = curr
            for nei in nd.neighbors: 
                nxt = Node(nei.val) 
                if nei.val not in visited:
                    clone(nxt, nei, visited)
                    visited[nei.val] = nxt
                    curr.neighbors.append(nxt)
                else: 
                    curr.neighbors.append(visited[nei.val])
        visited[node.val] = res
        clone(res, node, visited)

        return res
