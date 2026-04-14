class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "[": "]", "{": "}"}
        stack = []
        opening = True
        for c in s: 
            print(stack)
            if c in d: 
                stack.append(c)
            elif not stack:
                return False
            elif c == d[stack[-1]]: 
                stack.pop()
            else: 
                return False
            
        return not stack