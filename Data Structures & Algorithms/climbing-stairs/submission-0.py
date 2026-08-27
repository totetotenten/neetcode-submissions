class Solution:
    def climbStairs(self, n: int) -> int:
        back_one = 1
        back_two = 0
        i = n
        result = 0
        while i > 0:
            result = back_one + back_two
            back_two = back_one
            back_one = result
            i -= 1
        return result
        
        