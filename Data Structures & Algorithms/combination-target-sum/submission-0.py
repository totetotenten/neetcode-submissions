class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def search(current, target, idx):
            if target == 0:
                result.append(current.copy())
            if target < 0:
                return None
            n = len(nums)
            for i in range(idx, n):
                current.append(nums[i])
                search(current, target - nums[i], i)
                current.pop()

        search([], target, 0)
        return result
        