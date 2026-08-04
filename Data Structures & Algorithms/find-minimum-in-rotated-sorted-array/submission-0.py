class Solution:
    def findMin(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        return sorted_list[0]

        