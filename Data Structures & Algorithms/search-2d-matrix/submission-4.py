class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if m == 0:
            return False      
        up, down = 0, m - 1
        while up <= down:
            mid = (up + down)//2
            if target < matrix[mid][0]:
                down = mid - 1
            elif target > matrix[mid][n-1]:
                up = mid + 1
            else:
                left, right = 0, n - 1
                while left <= right:
                    center = (left + right)//2
                    if matrix[mid][center] == target:
                        return True
                    if matrix[mid][center] < target:
                        left = center + 1
                    else:
                        right = center -1
                return False

        return False

