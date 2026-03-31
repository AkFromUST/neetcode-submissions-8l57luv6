class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Intuitions:
            - Run BFS (why will DFS not work?)
            - Return the max layer it transcended
        """

        #constants
        ROWS, COLS = len(grid), len(grid[0])

        #checking if any fresh fruits exists. If not, return 0 since it takes 0 mins to rotten
        cont_fresh = 0
        cont_rotten = 0

        #rottenn tomatoes coordinates
        rotten_coord = []

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    cont_fresh = cont_fresh + 1
                if (grid[i][j] == 2):
                    cont_rotten = cont_rotten + 1
                    rotten_coord.append((i,j))
        if (cont_fresh == 0):
            return 0
        if (cont_rotten == 0):
            return -1

        print("Executing BFS")

        def isValid(r,c):
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS):
                return False
            return True

        def bfs(x,y):
            queue = []
            layer = 0
            for i in range(len(rotten_coord)):
                x,y = rotten_coord[i]
                queue.append((x,y,layer))

            dirs = [[-1,0], [1,0], [0,-1], [0,1]]
            max_layer = 0

            seen = []
            for i in range(ROWS):
                seen.append([])
                for j in range(COLS):
                    seen[i].append(False)

            while queue:
                ir, ic, ilayer = queue.pop(0)
                for dr, dc in dirs:
                    r = ir + dr
                    c = ic + dc

                    if (isValid(r,c) and (seen[r][c] != True) and (grid[r][c] != 0) and (grid[r][c] != 2)):
                        queue.append((r,c, ilayer+1))
                        seen[r][c] = True
                        max_layer = max(max_layer, ilayer+1)

                seen[ir][ic] = True
            
            
            #checking if any component is left
            for i in range(ROWS):
                for j in range(COLS):
                    if (grid[i][j] == 1 and seen[i][j] == False):
                        return -1
            
            return max_layer

        num_layer = float("inf")
        for i in range(ROWS):
            for j in range(COLS):
                if (grid[i][j] == 2):
                    print(bfs(i,j))
                    num_layer  =  min(bfs(i,j), num_layer)
                    
        return num_layer