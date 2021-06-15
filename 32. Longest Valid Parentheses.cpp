// https://leetcode.com/problems/longest-valid-parentheses/

// Given a string containing just the characters '(' and ')', find the length of
// the longest valid (well-formed) parentheses substring.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int longestValidParentheses(string s) {
        // return longestValidParenthesesStack(s);
        return longestValidParenthesesTwoPtrs(s);
        
        if (s.size() <= 1) return 0;
        // dp[i] = longest valid in s[i...n-1] must use s[i]
        vector<int> dp(s.size());
        for (int i = s.size() - 2; i >= 0; --i) {
            if (s[i] == '(') {
                // find farthest ')': s[i | len = dp[i+1] | j]
                int j = i + dp[i + 1] + 1;
                if (j < s.size() and s[j] == ')') {
                    dp[i] = dp[i + 1] + 2;
                    // s[i...j | dp[j+1]], append valid substr after j
                    if (j < s.size() - 1) dp[i] += dp[j+1];
                }
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
    
    int longestValidParenthesesStack(string s) {
        int ans = 0;
        // stack[i] = index of '('
        stack<int> leftPStack;
        leftPStack.push(-1); // insert a bad ')' at index -1
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') leftPStack.push(i);
            else { // s[i] == ')'
                leftPStack.pop();
                if (leftPStack.empty()) { // record the most recent bad ')'
                    leftPStack.push(i);
                }
                else {
                    // update ans, distance to the most recent bad ')' or unused '('
                    ans = max(ans, i - leftPStack.top());
                } 
            }
        }
        return ans;
    }
    
    int longestValidParenthesesTwoPtrs(string s) {
        int left = 0, right = 0, ans = 0;
        for (int i = 0; i < s.size(); ++i) {
            (s[i] == '(') ? ++left : ++right;
            if (left == right) ans = max(ans, right * 2);
            else if (right >= left) left = right = 0; // reset
        }
        left = right = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            (s[i] == '(') ? ++left : ++right;
            if (left == right) ans = max(ans, left * 2);
            else if (left >= right) left = right = 0; // reset
        }
        return ans;
    }
};
