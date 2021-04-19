# https://leetcode.com/problems/coin-change/

# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.

# You may assume that you have an infinite number of each kind of coin.

###############################################################################

# backpack -> dp[i][j] = fewest coins of first i coins to get amount j

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        # init
        dp = [[float("inf")] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1): # 0 way to get amount 0
            dp[i][0] = 0
        # dp[0][j] = float("inf") # no way get any amount without coin
        
        # dp
        for i in range(n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i-1][j] # not use coins[i-1]
                if coins[i-1] <= j: # use coins[i-1]
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i-1]] + 1)
        
        if dp[-1][-1] == float("inf"):
            return -1
        return dp[-1][-1]