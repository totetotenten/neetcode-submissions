class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals = sorted(intervals)
        n = len(intervals)
        start, end = intervals[0]
        for i in range(1, n):
            new_start, new_end = intervals[i]
            if new_start >= end:
                start, end = new_start, new_end
            else:
                if end >= new_end:
                    start, end = new_start, new_end
                    result += 1
                else:
                    result += 1
        return result

            