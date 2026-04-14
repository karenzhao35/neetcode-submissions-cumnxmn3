import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window 
        window = []
        lst1 = list(s1)
        for c in s2:
            if c in lst1: 
                window.append(c)
            else: 
                window = []

            if len(window) == len(lst1):
                if collections.Counter(lst1) == collections.Counter(window):
                    return True
                else: 
                    window.pop(0)
        return False