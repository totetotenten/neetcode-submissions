class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            chars = "".join(sorted(word))
            seen.setdefault(chars, [])
            seen[chars].append(word)
        return list(seen.values())