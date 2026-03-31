class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
         #lets do a DFS. If the surrounding is 0, then its an island. If its a 1, then do DFS on it as well
        row, col = len(grid), len(grid[0])
        seen = []
        ans = 0

        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(False)
            seen.append(temp)

        def dfs(i,j):
        
            if (i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0 or seen[i][j] == True):
                return 0

            #otherwise, lets do DFS on every neighbour
            seen[i][j] = True #changing it to seen to avoid duplication or infinite loop
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1)
    
        for i in range(row):
            for j in range(col):
                if (grid[i][j] == 1 and seen[i][j] == False):
                    ans = max (ans, dfs(i,j))
        return ans