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

        interval_list = []
        for interval in intervals:
            start, end = interval.start, interval.end
            interval_list.append([start, end])
        interval_list = sorted(interval_list)
        start, end = interval_list[0]
        n = len(interval_list)
        for i in range(1, n):
            next_start, next_end = interval_list[i]
            if end > next_start:
                return False
            start, end = next_start, next_end
        return True

            

