class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        nei = [(-1,0), (1,0), (0,1), (0,-1)]
        row, col = len(grid), len(grid[0])
        
        def _dfs(x,y):
            s = []
            s.append((x,y))
            while s:
                dx, dy = s.pop()
                grid[dx][dy] = "0"
                for r,c in nei:
                   nx, ny = dx + r, dy + c
                   if (nx >= 0 and nx < row) and (ny >= 0 and ny < col) and (nx,ny) and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        s.append((nx,ny))
        
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "0":
                    continue
                _dfs(r, c)
                count += 1

        return count