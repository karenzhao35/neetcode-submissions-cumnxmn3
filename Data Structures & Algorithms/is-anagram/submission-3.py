class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = set(s), set(t)

        c1 = set(list(s.count(x) for x in s))
        c2 = set(list(t.count(x) for x in t))
        return s1 == s2 and c1 == c2