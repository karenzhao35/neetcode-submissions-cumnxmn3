class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inorder = [0] * numCourses
        adj = defaultdict(list)
        result = []

        for to, fro in prerequisites:
            adj[fro].append(to)
            inorder[to] += 1 
        Q = deque([])
        visited = set()

        for node, ins in enumerate(inorder):
            if ins == 0: 
                Q.append(node)
        while Q: 
            curr = Q.popleft()
            result.append(curr)

            for nxt in adj[curr]:
                inorder[nxt] -= 1
                if inorder[nxt] == 0:
                    Q.append(nxt)
        print(result)
        if len(result) == numCourses: return result
        return []