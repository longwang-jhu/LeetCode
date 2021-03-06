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