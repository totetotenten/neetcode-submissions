class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            dig_a = (a & (1 << i)) >> i
            dig_b = (b & (1 << i)) >> i
            dig_tmp = dig_a ^ dig_b ^ carry
            carry = (dig_a & dig_b) | (dig_a & carry) | (carry & dig_b)
            result = result | (dig_tmp << i)

        if result > 0x7FFFFFFF:
            result = ~(result^mask)
        return result

