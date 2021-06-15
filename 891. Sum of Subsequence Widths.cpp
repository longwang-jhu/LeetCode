// https://leetcode.com/problems/sum-of-subsequence-widths/

// Given an array of integers nums, consider all non-empty subsequences of nums.

// For any sequence seq, let the width of seq be the difference between the maximum
// and minimum element of seq.

// Return the sum of the widths of all subsequences of nums.

// As the answer may be very large, return the answer modulo 109 + 7.

////////////////////////////////////////////////////////////////////////////////

// max and min of all subseqs -> ok to sort
// number of subseqs with min = nums[i] and max = nums[j] is 2^(j - i - 1)
// ans = sum (nums[j] - nums[i]) * 2^(j - i - 1) over all (j > i)

class Solution {
public:
    int sumSubseqWidths(vector<int>& nums) {
        const int MOD = 1e9 + 7;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<long int> pows(n); pows[0] = 1;
        for (int i = 1; i < n; ++i) {
            pows[i] = pows[i - 1] * 2 % MOD;
        }
        long int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = (ans + (pows[i] - pows[n - 1 - i]) * nums[i]) % MOD;
        }
        return (int) ans;
    }
};
