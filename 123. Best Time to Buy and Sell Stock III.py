# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# You are given an array prices where prices[i] is the price of a given stock on
# the ith day.

# Find the maximum profit you can achieve. You may complete at most two
# transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must
# sell the stock before you buy again).

################################################################################

# seperate the data into two parts
# dp_left[i] = profit for prices[0, ..., i], scan forwards
# dp_right[i+1] = profit for prices[i+1, ..., n-1], scan backwards

# method 2
# dp_last_buy[i][j] = trade j times for prices[0, ..., i], last trans is buy
# dp_last_sell[i][j] = trade j times for prices[0, ..., i], last trans is sell
# one trade is one buy + one sell

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1: return 0
        
        n = len(prices)
        # get profit for left part
        dp_left = [0] * n
        min_price = prices[0] # track the best buy price
        for i in range(1, n):
            dp_left[i] = max(dp_left[i-1], prices[i] - min_price) # check if can sell at prices[i]
            min_price = min(min_price, prices[i]) # update best buy price
        
        # get profit for right part
        dp_right = [0] * n
        max_price = prices[-1] # track the best sell price
        for i in range(n - 2, -1, -1):
            dp_right[i] = max(dp_right[i+1], max_price - prices[i]) # check if can buy at prices[i]
            max_price = max(max_price, prices[i]) # update best sell price

        # find the total profit
        max_profit = dp_left[-1]
        for i in range(1, n - 1):
            max_profit = max(max_profit, dp_left[i] + dp_right[i+1])
        return max_profit
