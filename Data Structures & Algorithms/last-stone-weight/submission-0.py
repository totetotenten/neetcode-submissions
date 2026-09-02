import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: 
        heap_stone = []
        for stone in stones:
            heapq.heappush(heap_stone, -1*stone)
        
        while len(heap_stone) > 1:
            x = heapq.heappop(heap_stone)
            y = heapq.heappop(heap_stone)
            if x != y:
                new = x - y
                heapq.heappush(heap_stone, new)


        if heap_stone:
            return heap_stone[0]*-1
        else:
            return 0

        