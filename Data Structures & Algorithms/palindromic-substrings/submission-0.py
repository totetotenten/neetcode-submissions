class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n):
            left, right = i, i
            while left >= 0 and right <= n-1:
                if s[left] != s[right]:
                    break
                result += 1
                left -= 1
                right += 1

        for i in range(n-1):
            left, right = i, i+1
            while left >= 0 and right <= n-1:
                if s[left] != s[right]:
                    break
                result += 1
                left -= 1
                right += 1

        return result

        