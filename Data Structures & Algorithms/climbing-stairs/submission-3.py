class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1

        
        r = []

        for i in range(n):
            r.append(0)

        r[0] = 1
        r[1] = 2

        for i in range(2, n):
            r[i] = r[i-1] + r[i-2]
        
        return r[n-1]