class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        """
        #this is actually backtracking

        total = float("inf")

        def backtracking(floor, curr_cost):

            if floor == 0 or floor == 1:
                nonlocal total
                total = min(total, curr_cost)
                return

            if floor < 0:
                return

            if floor - 1 >= 0:
                #take one step
                backtracking(floor-1, curr_cost + cost[floor - 1])

            if floor - 2 >= 0:
                #take two step
                backtracking(floor-2, curr_cost + cost[floor - 2])

        backtracking(len(cost), 0)

        return total
        """

        #lets make the DP version of it. Lets make the recursive relation so we can make the DP formula
        n = len(cost)

        cost.append(0)

        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(
                dp[i-1] + cost[i-1],
                dp[i-2] + cost[i-2]
            )

        return dp[n]