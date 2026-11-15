class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, left, ones = 0, 0, 0
        n = len(nums)
        for right in range(n):
            length = right - left + 1
            if nums[right] == 1:
                ones += 1
            if length - ones > k:
                if nums[left] == 1:
                    ones -= 1
                left += 1
            length = right - left + 1
            res = max(res, length)
            print(left, right, ones, res)
        return res

        