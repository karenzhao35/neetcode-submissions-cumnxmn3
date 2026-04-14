class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        N, M = len(matrix[0]), len(matrix)

        for y in range(len(matrix)):
            rep = False
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    matrix[0][x] = 2**32
                    rep = True
            
            if rep and y == 0:
                for i in range(len(matrix[0])):
                    if matrix[0][i] != 2**32: matrix[0][i] = 0
            elif rep: matrix[y] = [0] * N
        # print(matrix)
        for x in range(len(matrix[0])):
            if matrix[0][x] == 2**32:
                for y in range(len(matrix)):
                    matrix[y][x] = 0

