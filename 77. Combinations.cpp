// https://leetcode.com/problems/combinations/

// Given two integers n and k, return all possible combinations of k numbers out of
// the range [1, n].

// You may return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<vector<int>> ans;
    vector<int> holder;
    
    vector<vector<int>> combine(int n, int k) {
        dfs(n, k, 0);
        return ans;
    }
    
    void dfs(const int &n, const int &k, int i) {
        if (holder.size() == k) {
            ans.push_back(holder);
            return;
        }
        
        for (int j = i + 1; j <= n; ++j) {
            holder.push_back(j);
            dfs(n, k, j);
            holder.pop_back();
        }
        return;
    }
    
};
