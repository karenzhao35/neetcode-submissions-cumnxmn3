class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def is_valid(s):
            if s[0] == "0": return False
            n = int(s)
            return 1 <= n and 26 >= n
        def search(i):
            if i in memo:
                return memo[i]
            if i == len(s): 
                return 1
            rsf = 0 
            if is_valid(s[i]):
                rsf += search(i+1)
            if i+1 < len(s) and is_valid(s[i]+s[i+1]):
                rsf += search(i+2)
            memo[i] = rsf
            return rsf
        
        return search(0)