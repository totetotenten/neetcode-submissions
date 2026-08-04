class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        result = 0
        before = None
        sequence = 0
        for num in sorted_nums:
            sequence += 1   
            if before is not None and num - before != 1:
                sequence = 1
            if sequence > result:
                result = sequence
            before = num
        return result


        