// https://leetcode.com/problems/candy/

// There are n children standing in a line. Each child is assigned a rating value
// given in the integer array ratings.

// You are giving candies to these children subjected to the following
// requirements:

// Return the minimum number of candies you need to have to distribute the candies
// to the children.

////////////////////////////////////////////////////////////////////////////////

// greedy -> init ans = [1,...,1]
// forward pass and backward pass to update ans
class Solution {
public:
    int candy(vector<int>& ratings) {
        if (ratings.size() == 1) return 1;
        
        int n = ratings.size();
        vector<int> ans(n, 1);
        // forward pass
        for (int i = 1; i <= n - 1; ++i) {
            if (ratings[i] > ratings[i-1]) ans[i] = ans[i-1] + 1;
        }
        // backward pass
        for (int i = n - 2; i >= 0; --i) {
            if (ratings[i] > ratings[i+1]) ans[i] = max(ans[i], ans[i+1] + 1);
        }
        
        return accumulate(ans.begin(), ans.end(), 0);
    }
};
