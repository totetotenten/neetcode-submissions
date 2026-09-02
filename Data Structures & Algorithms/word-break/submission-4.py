class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_k = {}
        min_k = float("inf")
        max_k = 0
        for word in wordDict:
            k = len(word)
            min_k = min(min_k, k)
            max_k = max(max_k, k)
            dict_k.setdefault(k, set())
            dict_k[k].add(word)
        
        n = len(s)   
        k = min_k
        if n in dict_k and s in dict_k[n]:
            return True
                
        while n - k >= min_k:
            if k not in dict_k:
                k += 1
                continue

            word_k = s[:k]
            if word_k not in dict_k[k]:
                k += 1
                continue

            l = min_k
            while n - (k+l) >= 0 and l <= max_k:
                    if l not in dict_k:
                        l += 1
                        continue

                    word_l = s[k:k+l]
                    if word_l not in dict_k[l]:
                        l += 1
                        continue   
                    if k + l == n:
                        return True
                    dict_k.setdefault(k+l, set())
                    dict_k[k+l].add(word_k + word_l)
                    max_k = max(max_k, k + l)
                    l += 1
            k += 1
        
        return False
            

            




        

        