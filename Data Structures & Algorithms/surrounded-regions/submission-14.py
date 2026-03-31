class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # initial thought:
            # lets run BFS and find all connected components
            # then check if any node in the connected component is a border node, if yes then no change, otherwise change to X

        ROWS, COLS = len(board), len(board[0])
        seen = [[False for i in range(COLS)] for i in range(ROWS)]
        connected_comp = []

        def isValid(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == "X"):
                return False
            return True

        def isOnBorder(r,c):
            if (c == 0 or c == COLS-1 or r == 0 or r == ROWS-1):
                return True
            return False

        #helper function to debug
        def pretty_print(board):
            for i in range(len(board)):
                print(board[i])

        def bfs(r,c):
            queue = []
            queue.append((r,c))
            path = []
            seen[r][c] = True
            dirs = [(-1,0), (1,0), (0,-1), (0,1)]
            while queue:
                xr, xc = queue.pop(0)
                seen[xr][xc] = True
                path.append((xr,xc))
                for dr, dc in dirs:
                    ir = dr + xr
                    ic = dc + xc

                    if (isValid(ir,ic) and (seen[ir][ic] != True)):
                        queue.append((ir,ic))

            for i,j in path:
                if (isOnBorder(i,j)):
                    return []
            return path

        #input in a pretty format
        pretty_print(board)                

        
        #now seen has all connected components
        for i in range(ROWS):
            for j in range(COLS):
                if (board[i][j] == "O" and seen[i][j] != True):
                    connected_comp.append(bfs(i,j))

        for lis in connected_comp:
            print(lis)
            for r,c in lis:
                board[r][c] = "X"       
        
