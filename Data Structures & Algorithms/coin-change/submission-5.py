class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        d = {}
        for t in range(amount+1):
            cur = float("inf")
            if t == 0:
                d[t] = 0
            elif t in coins:
                d[t] = 1
            else:
                for coin in coins:
                    if coin < t:
                        cur = min(cur, d[t-coin]+1)
                d[t] = cur
            print(t, d[t])
        res = d[amount]
        return -1 if res == float("inf") else res





        