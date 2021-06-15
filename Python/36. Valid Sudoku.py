# https://leetcode.com/problems/valid-sudoku/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:

# Note:

###############################################################################

# one-pass -> Set for rows, cols, and boxes

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    
                    # row
                    if num in rows[i]:
                        return False
                    else:
                        rows[i].add(num)
                    
                    # column
                    if num in cols[j]:
                        return False
                    else:
                        cols[j].add(num)
                    
                    # box
                    box_idx = (i // 3 ) * 3 + j // 3
                    if num in boxes[box_idx]:
                        return False
                    else:
                        boxes[box_idx].add(num)
        return True