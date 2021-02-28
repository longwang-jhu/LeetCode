# record each row seperately
# use rowIncrement and filp direction when reach edge rows

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        currRes = [""] * numRows # record each row seperately

        currRow = 0
        rowIncrement = 1

        for i in range(len(s)):
            currRes[currRow] += s[i]
            currRow += rowIncrement

            if currRow == 0 or currRow == numRows - 1: # each the edge rows
                rowIncrement *= -1 # filp direction

        res = ""
        for j in range(numRows):
            res += currRes[j]

        return res