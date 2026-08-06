class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals)
        n = len(intervals)
        start, end = intervals[0]
        for i in range(n-1):
            if intervals[i+1][0] > end:
                result.append([start, end])
                start, end = intervals[i+1]
            else:
                start = min(start, intervals[i+1][0]) 
                end = max(end, intervals[i+1][1])

        result.append([start, end])
        return result

        