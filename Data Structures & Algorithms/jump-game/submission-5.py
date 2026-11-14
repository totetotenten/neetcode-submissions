class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_length = 0
        n = len(nums)
        for i, num in enumerate(nums):
            jump_length = max(jump_length-1, num)
            if i + jump_length >= n-1:
                return True
            if jump_length <= 0:
                return False
            


        