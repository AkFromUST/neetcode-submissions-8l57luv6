class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        v = []
        x = []

        cost.append(0)

        for i in range(len(cost)):
            v.append(-1)
            x.append(-1)
        
        target = len(cost) - 1

        v[target] = 0
        x[target] = 0

        if (len(cost) == 1):
            return cost[0]

        v[target-1] = cost[target-1]
        x[target-1] = cost[target-1]

        for i in range(target-2, -1, -1):
            v[i] = min(v[i+1], v[i+2]) + cost[i]

        for i in range(target-2, 0, -1):
            x[i] = min(x[i+1], x[i+2]) + cost[i]

        return min(v[0], x[1])

