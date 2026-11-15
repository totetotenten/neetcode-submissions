class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, left, subsum = float("inf"), 0, 0
        flag = False
        n = len(nums)
        for right in range(n):
            subsum += nums[right]
            if subsum >= target:
                while subsum - nums[left] >= target:
                    subsum -= nums[left]
                    left += 1
                    
                length = right - left + 1
                res = min(res, length)
    
        if res == float("inf"):
            res = 0
        return res
        