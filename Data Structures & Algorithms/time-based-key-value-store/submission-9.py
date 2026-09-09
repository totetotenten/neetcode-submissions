import heapq
class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d.setdefault(key, [])
        self.d[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.d.get(key)
        if not lst:
            return ""

        n = len(lst)
        left, right = 0, n-1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if lst[mid][0] == timestamp:
                return lst[mid][1]
            if lst[mid][0] > timestamp:
                right = mid - 1
            else:
                result = lst[mid][1]
                left = mid + 1
        return result



        
        
