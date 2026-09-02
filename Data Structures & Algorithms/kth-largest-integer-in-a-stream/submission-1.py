import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = sorted(nums)
        self.stack = nums[-k:]
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.stack, val)
        if len(self.stack) > self.k:
            heapq.heappop(self.stack)
        result = self.stack[0]
        return result 

