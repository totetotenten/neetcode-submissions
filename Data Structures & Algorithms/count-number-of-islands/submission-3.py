class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        n, m = len(grid), len(grid[0])
        res = 0

        def search(i, j):
            if i < 0 or i > n - 1 or j < 0 or j > m - 1:   # 範囲外
                return
            if (i, j) in seen or grid[i][j] == "0":        # 見た / 水
                return
            seen.add((i, j))
            search(i + 1, j)   # 下
            search(i - 1, j)   # 上
            search(i, j + 1)   # 右
            search(i, j - 1)   # 左

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in seen:
                    res += 1          # 新しい島を見つけた
                    search(i, j)      # つながっている陸を全部「見た」にする
        return res



        