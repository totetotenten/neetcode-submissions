class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        n = len(cost)
        for i in range(n):
            tmp = one
            one = min(two + cost[i], one + cost[i])
            two = tmp
        return min(one, two)

        