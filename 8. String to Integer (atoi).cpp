// https://leetcode.com/problems/string-to-integer-atoi/

// Implement the myAtoi(string s) function, which converts a string to a 32-bit
// signed integer (similar to C/C++'s atoi function).

// The algorithm for myAtoi(string s) is as follows:

// Note:

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int myAtoi(string s) {
        if (s.size() == 0) return 0;        
        int n = s.size(), ans = 0, i = 0, sign = 1;
        // skip leading whitespace
        while (i < n and s[i] == ' ') ++i;
        // check for sign
        if (i < n and (s[i] == '+' or s[i] == '-')) sign = s[i++] == '+' ? 1 : -1;
        // check for digits
        while (i < n and s[i] >= '0' and s[i] <= '9') {
            int lastDigit = s[i] - '0';
            if (ans > INT_MAX / 10 or (ans == INT_MAX / 10 and lastDigit > 7)) return INT_MAX; // overflow
            if (ans < INT_MIN / 10 or (ans == INT_MIN / 10 and lastDigit > 8)) return INT_MIN; // underflow
            ans = ans * 10 + sign * lastDigit;
            i++;
        }
        return ans;
    }
};
