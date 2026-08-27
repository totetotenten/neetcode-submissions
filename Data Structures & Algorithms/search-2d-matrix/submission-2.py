class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if m == 0:
            return False
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left+right)//2
            m_tmp = mid//n
            n_tmp = mid%n
            if matrix[m_tmp][n_tmp] == target:
                return True
            if matrix[m_tmp][n_tmp] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False