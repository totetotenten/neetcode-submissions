class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        result = 0
        left = 0
        seen = {}
        for i, char in enumerate(s):
            if seen.get(char, -1) >= left:
                left = seen[char] + 1
            length = i - left + 1
            result = max(result, length)
            seen[char] = i
        return result
        