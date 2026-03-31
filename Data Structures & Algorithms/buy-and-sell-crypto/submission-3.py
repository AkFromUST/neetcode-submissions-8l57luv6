class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force approach is O(n^2)

        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_profit = max(max_profit, (prices[j] - prices[i]))
        return max_profit