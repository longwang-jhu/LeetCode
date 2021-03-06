# record change of score from K - 1 to K at change[K]
# for each A[i], find out its the boundary K, make change[k+1] -= 1

class Solution:
    def bestRotation(self, A: List[int]) -> int:
        n = len(A)
        # change of score from K to K + 1, always get a point by moving A[0] to the end
        # note: initialize score for K = 0 as 1 (not matter in the end)
        change = [1] * n # change[K] = point change from K-1 to K
        
        # lose point
        # for A[i], if K = (i - A[i] + n) % n, then A[i] == index, any larger K will cause it to lose point       
        # loop over every A[i] and find out the boundary K
        for i in range(n):
            # loss point 
            change[(i - A[i] + n + 1) % n] -= 1 # only need to record the change from K to K + 1, modify change[K+1]
            
        # compute the cumulative score
        for i in range(1, n):
            change[i] += change[i-1]
        
        return change.index(max(change))