# https://leetcode.com/problems/coin-change-2/

# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of
# money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

###############################################################################

# backpack
# dp[i][j] = no. of ways to use first i coins to get ammount=j

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
                
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for i in range(n + 1): # only one way to get amount=0
            dp[i][0] = 1
        for j in range(1, amount + 1): # no way to get amount>0 without coins
            dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i-1][j] # not use the new coin
                if coins[i-1] <= j: # may use the new coin
                    dp[i][j] += dp[i][j - coins[i-1]]
        
        return dp[-1][-1]