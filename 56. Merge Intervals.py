# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals that
# cover all the intervals in the input.

################################################################################

# merge interval -> sort -> combine overlap
# time: O(nlogn), space: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1: return intervals
        
        intervals.sort(key = lambda x: x[0]) # sort by start_val
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if ans[-1][1] < interval[0]: # no overlap
                ans.append(interval)
            else: # overlap, merge end point
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans
