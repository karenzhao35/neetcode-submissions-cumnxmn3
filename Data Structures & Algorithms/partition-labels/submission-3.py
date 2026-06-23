class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i, c in enumerate(s):
            last[c] = i 

        l, r = 0, 0
        result = []
        latest = last[s[0]]
        for i, c in enumerate(s):
            if i == latest: 
                result.append(i-l+1)
                l = i+1
                latest = last[s[i+1]] if i+1 < len(s) else -1
            latest = max(latest, last[c])

        return result
            
