class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        result = None
        while left < right:
            mid = (left + right)//2
            result = nums[mid]
            if result > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        