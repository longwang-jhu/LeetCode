// https://leetcode.com/problems/combinations/

// Given two integers n and k, return all possible combinations of k numbers out of
// the range [1, n].

// You may return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        dfs(0, n, k); return ans;
    }
private:
    vector<int> holder;
    vector<vector<int>> ans;
    void dfs(int i, const int& n, const int& k) {
        if (holder.size() == k) {
            ans.push_back(holder); return;
        }
        for (int j = i + 1; j <= n; ++j) {
            holder.push_back(j);
            dfs(j, n, k);
            holder.pop_back();
        }
        return;
    }
    
};
