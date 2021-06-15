// https://leetcode.com/problems/combination-sum-ii/

// Given a collection of candidate numbers (candidates) and a target number
// (target), find all unique combinations in candidates where the candidate numbers
// sum to target.

// Each number in candidates may only be used once in the combination.

// Note: The solution set must not contain duplicate combinations.

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
            if (i == pos or candidates[i] != candidates[i-1]) { // avoid duplicates
                if (candidates[i] <= remainder) {
                    holder.push_back(candidates[i]);
                    dfs(i + 1, remainder - candidates[i], candidates);
                    holder.pop_back();
                }
            }
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        dfs(0, target, candidates);
        return ans;
    }
};
