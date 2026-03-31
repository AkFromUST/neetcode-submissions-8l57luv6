class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # brute force approach is O(n^2)
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         max_profit = max(max_profit, (prices[j] - prices[i]))
        # return max_profit

        l , r = 0, 1
        
        if len(prices) <= 1:
            return 0

        max_profit = 0
        while (l < len(prices)) and (r < len(prices)) and l < r:
            if (prices[r] < prices[l]):
                l = r
            else:
                max_profit = max(max_profit, (prices[r] - prices[l]))
            r += 1
        return max_profit