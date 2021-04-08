# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# You are given an integer array prices where prices[i] is the price of a given
# stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k
# transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).

###############################################################################

# dp_last_buy[i][j] = trade j times for prices[0, ..., i], last trans is buy
# dp_last_sell[i][j] = trade j times for prices[0, ..., i], last trans is sell
# one trade is one buy + one sell

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or len(prices) <= 1: return 0
        
        n = len(prices)
        # initialization
        dp_last_buy = [[0] * (k + 1) for _ in range(n)]
        dp_last_sell = [[0] * (k + 1) for _ in range(n)]
        for j in range(k + 1): # buy at prices[0]
            dp_last_buy[0][j] = -prices[0]
        
        # loop over price and k
        for i in range(1, n):
            for j in range(1, k + 1):
                # ignore prices[i] or buy at prices[i]
                dp_last_buy[i][j] = max(dp_last_buy[i-1][j], dp_last_sell[i-1][j-1] - prices[i])
                
                # ignore prices[i] or sell at prices[i]
                dp_last_sell[i][j] = max(dp_last_sell[i-1][j], dp_last_buy[i-1][j] + prices[i])
        
        return dp_last_sell[-1][-1]