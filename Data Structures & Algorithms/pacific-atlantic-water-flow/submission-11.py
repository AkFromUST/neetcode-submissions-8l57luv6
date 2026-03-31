class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # to check if the node value is greater or not
        
        ROWS, COLS = len(heights), len(heights[0])

        def canTraverse(x1, y1, x2, y2, grid):
            if (heights[x1][y1] >= heights[x2][y2]):
                return True
            return False
        
        def reached_Pacific(r,c):
            if (r < 0 or c < 0):
                return True
            return False
        
        def reached_Atlantic(r,c):
            if (r >= ROWS or c >= COLS):
                return True
            return False
        
        def isValid(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS):
                return False
            return True
        
        def dfs(r,c):
            seen = [[False for i in range(COLS)] for i in range(ROWS)]
            stack = []
            stack.append((r,c))
            dirs = [[-1,0], [1,0], [0,-1], [0,1]]
            can_reach_pac = False
            can_reach_atl = False
            while stack:
                x,y = stack.pop()
                print("Going to\t", x,y)

                for dr, dc in dirs:
                    xr = x + dr
                    xc = y + dc

                    if (reached_Pacific(xr,xc)):
                        can_reach_pac = True
                    
                    if (reached_Atlantic(xr,xc)):
                        can_reach_atl = True

                    #checking for the final condition
                    if (can_reach_pac and can_reach_atl):
                        return True

                    if (isValid(xr,xc) and seen[xr][xc] != True) and (canTraverse(x,y,xr,xc,heights)):
                        stack.append((xr,xc))
                        seen[xr][xc] = True
                
            return False
                    
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (dfs(i,j)):
                    res.append([i,j])
    
        return res