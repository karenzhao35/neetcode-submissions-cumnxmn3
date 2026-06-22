class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        edges = {}

        for ui, vi, ti in times: 
            adj[ui].append(vi)
            edges[(ui,vi)] = ti
        
        q = [(0, k)]
        visited = set()

        while q:
            time, nd = heapq.heappop(q)
            if nd in visited: continue
            visited.add(nd)
            if len(visited) == n: return time

            for nei in adj[nd]:
                if nei not in visited: 
                    heapq.heappush(q,(time+edges[(nd,nei)], nei))
        return -1
