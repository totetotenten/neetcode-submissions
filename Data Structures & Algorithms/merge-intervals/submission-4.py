class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals)
        n = len(intervals)
        start, end = intervals[0]
        for i in range(1, n):
            if intervals[i][0] > end:
                result.append([start, end])
                start, end = intervals[i]
            else:
                start = min(start, intervals[i][0]) 
                end = max(end, intervals[i][1])

        result.append([start, end])
        return result

        