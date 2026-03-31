class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def isValid(grid, x, y, row, col):
            row = len(grid)
            col = len(grid[0])
            if (x < 0 or x >= row) or (y < 0 or y >= col) or (grid[x][y] < 0):
                return False
            return True

        def bfs(ix,iy, grid):
            #adding to queue
            queue = []
            queue.append((ix,iy))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            min_dist = float("inf")

            #init dist, seen
            seen, dist = [], []
            for i in range(row):
                seen.append([])
                dist.append([])
                for j in range(col):
                    seen[i].append(False)
                    dist[i].append(float("inf"))

            dist[ix][iy] = 0

            while queue:
                #pop from queue
                x,y = queue.pop(0)

                for dr, dc in directions:
                    xr = x + dr
                    xc = y + dc

                    if isValid(grid, xr, xc, len(grid), len(grid[0])) and (not (seen[xr][xc])):
                        if (grid[xr][xc] > 0):
                            queue.append((xr, xc))
                            seen[xr][xc] = True
                            dist[xr][xc] = dist[x][y] + 1
                        elif (grid[xr][xc] == 0):
                            dist[xr][xc] = dist[x][y] + 1
                            seen[xr][xc] = True
                            min_dist = min(min_dist, dist[xr][xc])

                seen[x][y] = True
        
            grid[ix][iy] = min_dist

        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if (grid[i][j] > 1):
                    bfs(i,j, grid)