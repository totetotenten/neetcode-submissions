from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            word_list = tuple(sorted(Counter(word).items()))
            seen.setdefault(word_list,[])
            seen[word_list].append(word)
        
        return list(seen.values())