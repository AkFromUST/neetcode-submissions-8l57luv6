class Solution:
    def climbStairs(self, n: int) -> int:
        
        # I am allowed to take either one step or two step
        # recursively the way would be too

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

        return res