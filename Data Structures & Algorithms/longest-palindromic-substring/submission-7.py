class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        length = 0
        start = 0
        for i, char in enumerate(s):
            left, right = i, i
            while left>0 and right<n-1:
                if s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                else:
                    break
            if length < right - left + 1:
                length = right - left + 1
                start = left
            if i+1 <= n-1 and char == s[i+1]:
                left, right = i, i+1
            while left>0 and right<n-1:
                if s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                else:
                    break
            if length < right - left + 1:
                length = right - left + 1
                start = left
            print(start, length)
        result = ""
        for i in range(length):
            result = result + s[i+start]
        return result