# compare x and xRev

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0: return False
        
        xRev = 0
        xCopy = x
        while xCopy != 0:
            xCopy, digitLast = divmod(xCopy, 10)
            xRev = xRev * 10 + digitLast
        
        return x == xRev