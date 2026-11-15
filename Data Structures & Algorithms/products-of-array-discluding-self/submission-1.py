class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]
        n = len(nums)
        for i in range(n-1):
            left.append(left[i]*nums[i])
            right.append(right[i]*nums[n-1-i])
        result = []
        for i in range(n):
            result.append(left[i]*right[n-1-i])
        
        return result


        
        