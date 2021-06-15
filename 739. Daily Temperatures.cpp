// https://leetcode.com/problems/daily-temperatures/

// Given an array of integers temperatures represents the daily temperatures,
// return an array answer such that answer[i] is the number of days you have to
// wait after the ith day to get a warmer temperature. If there is no future day
// for which this is possible, keep answer[i] == 0 instead.

////////////////////////////////////////////////////////////////////////////////

// distance to next larger num -> monostack
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> distToNextLarger(n, 0);
        stack<int> toLeft; // ele = idx
        for (int i = n - 1; i >= 0; --i) {
            // pop when next is not larger
            while (!toLeft.empty() and temperatures[toLeft.top()] <= temperatures[i]) {
                toLeft.pop();
            }
            distToNextLarger[i] = toLeft.empty() ? 0 : toLeft.top() - i;
            toLeft.push(i);
        }
        return distToNextLarger;
    }
    
    vector<int> dailyTemperaturesToRight(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> distToNextLarger(n, 0);
        stack<int> toRight; // ele = idx
        for (int i = 0; i < n; ++i) {
            // pop when next is larger
            while (!toRight.empty() and temperatures[toRight.top()] < temperatures[i]) {
                distToNextLarger[toRight.top()] = i - toRight.top(); // update ans
                toRight.pop();
            }
            toRight.push(i);
        }
        return distToNextLarger;
    }
};
