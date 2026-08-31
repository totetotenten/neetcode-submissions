class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for digit in str(bin(n)):
            if digit == "1":
                result += 1
        return result
    

        