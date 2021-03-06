# log(n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        n_abs = abs(n)
        ans = 1
        while n_abs > 0:
            if n_abs % 2 == 0:
                x *= x
                n_abs /= 2
            else:
                ans *= x
                n_abs -= 1
        
        if n < 0:
            return 1 / ans
        else:
            return ans