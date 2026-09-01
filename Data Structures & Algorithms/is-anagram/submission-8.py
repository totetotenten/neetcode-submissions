class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}
        t_seen = {}
        for char in s:
            s_seen.setdefault(char, 0)
            s_seen[char] += 1
        for char in t:
            t_seen.setdefault(char, 0)
            t_seen[char] += 1
        if s_seen == t_seen:
            return True
        else:
            return False


        