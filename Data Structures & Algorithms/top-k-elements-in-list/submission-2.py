class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen.setdefault(num, 0)
            seen[num] += 1
        seen_list = list(seen.items())
        seen_list = sorted(seen_list, key = lambda x:x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(seen_list[i][0])
        return result
    