// https://leetcode.com/problems/permutations/

// Given an array nums of distinct integers, return all the possible permutations.
// You can return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

// dfs
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        n = nums.size();
        visited = vector<bool>(n, false);
        dfs(nums);
        return ans;
    }
private:
    int n;
    vector<bool> visited;
    vector<int> holder;
    vector<vector<int>> ans;
    void dfs(const vector<int>& nums) {
        if (holder.size() == n) {
            ans.push_back(holder); return;
        }
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                visited[i] = true;
                holder.push_back(nums[i]);
                dfs(nums);
                holder.pop_back();
                visited[i] = false;
            }
        }
        return;
    }
};
