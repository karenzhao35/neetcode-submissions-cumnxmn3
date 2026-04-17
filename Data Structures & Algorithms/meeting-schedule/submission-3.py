"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sort = sorted(intervals, key=lambda x: x.start)
        prev = Interval(0,0)
        for interval in sort:
            s, e = interval.start, interval.end

            if s < prev.end:
                return False
            prev = interval
        return True
