class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.setdefault(num, 0) + 1
        values = list(seen.values())
        sorted_items = sorted(seen.items(), reverse=True, key = lambda x: x[1])

        top_k = sorted_items[:k]

        result = []
        for item in top_k:
            result.append(item[0])

        return result

        