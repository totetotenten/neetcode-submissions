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
        result = 1
        if not intervals:
            return 0
        
        sorted_intervals = sorted(intervals, key = lambda interval:interval.start)
        n = len(sorted_intervals)
        room_ends = []
        heapq.heappush(room_ends, -1) 
        for interval in sorted_intervals:
            start, end = interval.start, interval.end
            earliest_end = room_ends[0]
            if earliest_end <= start:
                heapq.heappop(room_ends) 
                heapq.heappush(room_ends, end) 
            else:
                heapq.heappush(room_ends, end)
                result = max(result, len(room_ends)) 

        return result      