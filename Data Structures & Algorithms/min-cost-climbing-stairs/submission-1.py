class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = 0, 0
        n = len(cost)
        for i in range(n):
            tmp = prev1
            prev1 = min(prev2 + cost[i], prev1 + cost[i])
            prev2 = tmp
        return min(prev1, prev2)

        