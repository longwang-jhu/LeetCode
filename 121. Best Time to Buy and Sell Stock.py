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