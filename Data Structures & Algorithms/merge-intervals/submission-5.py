class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        result = []
        prev = [0, 0]
        for i, interval in enumerate(intervals):
            prev_start, prev_end = prev
            tmp_start, tmp_end = interval
            if prev_end >= tmp_start:
                prev = [prev_start, max(prev_end, tmp_end)]
            else:
                if i != 0:
                    result.append(prev)
                prev = interval
        result.append(prev)

        return result