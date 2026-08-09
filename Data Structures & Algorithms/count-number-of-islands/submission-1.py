class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        result = 0
        def search(row, col, seen):
            if (row, col) in seen:
                return False
            if grid[row][col] == "1":
                seen.add((row, col))
                for (dr, dc) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= row + dr <= len(grid)-1:
                        if 0 <= col + dc <= len(grid[0])-1:
                            search(row + dr, col + dc, seen)
                return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if search(i, j, seen):
                    result += 1
        return result
