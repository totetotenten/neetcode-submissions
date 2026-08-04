class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        small = 101
        for price in prices:
            result = max(result, price - small)
            small = min(small, price)
        return result

        