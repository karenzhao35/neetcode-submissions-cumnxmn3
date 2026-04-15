class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        window = set()
        n = len(s)-1
        res = 0 
        while r <= n and l <= n:
            if s[r] in window:
                while l <= n and s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                l += 1
            window.add(s[r])
            r += 1 
            res = max(res, len(window))
            
            print(window)
        return res