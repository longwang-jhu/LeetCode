# https://leetcode.com/problems/rotate-function/

# Given an array of integers A and let n to be its length.

# Assume Bk to be an array obtained by rotating the array A k positions clock-
# wise, we define a "rotation function" F on A as follow:

# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

# Calculate the maximum value of F(0), F(1), ..., F(n-1).

# Note: n is guaranteed to be less than 105.

# Example:

# 

###############################################################################

# f(i)          = 0 * A[0] + 1 * A[1] + 2 * A[2] + .... +  (k-1) * A[k-1] + k * A[k]
# f(i+1)        = 1 * A[0] + 2 * A[1] + 3 * A[2] + ...  +     k  * A[k-1] + 0 * A[k] 
# f(i+1) - f(i) =     A[0]   +   A[1]   +   A[2] + ...  +          A[k-1] - k * A[k] 
#               = total - A[k] * array.length
# f(i+1) = f(i) + total - n * last element of F(i)

class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return 0

        # compute F(0)
        curr = 0
        for i, v in enumerate(A):
            curr += i * v
        
        # compute F(1) to F(n-1)
        total = sum(A)
        ans = curr
        for i in range(1, n):
            curr = curr + total - n * A[-i]
            ans = max(ans, curr)
        
        return ans