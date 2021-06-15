# https://leetcode.com/problems/smallest-rotation-with-highest-score/

#  Given an array A, we may rotate it by a non-negative integer K so that the
# array becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ...,
# A[K-1].  Afterward, any entries that are less than or equal to their index
# are worth 1 point.

# For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes
# [1, 3, 0, 2, 4].  This is worth 3 points because 1 > 0 [no points], 3 > 1 [no
# points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

# Over all possible rotations, return the rotation index K that corresponds to
# the highest score we could receive.  If there are multiple answers, return
# the smallest such index K.

# So we should choose K = 3, which has the highest score.

###############################################################################

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