import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen.setdefault(num, 0)
            seen[num] += 1
        result = [(-v, key) for key, v in seen.items()]
        heapq.heapify(result)
        res = []
        for _ in range(k):
            _, key = heapq.heappop(result)
            res.append(key)

        return res
        

        