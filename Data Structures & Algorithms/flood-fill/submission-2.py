from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cur = image[sr][sc]
        q = deque([(sr, sc)])
        n, m = len(image), len(image[0])
        seen = set()
        while q:
            i, j = q.popleft()
            seen.add((i, j))
            if image[i][j] == cur:
                image[i][j] = color
            else:
                continue
            if i+1 <= n-1 and (i+1, j) not in seen:
                q.append((i+1, j))
            if i-1 >= 0 and (i-1, j) not in seen:
                q.append((i-1, j))
            if j+1 <= m-1 and (i, j+1) not in seen:
                q.append((i, j+1))
            if j-1 >= 0 and (i, j-1) not in seen:
                q.append((i, j-1))
        return image
        

        