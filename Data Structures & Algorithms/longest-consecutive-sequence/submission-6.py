class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        length = 0
        for num in nums:
            if num - 1 in seen:
                continue

            tmp_length = 1
            tmp = num
            while tmp + 1 in seen:
                tmp += 1
                tmp_length += 1
            length = max(tmp_length, length)

        return length
