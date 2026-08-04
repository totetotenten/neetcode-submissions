class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        seen = 101
        for i, price in enumerate(prices):
            seen = min(seen, price)
            result = max(result, price - seen)
        return result


        