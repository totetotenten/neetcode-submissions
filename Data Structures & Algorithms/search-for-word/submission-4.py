class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        char_dict = {}
        for i, row in enumerate(board):
            for j, char in enumerate(board[i]):
                char_dict.setdefault(char, []).append((i, j))
        
        need_char = list(word)
        start_list = char_dict.get(need_char[0],[])
        checked_board = set()
        def search(row, col, idx, checked_board):
            is_match = False
            checked_board.add((row, col))
            if board[row][col] == need_char[idx]:
                if idx == len(need_char)-1:
                    return True
                if row-1 >= 0 and (row-1, col) not in checked_board:
                    if search(row-1, col, idx+1, checked_board):
                        is_match = True
                if row+1 <= len(board)-1 and (row+1, col) not in checked_board:
                    if search(row+1, col, idx+1, checked_board):
                        is_match = True
                if col-1 >= 0 and (row, col-1) not in checked_board:
                    if search(row, col-1, idx+1, checked_board):
                        is_match = True
                if col+1 <= len(board[row])-1 and (row, col+1) not in checked_board:
                    if search(row, col+1, idx+1, checked_board):
                        is_match = True

            checked_board.remove((row, col))
            return is_match  


        for start in start_list:
            row, col = start
            if search(row, col, 0, checked_board):
                return True
        return False
