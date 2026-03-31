class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profits = [0]
        
        for i in range(1, len(prices)):
            profits.append(prices[i] - prices[i-1])

        #kadane's Algorithm on profits

        v_max = -1*float("inf")
        v = 0
        for i in range((len(profits))):
            v += profits[i]

            v = max(v, profits[i])

            v_max = max(v_max, v)

        return v_max
            
        