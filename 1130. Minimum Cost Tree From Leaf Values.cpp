// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

// Given an array arr of positive integers, consider all binary trees such that:

// Among all possible binary trees considered, return the smallest possible sum of
// the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit
// integer.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<vector<int>> memo;
    int mctFromLeafValues(vector<int>& arr) {
        // return mctFromLeftValuesTopDownDP(arr);
        // return mctFromLeftValuesGreedy(arr);
        return mctFromLeftValuesMonoStack(arr);
    }
    
    // dp[i][j] = min cost tree from arr[i...j]
    // dp[i][j] = min over k { dp[i][k] + dp[k+1][j] + max(arr[i...k]) * max(arr[k+1...j]) }
    // time: O(n^3)
    int mctFromLeftValuesTopDownDP(vector<int>& arr) {
        int n = arr.size();
        memo = vector<vector<int>>(n, vector<int>(n, 0));
        return dp(arr, 0, n - 1);
    }
    
    int dp(vector<int>& arr, int i, int j) {
        if (i >= j) return 0;
        if (memo[i][j] > 0) return memo[i][j];
        
        int ans = INT_MAX;
        for (int k = i; k + 1 <= j; ++k) {
            int rootVal = *max_element(arr.begin() + i, arr.begin() + k + 1); // max(arr[i...k])
            rootVal *= *max_element(arr.begin() + k + 1, arr.begin() + j + 1); // max(arr[k+1...j])
            ans = min(ans, dp(arr, i, k) + dp(arr, k + 1, j) + rootVal);
        }
        memo[i][j] = ans;
        return memo[i][j];
    }
    
    // greedy, pick the smallest num, build tree with its smaller neighbor, remove the smallest num
    // time: O(n^2)
    int mctFromLeftValuesGreedy(vector<int>& arr) {
        int ans = 0;
        while (arr.size() > 1) {
            auto minPtr = min_element(arr.begin(), arr.end());
            // build tree with smallest num and its smaller neighbor
            if (minPtr == arr.begin()) {
                ans += *minPtr * *(minPtr + 1);
            } else if (minPtr == arr.end() - 1) {
                ans += *(minPtr - 1) * *minPtr;
            } else {
                ans += *minPtr * min(*(minPtr - 1), *(minPtr + 1));
            }
            arr.erase(minPtr);
        }
        return ans;
    }
    
    // monostack, build stack toRight
    // when find a prevLess, build tree with its smaller neighbor and then pop it
    int mctFromLeftValuesMonoStack(vector<int>& arr) {
        stack<int> toRight; toRight.push(INT_MAX);
        int ans = 0, n = arr.size();
        for (int i = 0; i < n; ++i) {
            while (!toRight.empty() and toRight.top() <= arr[i]) {
                int prevLess = toRight.top(); toRight.pop();
                ans += prevLess * min(toRight.top(), arr[i]);
            }
            toRight.push(arr[i]);
        }
        while (toRight.size() > 2) { // the very first element is INT_MAX
            int curr = toRight.top(); toRight.pop();
            ans += toRight.top() * curr;
        }
        return ans;
    }
};
