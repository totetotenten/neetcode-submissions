class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res, length = 0, 1
        for num in nset:
            if num - 1 not in nset:
                cur = num
                while cur + 1 in nset:
                    cur += 1
                    length += 1
                res = max(res, length)
                print(num, res, length)
                length = 1
            
        return res
        