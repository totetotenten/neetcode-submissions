from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = Counter(s1)
        left, k = 0, len(s1)
        n = len(s2)
        while left + k - 1 <= n-1:
            tmp = s2[left:left + k]
            tmp_count = Counter(tmp)
            if tmp_count == target_count:
                return True
            else:
                left += 1
        return False