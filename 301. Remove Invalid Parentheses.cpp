// https://leetcode.com/problems/remove-invalid-parentheses/

// Given a string s that contains parentheses and letters, remove the minimum
// number of invalid parentheses to make the input string valid.

// Return all the possible results. You may return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    unordered_set<string> ans;
    string holder;
    vector<string> removeInvalidParentheses(string s) {
        int leftExtra = 0, rightExtra = 0; // count the no. of extra '(' and ')'
        for (char c : s) {
            if (c == '(') ++leftExtra;
            else if (c == ')') {
                if (leftExtra == 0) ++rightExtra;
                else --leftExtra;
            }
        }
        dfs(s, leftExtra, rightExtra, 0, 0, 0);
        vector<string> ansVec; ansVec.insert(ansVec.end(), ans.begin(), ans.end());
        return ansVec;
    }
    
    void dfs(string& s, int leftExtra, int rightExtra,
             int leftCount, int rightCount, int idx) {
        if (idx == s.size()) {
            if (leftExtra == 0 and rightExtra == 0) ans.insert(holder);
            return;
        }
        
        if (s[idx] == '(') {
            if (leftExtra > 0) { // skip '('
                dfs(s, leftExtra - 1, rightExtra, leftCount, rightCount, idx + 1);
            }
            holder.push_back('('); // keep '('
            dfs(s, leftExtra, rightExtra, leftCount + 1, rightCount, idx + 1);
            holder.pop_back();
        } else if (s[idx] == ')') {
            if (rightExtra > 0) { // skip ')'
                dfs(s, leftExtra, rightExtra - 1, leftCount, rightCount, idx + 1);
            }
            if (leftCount > rightCount) { // keep ')'
                holder.push_back(')');
                dfs(s, leftExtra, rightExtra, leftCount, rightCount + 1, idx + 1);
                holder.pop_back();
            }
        } else {
            holder += s[idx];
            dfs(s, leftExtra, rightExtra, leftCount, rightCount, idx + 1);
            holder.pop_back();
        }
        return;
    }
};
