// https://leetcode.com/problems/score-of-parentheses/

// Given a balanced parentheses string s, compute the score of the string based on
// the following rule:

////////////////////////////////////////////////////////////////////////////////

// stack = [score at each depth]
// "(" push a deeper depth with score 0
// ")" pop the deepest depth and add score to prev depth
class Solution {
public:
    int scoreOfParentheses(string s) {
        stack<int> scores; scores.push(0); // very first one for ans
        for (char& c : s) {
            if (c == '(') scores.push(0);
            else {
                int score = scores.top(); scores.pop();
                scores.top() += max(2 * score, 1);
            }
        }
        return scores.top();
    }
};
