class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # to check if the node value is greater or not
        
        ROWS, COLS = len(heights), len(heights[0])
        
        pac_nodes = []
        atl_nodes = []

        def canTraverse(x1, y1, x2, y2, grid):
            if (heights[x1][y1] <= heights[x2][y2]):
                return True
            return False
        
        def isValid(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS):
                return False
            return True
        
        def dfs(r,c, fromWhere):
            stack = []
            stack.append((r,c))
            dirs = [[-1,0], [1,0], [0,-1], [0,1]]
            while stack:
                x,y = stack.pop()
                seen[x][y] = True
                if (fromWhere == "pac"):
                    pac_nodes.append((x,y))
                else:
                    atl_nodes.append((x,y))
                
                for dr, dc in dirs:
                    xr = x + dr
                    xc = y + dc

                    if (isValid(xr,xc) and seen[xr][xc] != True) and (canTraverse(x,y,xr,xc,heights)):
                        stack.append((xr,xc))
                    
        res = []

        seen = [[False for i in range(COLS)] for i in range(ROWS)]
        for i in range(COLS):
            dfs(0,i, "pac")
        for i in range(ROWS):
            dfs(i,0,"pac")

        seen = [[False for i in range(COLS)] for i in range(ROWS)]
        for i in range(COLS):
            dfs(ROWS-1,i, "alt")
        for i in range(ROWS):
            dfs(i, COLS-1, "alt")
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac_nodes and (r,c) in atl_nodes:
                    res.append((r,c))
        
        return res