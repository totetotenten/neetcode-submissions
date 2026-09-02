class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            tmp_result = []
            for subset in result:
                tmp = subset.copy()
                tmp.append(num)
                tmp_result.append(tmp)
            result = result + tmp_result
        return result
        
