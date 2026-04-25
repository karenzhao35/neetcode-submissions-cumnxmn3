class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(x,y):
            grid[x][y] = "0"
            visited.add((x,y))
            for dx, dy in DIRS: 
                nx, ny = dx+x, dy+y
                if (nx,ny) not in visited and nx < ROWS and nx >= 0 and ny < COLS and ny >= 0 and grid[nx][ny]=="1":
                    dfs(nx,ny)

            
        result = 0 
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1": 
                    result += 1 
                    dfs(x,y)
        return result
