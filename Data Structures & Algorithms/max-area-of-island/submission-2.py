class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Intuition:
            - Run DFS/BFS on every strongly/ connected component
            - Return the component with max nodes
        """

        #consts
        ROWS, COLS = len(grid), len(grid[0])
        seen = [[False for i in range(COLS)] for i in range(ROWS)]

        def isValid(r,c) -> bool:
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS):
                return False
            return True
        
        def dfs(r, c):
            stack = []
            stack.append((r,c))
            seen[r][c] = True
            directions = [[-1,0], [1,0], [0,1], [0,-1]]
            num_nodes = 1
            while stack:
                xr,xc = stack.pop()
                for dr, dc in directions:
                    x = xr+dr
                    y = xc+dc

                    if (isValid(x,y) and seen[x][y] != True and grid[x][y] != 0):
                        seen[x][y] = True
                        stack.append((x, y))
                        num_nodes = num_nodes + 1
            
                seen[xr][xc] = True
            return num_nodes

        max_area = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (grid[i][j] == 1 and not seen[i][j]):
                    max_area = max(max_area, dfs(i,j))

        return max_area