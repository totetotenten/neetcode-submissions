class Solution:
    def rob(self, nums: List[int]) -> int:
        one_, two_ = 0, 0
        one, two = nums[0], nums[0]
        n = len(nums)
        for i in range(1, n):
            if i == 1:
                one_ = nums[i]
            elif i == n-1:
                tmp = one_
                one_ = max(two_+nums[i], one_)
                two_ = tmp
            else:
                tmp_, tmp = one_, one
                one_, one = max(two_+nums[i], one_), max(two+nums[i], one)
                two_, two = tmp_, tmp
        return max(one_, one)

        