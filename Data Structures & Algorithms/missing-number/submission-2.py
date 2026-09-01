class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prev = -1
        for num in nums:
            if num - prev != 1:
                return prev + 1
            prev = num
        return prev + 1
        