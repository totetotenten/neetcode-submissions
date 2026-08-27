class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two = 0
        three = 0
        n = len(nums)
        for i in range(n):
            tmp = one 
            one = max(two+nums[i], three+nums[i])
            three = two
            two = tmp
        

        return max(one, two, three)
        
        