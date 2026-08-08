"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        sorted_intervals = sorted(intervals, key = lambda interval: interval.start)
        start, end = sorted_intervals[0].start, sorted_intervals[0].end
        n = len(sorted_intervals)
        for i in range(1, n):
            next_start, next_end = sorted_intervals[i].start, sorted_intervals[i].end
            if end > next_start:
                return False
            start, end = next_start, next_end
        return True


