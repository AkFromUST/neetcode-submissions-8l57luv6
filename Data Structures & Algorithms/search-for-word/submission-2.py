class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # hacky way? DFS?

        ROWS, COLS = len(board), len(board[0])
        nei = [[0,1], [0,-1], [1,0], [-1, 0]]
        present = False
        seen = set()

        def _inBounds(x,y):
            if (x < 0 or x >= ROWS) or (y < 0 or y >= COLS):
                return False
            return True

        def backtracking(x,y,curr):

            print("curr:\t", curr)

            if curr == word:
                nonlocal present
                present = True
                print("\t\tpresent: ", present)
                return

            if not _inBounds(x,y):
                return

            seen.add((x,y))

            #check all 4 dirs
            for i,j in nei:
                a,b = x + i, y + j
                if _inBounds(a,b) and board[a][b] in word and (a,b) not in seen:
                    backtracking(a,b, curr + board[a][b])
            
            seen.remove((x,y))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] in word:
                    backtracking(i,j, board[i][j])

        return present