class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        m, n = len(board), len(board[0])
        t = len(word)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def search(row: int, col: int, char_num: int) -> bool:
            char = word[char_num]
            if (row, col) in seen:
                return False
            if board[row][col] == char:
                char_num += 1
                seen.add((row, col))
                if char_num == t:
                    return True
        
                for i, j in directions:
                    tmp_row = row + i
                    tmp_col = col + j
                    if 0 <= tmp_row <= m-1 and 0 <= tmp_col <= n-1:
                        if search(tmp_row, tmp_col, char_num):
                            return True
                char_num -= 1
                seen.remove((row, col))
                    
            return False
                            
        for i in range(m):
            for j in range(n):
                if search(i, j, 0):
                    return True
        return False
        