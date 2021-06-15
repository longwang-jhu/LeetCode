// https://leetcode.com/problems/permutations/

// Given an array nums of distinct integers, return all the possible permutations.
// You can return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

// dfs
class Solution {
public:
    vector<vector<int>> ans;
    vector<int> holder;
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<bool> visited(nums.size(), false);
        dfs(nums, visited);
        return ans;
    }
    
    void dfs(const vector<int> &nums, vector<bool> &visited) {
        if (holder.size() == nums.size()) {
            ans.push_back(holder);
            return;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (!visited[i]) {
                visited[i] = true;
                holder.push_back(nums[i]);
                dfs(nums, visited);
                holder.pop_back();
                visited[i] = false;
            }
        }
        return;
    }
};
