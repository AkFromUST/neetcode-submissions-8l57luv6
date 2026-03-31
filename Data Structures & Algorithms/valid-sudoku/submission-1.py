class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #traverse through all rows, all cols and store the data in sets.

        ROWS, COLS = len(board), len(board[0])

        square_hash = {}
        
        #rows first
        for i in range(ROWS):
            row_set = set()
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_set:
                    print(board[i][j], "Present in row: ", i)
                    return False
                row_set.add(board[i][j])

        #cols
        for col in range(COLS):
            col_set = set()
            for row in range(ROWS):
                if board[row][col] == ".":
                    continue
                if board[row][col] in col_set:
                    return False
                col_set.add(board[row][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True