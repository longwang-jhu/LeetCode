# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# You are given an array prices where prices[i] is the price of a given stock on
# the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions
# as you like, but you need to pay the transaction fee for each transaction.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must
# sell the stock before you buy again).

################################################################################

# dp_last_buy[i] = profit for prices[0, ..., i], last trans is buy
# dp_last_sell[i] = profit for prices[0, ..., i], last trans is sell
# one trade is one buy + one sell

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) <= 1: return 0
        
        n = len(prices)
        # initialization
        dp_last_buy = [0] * n
        dp_last_sell = [0] * n
        dp_last_buy[0] = -prices[0] # buy at prices[0]
        
        # loop over price
        for i in range(1, n):
            # ignore prices[i] or buy at prices[i]
            dp_last_buy[i] = max(dp_last_buy[i-1], dp_last_sell[i-1] - prices[i])

            # ignore prices[i] or sell at prices[i] with fee
            dp_last_sell[i] = max(dp_last_sell[i-1], dp_last_buy[i-1] + prices[i] - fee)
        
        return dp_last_sell[-1]
