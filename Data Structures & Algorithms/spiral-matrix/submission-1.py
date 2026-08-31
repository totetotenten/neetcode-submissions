class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        short = min(n, m)
        for i in range((short+1)//2):
            for j in range(i, n-i):
                result.append(matrix[i][j])
            for j in range(i+1, m-i):
                result.append(matrix[j][n-i-1])
            if i*2 + 1 < short:
                for j in range(i+1, n-i):
                    result.append(matrix[m-i-1][n-j-1])
                for j in range(i+1, m-i-1):
                    result.append(matrix[m-j-1][i])
        return result

        