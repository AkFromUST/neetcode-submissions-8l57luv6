class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = []

        for i in range((amount)+1):
            dp.append(-1)

        dp[0] = 0

        for i in range(1, amount+1):
            v_min = float("inf")
            for j in range(len(coins)):
                if (i >= coins[j]):
                    v_min = min(v_min, 1 + dp[i - coins[j]])

            dp[i] = v_min


        if (dp[amount] == float("inf")):
            return -1
        else:
            return dp[amount]
        