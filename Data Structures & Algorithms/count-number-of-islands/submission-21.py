class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        def _isValid(x, y):
            n,m = len(grid), len(grid[0])
            if (0 <= x <= n-1) and (0 <= y <= m-1) and (grid[x][y] == "1"):
                return True
            return False

        #dfs
        seen = set()

        def dfs(x,y):
            stack = []
            stack.append((x,y))
        
            nei = [(-1,0), (1,0), (0,-1), (0,1)]

            while stack:
                ix, iy = stack.pop()
                
                for i,j in nei:
                    dr, dc = ix + i, iy + j
                    if ((dr,dc) not in seen) and _isValid(dr,dc):
                        stack.append((dr,dc))
                
                seen.add((ix,iy))

        total_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ((i,j) not in seen) and grid[i][j] == "1":
                    total_islands += 1
                    dfs(i,j)

        return total_islands