class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Two ptrs
        
        v_min = float("inf")

        max_profit = -1*float("inf")
        for i in range(len(prices)):
            v_min = min(v_min, prices[i])

            profit = prices[i] - v_min            

            max_profit = max(profit, max_profit)

        return max_profit
        