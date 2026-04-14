class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        result = 0 
        def findIsland(x: int, y: int):
            if x-1 >= 0: 
                if grid[x-1][y] == "1" and (x-1,y) not in visited:
                    visited.add((x-1,y))
                    findIsland(x-1,y)
            if y-1 >= 0:
                if grid[x][y-1] == "1" and (x,y-1) not in visited:
                    visited.add((x,y-1))
                    findIsland(x,y-1)
            if x+1 < len(grid):
                if grid[x+1][y] == "1" and (x+1,y) not in visited:
                    visited.add((x+1,y))
                    findIsland(x+1,y)
            if y+1 < len(grid[0]):
                if grid[x][y+1] == "1" and (x,y+1) not in visited:
                    visited.add((x,y+1))
                    findIsland(x,y+1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "0":
                    continue
                elif (x,y) in visited:
                    continue
                else:
                    visited.add((x,y))
                    findIsland(x,y)
                    result += 1

        return result 