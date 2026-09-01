class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] in seen:
                    return False
                if board[i][j] == ".":
                    continue
                seen.add(board[i][j])
            seen = set()

        seen = set()
        for i in range(9):
            for j in range(9):
                if board[j][i] in seen:
                    return False
                if board[j][i] == ".":
                    continue
                seen.add(board[j][i])
            seen = set()
        
        seen = set()
        for i in range(9):
            for j in range(9):
                m = (i//3)*3 + j//3
                n = (i%3)*3 + j%3
                if board[m][n] in seen:
                    return False
                if board[m][n] == ".":
                    continue
                seen.add(board[m][n])
            seen = set()
        return True