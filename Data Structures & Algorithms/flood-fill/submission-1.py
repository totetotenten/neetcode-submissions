#再帰
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        new_image = image.copy()
        n, m = len(image), len(image[0])
        def change(i, j, prev, new):
            if i > n-1 or j > m-1 or i < 0 or j <0:
                return
            if image[i][j] != prev:
                seen.add((i, j))
                return
            if (i, j) in seen:
                return
            seen.add((i, j))
            new_image[i][j] = new
            change(i+1, j, prev, new)
            change(i-1, j, prev, new)
            change(i, j+1, prev, new)
            change(i, j-1, prev, new)
        
        prev = image[sr][sc]
        change(sr, sc, prev, color)

        return new_image