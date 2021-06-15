# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves
# of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on
# each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the
# same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

################################################################################

# try swap into A[0]
# try swap into B[0]

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        
        # make value = A[0]
        n_swapB = 0 # count for swap B into A
        n_same = 0
        for i in range(0, n):
            if A[i] != A[0] and B[i] != A[0]:
                break # no solution
            elif A[i] == B[i]:
                n_same += 1
            elif B[i] == A[0]: # swap B into A
                n_swapB += 1
            
            if i == n - 1:
                return min(n_swapB, n - n_swapB - n_same)
        
        # make value = B[0]
        n_swapA = 0 # count for swap A into B
        n_same = 0
        for i in range(0, n):
            if A[i] != B[0] and B[i] != B[0]:
                break # no solution
            elif A[i] == B[i]:
                n_same += 1
            elif A[i] == B[0]: # swap A into B
                n_swapA += 1
            
            if i == n - 1:
                return min(n_swapA, n - n_swapA - n_same)
        
        return -1
