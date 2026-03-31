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
            #print("l: ", l, "\tr: ", r)
            if (prices[r] < prices[l]):
                l = r
                r += 1
            elif (prices[r] >= prices[l]):
                max_profit = max(max_profit, (prices[r] - prices[l]))
                r += 1
            #print("The profits would have been: ", prices[r] - prices[l])
        return max_profit