class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [(0, x) for x in range(numCourses)]
        adj = [[] for x in range(numCourses)]

        for course, prereq in prerequisites:
            indegrees[course] = (indegrees[course][0]+1, course)
            adj[prereq].append(course)
        init = indegrees.copy()
        heapq.heapify(init)
        print(init)
        degree,nd = heapq.heappop(init)
        print(init)
        if degree == 0: Q = deque([(degree,nd)])
        else: return False
        visited = set([nd])
        print(indegrees)
        while Q: 
            _, nd = Q.pop()
            visited.add(nd)
            for neighbour in adj[nd]:
                indegree, _ = indegrees[neighbour]
                indegrees[neighbour] = (indegree-1, neighbour)
                if neighbour not in visited and indegree-1 <= 0:
                    Q.append((0, neighbour))
            
            if not Q and len(visited) < numCourses:
                for x in range(numCourses): 
                    if x not in visited and indegrees[x][0] <= 0:
                        Q.append((0,x))
        print(len(visited))
        print(visited)
        return len(visited) == numCourses


        