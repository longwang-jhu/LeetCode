# https://leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a
# number of rows:

###############################################################################

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