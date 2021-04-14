# https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

###############################################################################

# x^n -> (x*x)^(n/2) -> (x*x*x*x)^(n/2/2) -> ...
# if odd: x^n -> x * x^(n-1)
# time: log(n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        
        n_abs = abs(n)
        ans = 1
        while n_abs > 0:
            if n_abs % 2 == 0:
                x *= x
                n_abs /= 2
            else:
                ans *= x
                n_abs -= 1
        
        return ans if n > 0 else 1 / ans