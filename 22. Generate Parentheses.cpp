// https://leetcode.com/problems/generate-parentheses/

// Given n pairs of parentheses, write a function to generate all combinations of
// well-formed parentheses.

////////////////////////////////////////////////////////////////////////////////

// dfs
class Solution {
public:
    vector<string> ans;
    string holder;
    vector<string> generateParenthesis(int n) {
        dfs(n, 0, 0);
        return ans;
    }
    
    void dfs(int n, int left, int right) {
        if (left == n and right == n) {
            ans.push_back(holder); return;
        }
        if (left < n) {
            holder.push_back('(');
            dfs(n, left + 1, right);
            holder.pop_back();
        }
        if (left > right) {
            holder.push_back(')');
            dfs(n, left, right + 1);
            holder.pop_back();
        }
    }
};
