class Solution:
    def climbStairs(self, n: int) -> int:
        
        # I am allowed to take either one step or two step. The way to do it recursively would be to either take step 1 or take step 2

        res = 0

        def backtracking(floor):

            if floor == 0:
                nonlocal res
                res += 1
                return
            
            if floor < 0:
                return

            #take first step
            backtracking(floor - 1)
            backtracking(floor - 2)

        backtracking(n)

        #but the above has lots of repeated patterns. So lets try to memorize them

        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

