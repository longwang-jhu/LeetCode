# https://leetcode.com/problems/non-overlapping-intervals/

# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of
# the intervals non-overlapping.

################################################################################

# greedy -> sort by end point -> count non-overlapping intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 1: return 0
        
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        
        n_non_overlap = 1
        anchor = 0
        for i in range(1, n):
            if intervals[i][0] >= intervals[anchor][1]:
                n_non_overlap += 1
                anchor = i # move anchor
        
        return n - n_non_overlap
