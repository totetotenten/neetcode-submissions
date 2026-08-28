class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        result = []
        n = len(nums)
        for i, num in enumerate(nums):
            if num in seen:
                continue
            if num > 0:
                continue
            left, right = i+1, n-1
            seen_left = set()
            while left < right:
                if nums[left] in seen_left:
                    left += 1
                    continue
                if nums[left]+nums[right]+num == 0:
                    result.append([num, nums[left], nums[right]])
                    seen_left.add(nums[left])
                    left += 1   
                elif nums[left]+nums[right]+num > 0:
                    right -= 1
                else:
                    left += 1
            seen.add(num)
        return result
        