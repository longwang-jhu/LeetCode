# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# You are given an array prices where prices[i] is the price of a given stock
# on the ith day.

# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).

# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).

###############################################################################

# greedy -> repeatly buy prices[i] and sell prices[i+1] if profitable

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1: return 0
        
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(0, prices[i+1] - prices[i])
        return max_profit