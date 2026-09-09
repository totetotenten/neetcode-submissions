class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[nums[0]], nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        fast = 0
        while fast != slow:
            prev = fast
            fast, slow = nums[fast], nums[slow]

        return fast