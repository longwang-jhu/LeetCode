# range = [-2147483648, 2147483647]
# convert to abs(x) first

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31
        
        # convert x to abs(x)
        # Note that abs(INT_MIN) and reverse of INT_MIN will overflow
        if x == INT_MIN:
            return 0
        
        xAbs = abs(x)
        xRev = 0
        
        while xAbs != 0:
            xAbs, digitLast = divmod(xAbs, 10)

            # check overflow
            if (xRev > INT_MAX // 10) or (xRev == INT_MAX // 10 and digitLast > 7):
                return 0
            else:
                xRev = xRev * 10 + digitLast
        
        # assign negative sign if necessary
        if x < 0:
            xRev = -xRev
        
        return xRev