class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        result = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[j][n-1-i] = matrix[i][j]
        matrix[:] = result
