class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # connected graph with no cyclesp
        adj = [[] for _ in range(n)]
        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set([0])
        def dfs(nd, prev, visited): 
            visited.add(nd)
            res = True
            for neighbour in adj[nd]:
                if neighbour != prev and neighbour in visited: 
                    return False
                if neighbour not in visited: 
                    res = res and dfs(neighbour, nd, visited)
            return res
        return dfs(0, -1, visited) and len(visited) == n
                
