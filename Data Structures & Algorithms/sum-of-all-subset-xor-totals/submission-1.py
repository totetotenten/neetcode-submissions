class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        result = []
        path = 0
        def BT(start, path):
            for i in range(start, n):
                path ^= nums[i]
                result.append(path)
                BT(i + 1, path)
                path ^= nums[i]

        BT(0, path)
        return sum(result)


        