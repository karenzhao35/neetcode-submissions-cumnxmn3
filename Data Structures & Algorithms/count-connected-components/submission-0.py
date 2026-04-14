class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for x in range(n)]
        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        visited = set([0])
        Q = deque([0])
        res = 1

        while Q: 
            nd = Q.pop()
            visited.add(nd)
            for neighbour in adj[nd]:
                if neighbour not in visited: 
                    Q.append(neighbour)
            if not Q and len(visited) < n:
                res += 1
                diff = set(list(range(n))) - visited
                if diff: 
                    e = diff.pop()
                    Q.append(e)
                    visited.add(e)
        return res