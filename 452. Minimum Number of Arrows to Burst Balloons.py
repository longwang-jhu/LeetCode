# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# There are some spherical balloons spread in two-dimensional space. For each
# balloon, provided input is the start and end coordinates of the horizontal
# diameter. Since it's horizontal, y-coordinates don't matter, and hence the
# x-coordinates of start and end of the diameter suffice. The start is always
# smaller than the end.

# An arrow can be shot up exactly vertically from different points along the
# x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤
# x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow
# once shot keeps traveling up infinitely.

# Given an array points where points[i] = [xstart, xend], return the minimum
# number of arrows that must be shot to burst all balloons.

################################################################################

# count non-overlap ballons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        if len(points) == 1: return 1
        
        n = len(points)
        points.sort(key=lambda x: x[1])
                
        ans = 1
        anchor = 0
        for i in range(1, n):
            if points[anchor][1] < points[i][0]: # no overlap
                ans += 1 # need one more arrow
                anchor = i
        
        return ans
