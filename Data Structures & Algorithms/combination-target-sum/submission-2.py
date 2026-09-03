class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        nums = sorted(nums)
        n = len(nums)
        def BT(start, target):
            for i in range(start, n):
                if target < 0:
                    break
                target -= nums[i]
                path.append(nums[i])
                if target == 0:
                    result.append(path.copy())
                BT(i, target)
                path.pop()
                target += nums[i]
        BT(0, target)
        return result

        