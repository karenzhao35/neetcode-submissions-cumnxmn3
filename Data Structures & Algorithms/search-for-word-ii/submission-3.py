import copy

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words: 
            curr = root
            for c in word: 
                curr = curr.setNext(c)
            curr.setEnd(True)

        DIRS = [(0,1), (1,0), (-1,0), (0,-1)]
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(x,y,visited,word,trie):
            nonlocal res
            # if (x,y) in visited: return 
            visited.add((x,y))
            c = board[x][y]
            if c not in trie.children: return 
            trie = trie.children[c]
            if trie.is_end: res.append(word+c)
            # print(word+c)

            for dx, dy in DIRS: 
                nx, ny = dx+x, dy+y
                if nx < ROWS and nx >= 0 and ny < COLS and ny >= 0 and (nx,ny) not in visited:
                    dfs(nx,ny, visited, word+c,trie)
                    visited.remove((nx,ny))
        
        for x in range(ROWS):
            for y in range(COLS):
                dfs(x,y, set(),"",root)
        return list(set(res))
            

class TrieNode: 
    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end
    def setNext(self, c):
        if c not in self.children:
            node = TrieNode()
            self.children[c] = node
        else: 
            node = self.children[c]
        return node
    def setEnd(self, is_end):
        self.is_end = is_end
