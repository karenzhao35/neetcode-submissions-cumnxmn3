class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]: 
                    mem[i+1][j+1] = max(mem[i+1][j], mem[i][j]+1,mem[i][j+1])
                else: 
                    mem[i+1][j+1] = max(mem[i+1][j], mem[i][j],mem[i][j+1])
                # print(i+1,j+1,mem[i][j-1],mem)
        print(mem)
        return mem[len(text2)][len(text1)]
