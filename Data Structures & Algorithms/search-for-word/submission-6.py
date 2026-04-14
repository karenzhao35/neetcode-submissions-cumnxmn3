class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
        ROWS, COLS = len(board), len(board[0])
        found = False
        def dfs(x, y, i, visited):
            nonlocal found
            
            if board[x][y] != word[i]:
                return
            if i == len(word)-1: 
                found = True
                return

            visited.add((x,y))
            print(board[x][y])
            for dx, dy in DIRS: 
                nx, ny = x+dx, y+dy
                if (nx,ny) not in visited and nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS: 
                    dfs(nx, ny, i+1, visited)
            visited.remove((x,y))
                    
            
        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(x,y,0,set())
                if found: return True
        return found
