class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key= lambda x: x[0])
        ps, pe = intervals[0]
        res = 0 
        for s, e in intervals[1:]: 

            if pe > s: 
                if pe > e: 
                    ps, pe = s, e
                res += 1
            else: 
                ps, pe = s, e
            
        return res