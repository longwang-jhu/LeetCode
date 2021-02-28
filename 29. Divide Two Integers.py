class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = - 2 ** 31
        INT_MAX = 2 ** 31 - 1
        
        if dividend == 0: return 0
        if divisor == 1: return dividend
        if divisor == -1:
            if dividend > INT_MIN: return -dividend
            else: return INT_MAX
        
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        
        a = abs(dividend)
        b = abs(divisor)
        
        def divideSimple(a: int, b: int) -> int:
            if a < b: return 0
            count = 1
            bTemp = b
            while bTemp * 2 <= a:
                count *= 2
                bTemp *= 2
            return count + divideSimple(a - bTemp, b)
        
        res = divideSimple(a,b)
        
        if sign > 0:
            if res > INT_MAX:
                res == INT_MAX
            return res
        else:
            return -res;