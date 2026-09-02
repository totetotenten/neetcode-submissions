class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse = True)
        seen = {}
        seen[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    need = i - coin 
                    if seen[need] != -1:
                        tmp = seen.get(i, float('inf'))
                        seen[i] = min(tmp, seen[need]+1)
            seen.setdefault(i, -1)

        return seen[amount]
        