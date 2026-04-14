class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        DIRECTIONS = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c,visited,prevHeight):
            if (r,c) in visited: return
            visited.add((r,c))
            for dx,dy in DIRECTIONS: 
                nx, ny = dx+r, dy+c
                if m > nx >= 0 and n > ny >= 0 and heights[nx][ny] >= prevHeight:
                    dfs(nx,ny,visited,heights[nx][ny])
        for c in range(n):
            dfs(0,c,pac,heights[0][c])
            dfs(m-1,c,atl,heights[m-1][c])
        for r in range(m):
            dfs(r,0,pac,heights[r][0])
            dfs(r,n-1,atl,heights[r][n-1])
        result = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl: result.append([r,c])
        return result