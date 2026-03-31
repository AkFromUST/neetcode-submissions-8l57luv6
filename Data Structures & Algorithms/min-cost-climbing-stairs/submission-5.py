class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #this is actually backtracking

        total = float("inf")

        def backtracking(floor, curr_cost):

            if floor == 0 or floor == 1:
                nonlocal total
                print("curr cost is at: ", curr_cost)
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

            