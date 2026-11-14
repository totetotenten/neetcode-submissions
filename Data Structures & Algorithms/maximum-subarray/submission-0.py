class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        current = 0
        for num in nums:
            if current < 0:
                current = num
            else:
                current += num
            if current > res:
                res = current
        return res
            

        