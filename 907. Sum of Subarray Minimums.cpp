// https://leetcode.com/problems/sum-of-subarray-minimums/

// Given an array of integers arr, find the sum of min(b), where b ranges over
// every (contiguous) subarray of arr. Since the answer may be large, return the
// answer modulo 109 + 7.

////////////////////////////////////////////////////////////////////////////////

// for each i, find subarrays where nums[i] is the min
// contiguous subarray -> find idx of prevLessEqual (equal is for duplicates) and nextLess
// [l | ...i...| r] -> (i - l) * (r - i) number of subarrays of which nums[i] is the min
// ans += nums[i] * (i - l) * (r - i)
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        const int MOD = 1e9 + 7;
        int n = arr.size();
        vector<int> prevLessEqualIdx(n), nextLessIdx(n);
        stack<int> toRight, toLeft;
        for (int i = 0; i < n; ++i) {
            while (!toRight.empty() and arr[toRight.top()] > arr[i]) {
                toRight.pop();
            }
            prevLessEqualIdx[i] = toRight.empty() ? -1 : toRight.top();
            toRight.push(i);
        }
        for (int i = n - 1; i >= 0; --i) {
            while (!toLeft.empty() and arr[toLeft.top()] >= arr[i]) {
                toLeft.pop();
            }
            nextLessIdx[i] = toLeft.empty() ? n : toLeft.top();
            toLeft.push(i);
        }
        
        long int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = (ans + (long int) arr[i] * (i - prevLessEqualIdx[i]) * (nextLessIdx[i] - i)) % MOD;
        }
        return (int) ans;
    }
};
