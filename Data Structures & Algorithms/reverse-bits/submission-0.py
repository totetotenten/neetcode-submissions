class Solution:
    def reverseBits(self, n: int) -> int:
        bin_lst = [0]*32
        i = 0
        while n > 0:
            if n % 2 == 1:
                bin_lst[i] = 1
                n -= 1
            n = n//2
            i += 1

        print(bin_lst)
        result = "".join(map(str, bin_lst))
        return int(result, 2)

                
        