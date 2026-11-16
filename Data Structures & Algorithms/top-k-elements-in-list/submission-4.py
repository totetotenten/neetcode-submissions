class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen.setdefault(num, 0)
            seen[num] += 1
        result_list = sorted(list(seen.items()), key = lambda x:x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(result_list[i][0])
        return result