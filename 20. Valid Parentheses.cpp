// https://leetcode.com/problems/valid-parentheses/

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
// determine if the input string is valid.

// An input string is valid if:

////////////////////////////////////////////////////////////////////////////////

// stack
class Solution {
public:
    bool isValid(string s) {
        stack<char> toRight;
        for (char &c : s) {
            if (c == '(' or c == '[' or c == '{') toRight.push(c);
            else if (toRight.empty()) return false;
            else if (c == ')' and toRight.top() != '(') return false;
            else if (c == ']' and toRight.top() != '[') return false;
            else if (c == '}' and toRight.top() != '{') return false;
            else toRight.pop();
        }
        return (toRight.empty()) ? true : false;
    }
};
