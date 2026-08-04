class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i, num in enumerate(nums): 
            if target - num in needs:
                return [needs[target - num], i]
            needs[num] = i