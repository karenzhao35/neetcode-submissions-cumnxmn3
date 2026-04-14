class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        al = [[] for _ in range(numCourses)]
        indegree = defaultdict(int)
        Q = deque()
        visited = set()
        for c, prereq in prerequisites:
            al[prereq].append(c)
            indegree[c] += 1
            indegree[prereq] += 0
        for nd in indegree: 
            if indegree[nd] == 0: 
                Q.append(nd)
        while Q: 
            node = Q.popleft()
            visited.add(node)
            for nxt in al[node]:
                indegree[nxt] -= 1
                if nxt not in visited and indegree[nxt] == 0: 
                    Q.append(nxt)
        return len(visited) == len(indegree)