import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)
        while min_k < max_k:
            mid = (min_k + max_k)//2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/mid)
            if hour > h:
                min_k = mid + 1
            else:
                max_k = mid 
        return min_k


        