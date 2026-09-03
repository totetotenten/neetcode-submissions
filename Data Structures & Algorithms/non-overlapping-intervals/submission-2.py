class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        print(intervals)
        prev = None
        result = 0
        for interval in intervals:
            if prev is None:
                prev = interval.copy()
                continue

            prev_start, prev_end = prev
            tmp_start, tmp_end = interval
            if prev_end > tmp_start:
                result += 1
                #print(prev)
                if prev_end >= tmp_end:
                    prev = interval.copy()
            else:
                prev = interval.copy()

            
        return result


                