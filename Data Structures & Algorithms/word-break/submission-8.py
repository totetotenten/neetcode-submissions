class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        seen = set(wordDict)
        min_t, max_t = float('inf'), 0
        for word in wordDict:
            min_t = min(min_t, len(word))
            max_t = max(max_t, len(word))

        dp[0] = True
        n = len(s)
        for i in range(n+1):
            if i not in dp:
                return False
            if not dp[i]:
                continue
            for j in range(1, max_t+1):
                if s[i:i+j] in seen:
                    dp[i+j] = True
                else:
                    dp.setdefault(i+j, False)
                print(i+j, dp[i+j])
        return dp[n]



        
        