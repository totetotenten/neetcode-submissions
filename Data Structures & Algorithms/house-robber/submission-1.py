class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            one, two = max(two+num, one), one
        return one
        