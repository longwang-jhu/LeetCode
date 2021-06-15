// https://leetcode.com/problems/non-overlapping-intervals/

// Given an array of intervals intervals where intervals[i] = [starti, endi],
// return the minimum number of intervals you need to remove to make the rest of
// the intervals non-overlapping.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        int n = intervals.size();
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int nonOverlap = 1, anchor = 0;
        for (int i = 1; i < n; ++i){
            if (intervals[anchor][1] <= intervals[i][0]) {
                ++nonOverlap;
                anchor = i; // move anchor
            }
        }
        return n - nonOverlap;
    }
};
