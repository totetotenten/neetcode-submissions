"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        rooms = 0
        ends = []
        for inter in intervals:
            cur_start, cur_end = inter.start, inter.end
            if ends and ends[0] <= cur_start:
                heapq.heappop(ends)    
            heapq.heappush(ends, cur_end)
        return len(ends)