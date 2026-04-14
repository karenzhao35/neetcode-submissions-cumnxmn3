class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        curr_start, curr_end = intervals[0][0], intervals[0][1]
        res = []
        for start, end in intervals: 
            if curr_start <= start <= curr_end:
                curr_end = max(end, curr_end)
            else: 
                res.append([curr_start, curr_end])
                curr_start, curr_end = start, end
        res.append([curr_start, curr_end])
        return res
