// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

// There are some spherical balloons spread in two-dimensional space. For each
// balloon, provided input is the start and end coordinates of the horizontal
// diameter. Since it's horizontal, y-coordinates don't matter, and hence the
// x-coordinates of start and end of the diameter suffice. The start is always
// smaller than the end.

// An arrow can be shot up exactly vertically from different points along the
// x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤
// x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow
// once shot keeps traveling up infinitely.

// Given an array points where points[i] = [xstart, xend], return the minimum
// number of arrows that must be shot to burst all balloons.

////////////////////////////////////////////////////////////////////////////////

// greedy
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.empty()) return 0;
        
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>&b) {
            return a[1] < b[1];
        });
        
        int nonOverlap = 1;
        int i = 1, anchor = 0;
        while (i < points.size()) {
            if (points[anchor][1] < points[i][0]) {
                ++nonOverlap;
                anchor = i;
            }
            ++i;
        }
        return nonOverlap;
    }
};
