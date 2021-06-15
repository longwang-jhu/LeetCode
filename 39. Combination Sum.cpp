// https://leetcode.com/problems/combination-sum/

// Given an array of distinct integers candidates and a target integer target,
// return a list of all unique combinations of candidates where the chosen numbers
// sum to target. You may return the combinations in any order.

// The same number may be chosen from candidates an unlimited number of times. Two
// combinations are unique if the frequency of at least one of the chosen numbers
// is different.

// It is guaranteed that the number of unique combinations that sum up to target is
// less than 150 combinations for the given input.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<vector<int>> ans;
    vector<int> holder;
    
    void dfs(int pos, int remainder, vector<int>& candidates) {
        if (remainder == 0) {
            ans.push_back(holder);
            return;
        }
        for (int i = pos; i < candidates.size(); ++i) {
            if (candidates[i] <= remainder) {
                holder.push_back(candidates[i]);
                dfs(i, remainder - candidates[i], candidates);
                holder.pop_back();
            }
        }
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        dfs(0, target, candidates);
        return ans;
    }
};
