class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, result = 0, 0, 0
        n = len(s)
        seen = {}
        while left + result < n:
            seen.setdefault(s[right], 0)
            seen[s[right]] += 1
            length = right - left + 1
            if length - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
                right += 1
            else:
                result = max(length, result)
                right += 1
        return result
        