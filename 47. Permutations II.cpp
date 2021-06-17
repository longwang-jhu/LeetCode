// https://leetcode.com/problems/permutations-ii/

// Given a collection of numbers, nums, that might contain duplicates, return all
// possible unique permutations in any order.

////////////////////////////////////////////////////////////////////////////////

// dfs, sort first
// avoid duplicate: first child, or != prev, or == prev but prev is used
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        used = vector<bool>(nums.size(), false);
        dfs(nums);
        return ans;
    }
private:
    vector<bool> used;
    vector<int> holder;
    vector<vector<int>> ans;
    void dfs(const vector<int>& nums) {
        if (holder.size() == nums.size()) {
            ans.push_back(holder); return;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (used[i]) continue;
            // first child, or != prev, or == prev but prev is used
            if (i == 0 || nums[i] != nums[i-1] || used[i-1]) {
                holder.push_back(nums[i]);
                used[i] = true;
                dfs(nums);
                holder.pop_back();
                used[i] = false;
            }
        }
        return;
    }
};
