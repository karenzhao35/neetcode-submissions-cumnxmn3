class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_hash(num):
            if 0 <= num <= 2: return 0
            elif 3 <= num <= 5: return 1
            else: return 2
        horz = defaultdict(set)
        box = defaultdict(set)

        for x in range(9):
            vert = set()
            for y in range(9):
                num = board[x][y]
                if num != ".":
                    if (num in box[(get_hash(x),get_hash(y))] or
                    num in horz[y] or
                    num in vert): 
                        return False
                    box[(get_hash(x), get_hash(y))].add(num)
                    horz[y].add(num)
                    vert.add(num)

        return True
                    

        