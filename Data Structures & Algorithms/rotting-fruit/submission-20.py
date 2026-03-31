class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        # same as prev. Multisource BFS
        ROWS, COLS = len(grid), len(grid[0])

        nei = [[-1,0], [1,0], [0,-1], [0,1]]
        q = deque()
        mins = 0
        fresh = 0

        # adding all the rotten fruits now
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        #edge case 1: no rotten fruits
        if len(q) == 0 and fresh:
            return -1

        if not fresh:
            return 0
        

        def _isValid(x,y):
            if (x < 0 or x >= ROWS) or (y < 0 or y >= COLS) or grid[x][y] != 1:
                return False
            return True

        while q:
            for i in range(len(q)):
                ix, iy = q.popleft()
                for i,j in nei:
                    dr, dc = ix + i, iy + j
                    if _isValid(dr,dc):
                        grid[dr][dc] = 2
                        q.append((dr,dc))
            mins += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        return mins -1