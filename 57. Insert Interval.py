# https://leetcode.com/problems/insert-interval/

# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their
# start times.

###############################################################################

# loop over intervals -> merge with newIntercal if overlap
# append to ans if no overlap

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        
        ans = []
        inserted = False
        for interval in intervals:
            if interval[1] < newInterval[0]: # no overlap
                ans.append(interval)
            elif interval[0] > newInterval[1]: # no overlap
                if not inserted:
                    ans.append(newInterval)
                    inserted = True
                ans.append(interval)
            else: # overlap, merge intervals
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        if not inserted:
            ans.append(newInterval)
        return ans