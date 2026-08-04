class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        seen_num = set()
        result = []
        n = len(sorted_nums)
        for i, num in enumerate(sorted_nums):
            if num in seen_num:
                continue
            seen = set()
            seen_sum = set()
            need = 0 - num
            for j in range(n-i-1):
                if need-sorted_nums[i+j+1] in seen:
                    if (need-sorted_nums[i+j+1], sorted_nums[i+j+1]) in seen_sum:
                        continue
                    result.append([num, need-sorted_nums[i+j+1], sorted_nums[i+j+1]])
                    seen_sum.add((need-sorted_nums[i+j+1], sorted_nums[i+j+1]))
                seen.add(sorted_nums[i+j+1])
            seen_num.add(num)

        return result
        