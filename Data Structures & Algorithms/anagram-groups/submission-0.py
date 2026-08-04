class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i, word in enumerate(strs):
            chars = "".join(sorted(word))
            seen.setdefault(chars, []).append(word)
        return list(seen.values())