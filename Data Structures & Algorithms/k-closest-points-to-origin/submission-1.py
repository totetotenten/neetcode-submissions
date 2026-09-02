import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for point in points:
            x, y = point
            tmp_point = [-1*(x**2+y**2), x, y]
            heapq.heappush(result, tmp_point)
            if len(result) > k:
                heapq.heappop(result)
        
        closest = []
        
        for tmp in result:
            _, x, y = tmp
            closest.append([x, y])
        return closest




        