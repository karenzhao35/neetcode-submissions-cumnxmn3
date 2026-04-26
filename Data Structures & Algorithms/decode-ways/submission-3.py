class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        result = 0
        def is_valid(s):
            if s[0] == "0": return False
            n = int(s)
            return 1 <= n and 26 >= n
        def search(i):
            nonlocal result
            if i in memo:
                result += memo[i]
                return 
            if i == len(s): 
                result += 1
                return
            rsf = 0 
            if is_valid(s[i]):
                search(i+1)
            if i+1 < len(s) and is_valid(s[i]+s[i+1]):
                search(i+2)
            memo[i] = result
            return rsf
        search(0)
        print(memo)
        return result