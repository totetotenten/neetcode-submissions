class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sums = set()
        n = len(nums)
        for i, num in enumerate(nums):
            if num > 0:
                break
            need = 0 - num
            left, right = i+1, n-1
            while left < right:
                l_num, r_num = nums[left], nums[right]
                if l_num + r_num == need:
                    tmp = (num, l_num, r_num)
                    if tmp not in sums:
                        sums.add(tmp)
                    left += 1
                elif l_num + r_num > need:
                    right -= 1
                else:
                    left += 1


        result = list(map(list, sums))
        return result

        