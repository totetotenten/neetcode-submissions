class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)
        for i, height in enumerate(heights):
            left = i
            right = n-1
            while left < right:
                water = (right - left)*min(heights[left], heights[right])
                max_water = max(max_water, water)
                right -= 1
        return max_water


            

        