import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = [(-v, key) for key, v in c.items()]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)]
        