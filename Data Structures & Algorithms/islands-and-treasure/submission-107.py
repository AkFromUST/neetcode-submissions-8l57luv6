class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # multisource BFS? 
        # but how do I start all the bfs at the same time
        # simply append the coordinates to the stack

        ROWS, COLS = len(grid), len(grid[0])
        treasures = []
        seen = set()
        nei = [[-1,0], [1,0], [0,-1], [0,1]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    treasures.append((i,j))

        for i,j in treasures:
            seen.add((i,j))

        def _isValid(x,y):
            if (x < 0 or x >= ROWS) or (y < 0 or y >= COLS) or (grid[x][y] == -1):
                return False
            return True

        while treasures:

            ix, iy = treasures.pop(0)

            for i,j in nei:
                dr,dc = ix + i, iy + j

                if ((dr,dc) not in seen) and _isValid(dr,dc):
                    treasures.append((dr,dc))
                    grid[dr][dc] = grid[ix][iy] + 1 
                    seen.add((dr,dc))

        def pprint():
            for i in range(ROWS):
                print(grid[i])