class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            num_one = 0
            for digit in bin(i):
                if digit == "1":
                    num_one += 1
            result.append(num_one)
        return result
