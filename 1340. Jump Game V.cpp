// https://leetcode.com/problems/jump-game-v/

// Given an array of integers arr and an integer d. In one step you can jump from
// index i to index:

// In addition, you can only jump from index i to index j if arr[i] > arr[j] and
// arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k <
// max(i, j)).

// You can choose any index of the array and start jumping. Return the maximum
// number of indices you can visit.

// Notice that you can not jump outside of the array at any time.

////////////////////////////////////////////////////////////////////////////////

// lowest level cannot visit others -> higher levels depends on lower levels -> top-down dp with memo
class Solution {
public:
    int n;
    vector<int> memo; // memo[i] = max indices starting from i
    int maxJumps(vector<int>& arr, int d) {
        n = arr.size();
        memo = vector<int>(n, 0);
        
        vector<int> ans(n, 1);
        for (int i = 0; i < n; ++i) dp(arr, d, i);
        return *max_element(memo.begin(), memo.end());
    }
    
    int dp(vector<int>& arr, int& d, int i) {
        if (memo[i] > 0) return memo[i];
        memo[i] = 1;
        for (int j = i - 1; j >= i - d; --j) { // go left
            if (j < 0 or j >= n or arr[j] >= arr[i]) break; // cannot go further
            memo[i] = max(memo[i], dp(arr, d, j) + 1);
        }
        for (int j = i + 1; j <= i + d; ++j) { // go right
            if (j < 0 or j >= n or arr[j] >= arr[i]) break; // cannot go further
            memo[i] = max(memo[i], dp(arr, d, j) + 1);
        }
        return memo[i];
    }
};
