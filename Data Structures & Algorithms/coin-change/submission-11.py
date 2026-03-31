class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #lets do brute force first. Dont think that greedy will necessarily work here. Can do djikstra as well

        n = 10001

        dp = {}

        def bfs():

            stack = []

            stack.append((0,0))

            while stack:

                curramount, currcoins = stack.pop(0)

                #check for the conditions

                if curramount == amount:
                    nonlocal n
                    n = min(n, currcoins) 

                if curramount > amount:
                    continue

                for c in coins:

                    temp = curramount + c

                    if temp in dp:
                        continue
                    else:
                        #otherwise add this to the dp
                        dp[temp] = currcoins + 1
                        stack.append((temp, currcoins + 1))
                
                if curramount not in dp:
                    dp[curramount] = currcoins

        bfs()
        
        if n == 10001:
            return -1
        return n