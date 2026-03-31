class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def isValid(r,c,grid):
            ROWS, COLS = len(grid), len(grid[0])
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS):
                return False
            return True

        def dfs(r,c,grid,seen):
            queue = []
            queue.append((r,c))
            directions = [[-1, 0], [1,0], [0,-1], [0, 1]]
            while queue:
                xr, xc = queue.pop()

                for dr, dc in directions:
                    x = xr + dr
                    y = xc + dc

                    if (isValid(x,y,grid) and (seen[x][y] == False)) and not grid[x][y] == "0":
                        queue.append((x,y))
                        seen[x][y] = True
                
                seen[xr][xc] = True


        ROWS, COLS = len(grid), len(grid[0])
        seen = []
        for i in range(ROWS):
            seen.append([])
            for j in range(COLS):
                seen[i].append(False)

        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (grid[i][j] == "1" and seen[i][j] == False):
                    count = count + 1
                    dfs(i,j,grid,seen)
        
        return count