# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

# Given an array of integers, return the maximum sum for a non-empty subarray
# (contiguous elements) with at most one element deletion. In other words, you
# want to choose a subarray and optionally delete one element from it so that
# there is still at least one element left and the sum of the remaining
# elements is maximum possible.

# Note that the subarray needs to be non-empty after deleting one element.

###############################################################################

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return arr[0]
        if n == 2: return max(arr[0], arr[1], arr[0] + arr[1])
        
        dp_0 = [float("-inf")] * n # no deletion, must use arr[i]
        dp_1 = [float("-inf")] * n # one deletion, must use arr[i]
        
        # base case
        dp_0[0] = arr[0]
        dp_0[1] = max(arr[1], arr[0] + arr[1])
        dp_1[1] = arr[1]
        
        for i in range(2, n):
            dp_0[i] = max(arr[i], dp_0[i-1] + arr[i])
            dp_1[i] = max(dp_0[i-2] + arr[i], dp_1[i-1] + arr[i])
        
        return max(max(dp_0), max(dp_1))