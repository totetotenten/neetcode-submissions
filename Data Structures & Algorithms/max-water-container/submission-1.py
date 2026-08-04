class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        max_water = 0
        while left < right:
            water = (right - left) * min(heights[left], heights[right])
            max_water = max(max_water, water)
            if heights[left] > heights[right]:
                right -=1
            else:
                left += 1
        return max_water
        