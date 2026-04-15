class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        Zi, Zj = 0, 0
        res = []
        i, j = 0,0 
        flag = False
        inc = True
        while i < M and j < N and i >= Zi and j >= Zj: 
            res.append(matrix[i][j])
            if flag: 
                if inc:
                    if i == M-1: 
                        flag = False
                        N -= 1
                        j = N-1
                        inc = False
                    else: i += 1
                else:
                    if i == Zi:
                        flag = False
                        Zj += 1
                        j = Zj
                        inc = True
                    else: i -= 1    
            else:
                if inc:
                    if j == N-1: 
                        flag = True
                        Zi += 1
                        i = Zi
                    else: j += 1
                else:
                    if j == Zj:
                        M -= 1
                        i = M-1
                        flag = True
                    else: j -= 1

        return res