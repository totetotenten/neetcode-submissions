class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        n = len(s)
        res, left = 0, 0
        for right in range(n):
            length = right - left + 1
            d.setdefault(s[right], 0)
            d[s[right]] += 1
            max_num = max(d.values())
            if length - max_num > k:
                d[s[left]] -= 1
                left += 1
            length = right - left + 1
            res = max(res, length)
            #print(left, right, res)

        return res

            
            

            