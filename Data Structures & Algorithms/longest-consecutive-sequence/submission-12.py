class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        seen = set()
        res, length, cur = 1, 0, None
        if not nset:
            return 0
        for num in nset:
            if num in seen:
                continue
            cur = num
            while cur - 1 in nset:
                length += 1
                cur += 1
                seen.add(cur-1)
            res = max(res, length)
            length = 0
        return res
            

            


        