# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock
# on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.

###############################################################################

# one pass: set min_price = price if it lower, otherwise consider it as sell price

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 2 ** 31 - 1
        for price in prices:
            if price < min_price: # buy
                min_price = price
            elif price - min_price > max_profit: # sell
                max_profit = price - min_price
                
        return max_profit