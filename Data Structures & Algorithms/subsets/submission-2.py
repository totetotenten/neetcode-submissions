class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        path = []
        n = len(nums)
        def BT(start):
            for i in range(start, n):
                path.append(nums[i])
                result.append(path.copy())
                BT(i + 1)
                path.pop()
        BT(0)
        return result            

        