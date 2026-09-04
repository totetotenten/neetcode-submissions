class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        seen = set()
        n = len(nums)
        def BT(i: int):
            if i not in seen:
                path.append(nums[i])
                if len(path) == n:
                    result.append(path.copy())
                seen.add(i)
                for j in range(n):
                    BT(j)
                seen.remove(i)
                path.pop()
        
        for i in range(n):
            BT(i)
        return result
                

            

        

        