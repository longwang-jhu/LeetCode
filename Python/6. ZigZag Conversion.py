# https://leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a
# number of rows:

###############################################################################

# rearrange string -> display by rows -> record each row seperately
# use row_incr = +/- 1 and filp direction when reach the edge row

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 0: return None
        if numRows == 1: return s
        
        n_row = numRows
        rows = [''] * n_row # record each row seperately
        
        curr_row = 0
        row_incr = 1
        for i in range(len(s)):
            rows[curr_row] += s[i]
            curr_row += row_incr
            if curr_row == 0 or curr_row == n_row - 1: # each the edge row
                row_incr *= -1 # filp direction
        
        return ''.join(rows)