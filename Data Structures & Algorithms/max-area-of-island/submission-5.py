class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #same as the prev question. Just return the total nodes in the graphs too

        ROWS, COLS = len(grid), len(grid[0])

        def _isValid(x,y):
            #helper function
            if ((x < 0) or (x >= ROWS)) or ((y < 0) or (y >= COLS)) or (grid[x][y] == 0):
                return False
            return True

        seen = set()
        nei = [[-1,0], [1,0], [0,-1], [0,1]]

        def dfs(x,y):
            stack = []
            stack.append((x,y))
            nodes = 0
            while stack:
                ix,iy = stack.pop()
                
                print("\tAt: ", (ix,iy))
                seen.add((ix,iy))
                for r, c in nei:
                    dr, dc = ix + r, iy + c
                    if _isValid(dr, dc) and ((dr,dc) not in seen):
                        stack.append((dr,dc))
                        seen.add((dr,dc))
                        nodes += 1
            return nodes + 1

        maxN = 0
        for i in range(ROWS):
            for j in range(COLS):
                if ((i,j) not in seen) and grid[i][j] == 1:
                    print("Starting at: ", (i,j))
                    nodes = dfs(i,j)
                    maxN = max(maxN, nodes)

        return maxN
