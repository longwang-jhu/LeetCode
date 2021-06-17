// https://leetcode.com/problems/combination-sum-ii/

// Given a collection of candidate numbers (candidates) and a target number
// (target), find all unique combinations in candidates where the candidate numbers
// sum to target.

// Each number in candidates may only be used once in the combination.

// Note: The solution set must not contain duplicate combinations.

////////////////////////////////////////////////////////////////////////////////

// dfs, sort first
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        dfs(0, candidates, target);
        return ans;
    }
private:
    vector<int> holder;
    vector<vector<int>> ans;
    void dfs(int pos, const vector<int>& nums, int rem) {
        if (rem == 0) {
            ans.push_back(holder); return;
        }
        for (int i = pos; i < nums.size(); ++i) {
            if (i > pos && nums[i] == nums[i-1]) continue;
            if (nums[i] <= rem) {
                holder.push_back(nums[i]);
                dfs(i + 1, nums, rem - nums[i]);
                holder.pop_back();
            }
        }
    }
};
