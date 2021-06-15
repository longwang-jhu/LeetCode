// https://leetcode.com/problems/combination-sum-iii/

// Find all valid combinations of k numbers that sum up to n such that the
// following conditions are true:

// Return a list of all possible valid combinations. The list must not contain the
// same combination twice, and the combinations may be returned in any order.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<vector<int>> ans;
    vector<int> holder;
    void dfs(int pos, int remainder, int k) {
        if (holder.size() == k) {
            if (remainder == 0) {
                ans.push_back(holder);
                return;
            } else return;
        }
        for (int i = pos; i < 10; ++i) {
            if (i <= remainder) {
                holder.push_back(i);
                dfs(i + 1, remainder - i, k);
                holder.pop_back();
            }
        }
    }
    
    vector<vector<int>> combinationSum3(int k, int n) {
        dfs(1, n, k);
        return ans;
    }
};
