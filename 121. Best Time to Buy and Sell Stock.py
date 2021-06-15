# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on
# the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot
# achieve any profit, return 0.

################################################################################

# one-pass: maintain min_price, consider all future price as sell price

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1: return 0
        
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profit
