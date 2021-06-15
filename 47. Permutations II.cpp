// https://leetcode.com/problems/permutations-ii/

// Given a collection of numbers, nums, that might contain duplicates, return all
// possible unique permutations in any order.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<vector<int>> ans;
    vector<int> holder;
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        vector<bool> used(nums.size(), false);
        dfs(nums, used);
        return ans;
    }
    
    void dfs(const vector<int>& nums, vector<bool> used) {
        if (holder.size() == nums.size()) {
            ans.push_back(holder);
            return;
        }
        
        for (int i = 0; i < nums.size(); ++i) {
            if (!used[i]) { // must not used
                // first child, or != prev, or == prev but prev is used
                if (i == 0 or nums[i] != nums[i-1] or used[i-1]) {
                    holder.push_back(nums[i]);
                    used[i] = true;
                    dfs(nums, used);
                    holder.pop_back();
                    used[i] = false;
                }
            }
        }
        return;
    }
};
