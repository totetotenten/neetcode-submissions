class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        q = len(nums)
        left = [1]*q
        right = [1]*q
        for i in range(q):
            if i != 0:
                left[i] = left[i-1] * nums[i-1]
                right[q-1-i] = right[q-i] * nums[q-i]
        result = []
        for i in range(q):
            result.append(left[i]*right[i])
        return result
        

