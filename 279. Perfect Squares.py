# https://leetcode.com/problems/perfect-squares/

# Given an integer n, return the least number of perfect square numbers that sum
# to n.

# A perfect square is an integer that is the square of an integer; in other words,
# it is the product of some integer with itself. For example, 1, 4, 9, and 16 are
# perfect squares while 3 and 11 are not.

################################################################################

# dp[i] = ans for number i

class Solution:
    ans = dict()
    ans[0] = 0
    def numSquares(self, n: int) -> int:
        ans = self.ans
        if n in ans: return ans[n]
        
        dp = [float('inf')] * (n + 1)
        for i in range(1, n + 1):
            if i in self.ans:
                continue
            
            ans[i] = float('inf')
            j = 1
            while j**2 <= i:
                ans[i] = min(ans[i], ans[i - j**2] + 1)
                j += 1
        
        return ans[n]
