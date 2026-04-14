class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = [[] for x in range(numCourses)]

        for course, prereq in prerequisites:
            indegrees[course] += 1 
            adj[prereq].append(course)
        Q = deque()
        visited = set()
        for course in range(numCourses):
            if indegrees[course] == 0:
                Q.append(course)
        
        while Q: 
            nd = Q.pop()
            visited.add(nd)
            for neighbour in adj[nd]:
                indegrees[neighbour] -= 1
                if neighbour not in visited and indegrees[neighbour] <= 0:
                    Q.append(neighbour)
        return len(visited) == numCourses


        