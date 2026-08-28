class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            char = "".join(sorted(word))
            seen.setdefault(char, []).append(word)
        return list(seen.values())